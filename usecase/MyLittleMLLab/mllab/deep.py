"""Boucles courtes et explicites : CPU par défaut, GPU facultatif."""
from pathlib import Path
import copy,time
import numpy as np
import pandas as pd
from .core import ROOT,FEATURES,read_data,evaluate

def setup(seed=2026):
    import torch
    torch.manual_seed(seed);np.random.seed(seed);torch.set_num_threads(2)
    return torch

def train_loop(model,train_x,train_y,valid_x,valid_y,epochs=10,lr=.001,batch_size=64,patience=4,trainable=None):
    torch=setup();from torch import nn
    device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model=model.to(device)
    X=torch.as_tensor(train_x,dtype=torch.float32);y=torch.as_tensor(train_y,dtype=torch.long)
    VX=torch.as_tensor(valid_x,dtype=torch.float32);vy=torch.as_tensor(valid_y,dtype=torch.long)
    loader=torch.utils.data.DataLoader(torch.utils.data.TensorDataset(X,y),batch_size=batch_size,shuffle=True,generator=torch.Generator().manual_seed(2026))
    optim=torch.optim.AdamW(trainable or [p for p in model.parameters() if p.requires_grad],lr=lr,weight_decay=.01)
    criterion=nn.CrossEntropyLoss();best=float('inf');best_state=None;stale=0;history=[];start=time.perf_counter()
    def validation():
        model.eval();loss_sum=0.;predictions=[]
        with torch.no_grad():
            for begin in range(0,len(vy),batch_size):
                xb=VX[begin:begin+batch_size].to(device);yb=vy[begin:begin+batch_size].to(device)
                logits=model(xb);loss_sum+=criterion(logits,yb).item()*len(yb)
                predictions.append(logits.softmax(1).cpu().numpy())
        return loss_sum/len(vy),np.concatenate(predictions)
    for epoch in range(epochs):
        model.train();total=0.
        if hasattr(model,'backbone_frozen') and model.backbone_frozen:
            for child in list(model.children())[:-1]:child.eval()
        for xb,yb in loader:
            xb=xb.to(device);yb=yb.to(device)
            optim.zero_grad(set_to_none=True);logits=model(xb);loss=criterion(logits,yb);loss.backward();optim.step();total+=loss.item()*len(yb)
        val_loss,_=validation()
        history.append({'epoch':epoch+1,'train_loss':total/len(y),'valid_loss':val_loss})
        if val_loss<best-1e-5:best=val_loss;best_state={k:v.detach().cpu().clone() for k,v in model.state_dict().items()};stale=0
        else:stale+=1
        if stale>=patience:break
    model.load_state_dict(best_state);_,prob=validation();model=model.cpu().eval()
    return model,pd.DataFrame(history),prob,time.perf_counter()-start

def mlp_experiment(epochs=18,lr=.003,hidden=48):
    torch=setup();from torch import nn
    a=read_data('train');b=read_data('valid')
    model=nn.Sequential(nn.Linear(64,hidden),nn.ReLU(),nn.Dropout(.2),nn.Linear(hidden,10))
    return train_loop(model,a[FEATURES].to_numpy()/16,a.target.to_numpy(),b[FEATURES].to_numpy()/16,b.target.to_numpy(),epochs,lr)

def cnn_experiment(epochs=10):
    torch=setup();from torch import nn
    a=read_data('train');b=read_data('valid')
    model=nn.Sequential(nn.Conv2d(1,12,3,padding=1),nn.ReLU(),nn.Conv2d(12,24,3,padding=1),nn.ReLU(),nn.Flatten(),nn.Linear(24*8*8,10))
    return train_loop(model,a[FEATURES].to_numpy().reshape(-1,1,8,8)/16,a.target.to_numpy(),b[FEATURES].to_numpy().reshape(-1,1,8,8)/16,b.target.to_numpy(),epochs,.003)

def load_text_model(allow_download=False):
    from transformers import BertTokenizer,BertConfig,BertForSequenceClassification
    from huggingface_hub import hf_hub_download
    name='prajjwal1/bert-tiny'
    revision='6f75de8b60a9f8a2fdf7b69cbd86d9e64bcb3837'
    vocab=hf_hub_download(name,'vocab.txt',revision=revision,local_files_only=not allow_download)
    tokenizer=BertTokenizer(vocab=vocab,do_lower_case=True)
    config=BertConfig.from_pretrained(name,num_labels=2,revision=revision,local_files_only=not allow_download)
    config._commit_hash=revision
    model=BertForSequenceClassification.from_pretrained(name,config=config,revision=revision,local_files_only=not allow_download)
    return tokenizer,model

def pretrained_text(allow_download=False,fine_tune=False,epochs=2):
    torch=setup();tokenizer,model=load_text_model(allow_download)
    train=pd.read_csv(ROOT/'data/reviews_train.csv');valid=pd.read_csv(ROOT/'data/reviews_valid.csv')
    tr=tokenizer(train.text.tolist(),padding=True,truncation=True,max_length=64,return_tensors='pt')
    va=tokenizer(valid.text.tolist(),padding=True,truncation=True,max_length=64,return_tensors='pt')
    start=time.perf_counter()
    if not fine_tune:
        from sklearn.linear_model import LogisticRegression
        model.eval()
        with torch.no_grad():
            # Pooling masqué : les tokens de padding ne contribuent pas.
            def embed(batch):
                h=model.bert(**batch).last_hidden_state;mask=batch['attention_mask'].unsqueeze(-1)
                return ((h*mask).sum(1)/mask.sum(1)).numpy()
            X=embed(tr);V=embed(va)
        classifier=LogisticRegression(max_iter=400).fit(X,train.target)
        pred=classifier.predict_proba(V)
        return {'accuracy':float((pred.argmax(1)==valid.target.to_numpy()).mean()),'seconds':time.perf_counter()-start,'history':[],'mode':'encodeur préentraîné gelé + classifieur linéaire'}
    from torch.utils.data import DataLoader,TensorDataset
    loader=DataLoader(TensorDataset(tr['input_ids'],tr['attention_mask'],torch.tensor(train.target.to_numpy())),batch_size=16,shuffle=True,generator=torch.Generator().manual_seed(2026))
    optim=torch.optim.AdamW(model.parameters(),lr=3e-5);history=[]
    for epoch in range(epochs):
        model.train();losses=[]
        for ids,mask,y in loader:
            optim.zero_grad(set_to_none=True);loss=model(input_ids=ids,attention_mask=mask,labels=y).loss;loss.backward();optim.step();losses.append(loss.item())
        model.eval()
        with torch.no_grad():res=model(**va,labels=torch.tensor(valid.target.to_numpy()))
        history.append({'epoch':epoch+1,'train_loss':float(np.mean(losses)),'valid_loss':res.loss.item()})
    with torch.no_grad():pred=model(**va).logits.softmax(1).numpy()
    return {'accuracy':float((pred.argmax(1)==valid.target.to_numpy()).mean()),'seconds':time.perf_counter()-start,'history':history,'mode':'adaptation du transformer préentraîné (poids finaux, pas sélection sur test)'}

def pretrained_vision(allow_download=False,fine_tune=False):
    torch=setup();from torchvision.models import resnet18,ResNet18_Weights
    from torch import nn
    weights=ResNet18_Weights.DEFAULT
    cache=Path(torch.hub.get_dir())/'checkpoints'/Path(weights.url).name
    if not cache.exists() and not allow_download:raise FileNotFoundError('Poids ResNet18 absents ; préparer les assets avant la séance.')
    model=resnet18(weights=weights)
    # Petit sous-échantillon stratifié pour vérifier le parcours ; exercice long = augmenter le budget.
    from sklearn.model_selection import train_test_split
    train=read_data('train');valid=read_data('valid')
    train=train.iloc[train_test_split(np.arange(len(train)),train_size=120,stratify=train.target,random_state=2026)[0]]
    valid=valid.iloc[train_test_split(np.arange(len(valid)),train_size=40,stratify=valid.target,random_state=2026)[0]]
    def prep(f):
        from PIL import Image
        trans=weights.transforms()
        return torch.stack([trans(Image.fromarray((row.reshape(8,8)/16*255).astype('uint8')).convert('RGB')) for row in f[FEATURES].to_numpy()])
    X=prep(train);V=prep(valid)
    for p in model.parameters():p.requires_grad=False
    model.fc=nn.Linear(model.fc.in_features,10)
    if fine_tune:
        for p in model.layer4.parameters():p.requires_grad=True
    model.backbone_frozen=not fine_tune
    # 1 epoch valide le chemin technique ; aucune conclusion statistique sur 40 images.
    trained,hist,prob,seconds=train_loop(model,X.numpy(),train.target.to_numpy(),V.numpy(),valid.target.to_numpy(),epochs=1,lr=.001,batch_size=8)
    return {'scores':evaluate(valid.target,prob),'seconds':seconds,'history':hist.to_dict(orient='records'),'trainable':sum(p.numel() for p in trained.parameters() if p.requires_grad),'n_train':len(train),'n_valid':len(valid)}

"""BERT-tiny sur la vraie compétition Disaster Tweets, même protocole que TF-IDF."""
import time
import numpy as np
from .competition import subsets,save_result
from .core import ROOT
from .deep import setup,load_text_model

def run_text(root=ROOT,limit=1000,mode='frozen',epochs=2,allow_download=False):
    torch=setup();tokenizer,model=load_text_model(allow_download)
    a,v,_,_,rec=subsets('tweets',root,2026,limit)
    device=torch.device('cuda' if torch.cuda.is_available() else 'cpu');model=model.to(device)
    start=time.perf_counter();history=[]
    def batches(frame,batch=16):
        for i in range(0,len(frame),batch):
            block=frame.iloc[i:i+batch]
            tokens={k:x.to(device) for k,x in tokenizer(block.text.fillna('').tolist(),padding=True,truncation=True,max_length=96,return_tensors='pt').items()}
            yield tokens,torch.tensor(block.target.to_numpy(),dtype=torch.long,device=device)
    if mode=='frozen':
        from sklearn.linear_model import LogisticRegression
        def embeddings(frame):
            model.eval();arr=[]
            with torch.no_grad():
                for batch,_ in batches(frame):
                    h=model.bert(**batch).last_hidden_state;mask=batch['attention_mask'].unsqueeze(-1)
                    arr.append(((h*mask).sum(1)/mask.sum(1)).cpu().numpy())
            return np.concatenate(arr)
        X=embeddings(a);V=embeddings(v);head=LogisticRegression(max_iter=500).fit(X,a.target);p=head.predict_proba(V)[:,1]
    elif mode=='finetune':
        optim=torch.optim.AdamW(model.parameters(),lr=3e-5)
        for epoch in range(epochs):
            model.train();losses=[]
            for batch,y in batches(a):
                optim.zero_grad(set_to_none=True);loss=model(**batch,labels=y).loss;loss.backward();optim.step();losses.append(loss.item())
            history.append({'epoch':epoch+1,'train_loss':float(np.mean(losses))})
        model.eval();arr=[]
        with torch.no_grad():
            for batch,_ in batches(v):arr.append(model(**batch).logits.softmax(1)[:,1].cpu().numpy())
        p=np.concatenate(arr)
    else:raise ValueError('mode frozen ou finetune')
    config={'key':'tweets','model':mode,'params':{'checkpoint':'prajjwal1/bert-tiny','revision':getattr(model.config,'_commit_hash',None),'epochs':epochs,'max_length':96},'seed':2026,'limit':limit,'threshold':.5,'hypothesis':'Comparer la représentation préentraînée à TF-IDF sur les mêmes observations.'}
    out,scores=save_result('tweets',a,v,rec,p,config,time.perf_counter()-start,root)
    return out,scores,history

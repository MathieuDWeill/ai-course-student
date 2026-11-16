"""Dogs vs. Cats Redux : vrais fichiers JPEG, entraînement et inférence par batch."""
from pathlib import Path
import time,uuid,json
import numpy as np,pandas as pd
from sklearn.model_selection import train_test_split
from .core import ROOT,write_json,digest,source_hash
from .competition import get_folder,SPECS,binary_scores
from .deep import setup

def image_protocol(root=ROOT,limit=120):
    folder=get_folder('catsdogs',root)
    rows=[]
    for label,prefix in [(0,'cat'),(1,'dog')]:
        for p in sorted((folder/'train').glob(prefix+'.*.jpg')):rows.append({'path':str(p),'image_id':p.name,'target':label})
    if len(rows)<20:raise FileNotFoundError(f'Extraire train.zip dans {folder}/train et test.zip dans {folder}/test. Aucune image officielle fournie dans ce kit.')
    frame=pd.DataFrame(rows)
    i,j=train_test_split(np.arange(len(frame)),test_size=.2,stratify=frame.target,random_state=2026)
    if limit and len(i)>limit:i=train_test_split(i,train_size=limit,stratify=frame.iloc[i].target,random_state=2026)[0]
    if limit and len(j)>max(20,limit//3):j=train_test_split(j,train_size=max(20,limit//3),stratify=frame.iloc[j].target,random_state=2026)[0]
    return frame.iloc[i].copy(),frame.iloc[j].copy()

def run_images(root=ROOT,limit=120,epochs=1,mode='head',augment=False,allow_download=False):
    torch=setup();from torch import nn
    from torch.utils.data import DataLoader,Dataset
    from torchvision.models import resnet18,ResNet18_Weights
    from torchvision import transforms
    from PIL import Image
    a,v=image_protocol(root,limit);weights=ResNet18_Weights.DEFAULT
    cache=Path(torch.hub.get_dir())/'checkpoints'/Path(weights.url).name
    if not cache.exists() and not allow_download:raise FileNotFoundError('Poids ResNet18 absents : préparer les assets')
    transform=weights.transforms()
    train_transform=transforms.Compose([transforms.RandomHorizontalFlip(),transform]) if augment else transform
    class Images(Dataset):
        def __init__(self,frame,trans):self.frame=frame.reset_index(drop=True);self.trans=trans
        def __len__(self):return len(self.frame)
        def __getitem__(self,i):
            row=self.frame.iloc[i]
            with Image.open(row.path) as image:x=self.trans(image.convert('RGB'))
            return x,int(row.target)
    tr=DataLoader(Images(a,train_transform),batch_size=8,shuffle=True,num_workers=0,generator=torch.Generator().manual_seed(2026));va=DataLoader(Images(v,transform),batch_size=8,shuffle=False,num_workers=0)
    model=resnet18(weights=weights)
    for p in model.parameters():p.requires_grad=False
    model.fc=nn.Linear(model.fc.in_features,2)
    if mode=='partial':
        for p in model.layer4.parameters():p.requires_grad=True
    elif mode!='head':raise ValueError('mode head ou partial')
    device=torch.device('cuda' if torch.cuda.is_available() else 'cpu');model=model.to(device)
    optimizer=torch.optim.AdamW([p for p in model.parameters() if p.requires_grad],lr=.0003)
    loss_fn=nn.CrossEntropyLoss();history=[];start=time.perf_counter()
    for epoch in range(epochs):
        model.train()
        if mode=='head':
            for child in list(model.children())[:-1]:child.eval()
        losses=[]
        for x,y in tr:
            x=x.to(device);y=y.to(device);optimizer.zero_grad(set_to_none=True);loss=loss_fn(model(x),y);loss.backward();optimizer.step();losses.append(loss.item())
        model.eval();proba=[]
        with torch.no_grad():
            for x,y in va:proba.extend(model(x.to(device)).softmax(1)[:,1].cpu().tolist())
        scores=binary_scores(v.target.to_numpy(),np.array(proba));history.append({'epoch':epoch+1,'train_loss':float(np.mean(losses)),'valid_log_loss':scores['log_loss']})
    out=Path(root)/'runs'/('catsdogs_'+uuid.uuid4().hex[:12]);out.mkdir(parents=True)
    predictions=pd.DataFrame({'image_id':v.image_id.to_numpy(),'target':v.target.to_numpy(),'probability_dog':proba});predictions.to_csv(out/'predictions.csv',index=False)
    cfg={'mode':mode,'augment_train_only':augment,'limit':limit,'epochs':epochs,'seed':2026,'weights':str(weights),'transform':str(transform)}
    write_json(out/'config.json',cfg);write_json(out/'metrics.json',{**scores,'seconds':time.perf_counter()-start})
    # Poids seulement ; ne jamais charger un objet Python arbitraire remis par un tiers.
    torch.save({k:x.detach().cpu() for k,x in model.state_dict().items()},out/'weights.pt')
    write_json(out/'manifest.json',{'competition':SPECS['catsdogs'],'source_sha256':source_hash(),'n_train':len(a),'n_valid':len(v),'trainable':sum(p.numel() for p in model.parameters() if p.requires_grad),'device':str(device),'images_sha256':{p.name:digest(p) for p in [Path(x) for x in pd.concat([a,v]).path]},'schema':3,'key':'catsdogs','files':{name:digest(out/name) for name in ['config.json','metrics.json','predictions.csv']},'warning':'Split stratifié par fichier ; auditer doublons et provenance. Un run court ne prouve pas un meilleur modèle.'})
    return out,scores,pd.DataFrame(history)

def submit_images(run_folder,root=ROOT):
    torch=setup();from torch import nn
    from torch.utils.data import Dataset,DataLoader
    from torchvision.models import resnet18,ResNet18_Weights
    from PIL import Image
    run_folder=Path(run_folder);folder=get_folder('catsdogs',root)
    sample=pd.read_csv(folder/'sample_submission.csv')
    if list(sample)!=['id','label']:raise ValueError('Sample submission id,label requise')
    model=resnet18(weights=None);model.fc=nn.Linear(model.fc.in_features,2)
    model.load_state_dict(torch.load(run_folder/'weights.pt',weights_only=True,map_location='cpu'));model.eval()
    trans=ResNet18_Weights.DEFAULT.transforms()
    class TestImages(Dataset):
        def __len__(self):return len(sample)
        def __getitem__(self,i):
            image_id=int(sample.iloc[i]['id']);p=folder/'test'/f'{image_id}.jpg'
            with Image.open(p) as image:return trans(image.convert('RGB'))
    probabilities=[]
    with torch.no_grad():
        for x in DataLoader(TestImages(),batch_size=8,num_workers=0):probabilities.extend(model(x).softmax(1)[:,1].tolist())
    dest=Path(root)/'runs'/('submission_catsdogs_'+uuid.uuid4().hex[:8]);dest.mkdir(parents=True)
    sample['label']=probabilities;sample.to_csv(dest/'submission.csv',index=False)
    return dest

def import_image_result(archive,root=ROOT):
    import zipfile,io,hashlib
    required={'manifest.json','config.json','metrics.json','predictions.csv'}
    with zipfile.ZipFile(archive) as z:
        if set(z.namelist())!=required or len(z.namelist())!=4 or any(i.file_size>20_000_000 for i in z.infolist()):raise ValueError('Archive image hors contrat')
        blobs={n:z.read(n) for n in required}
    manifest=json.loads(blobs['manifest.json']);cfg=json.loads(blobs['config.json'])
    for name in ['config.json','metrics.json','predictions.csv']:
        if hashlib.sha256(blobs[name]).hexdigest()!=manifest['files'][name]:raise ValueError('Fichier image modifié')
    a,v=image_protocol(root,cfg['limit'])
    for p in [Path(x) for x in pd.concat([a,v]).path]:
        if digest(p)!=manifest['images_sha256'].get(p.name):raise ValueError('Image différente')
    pred=pd.read_csv(io.BytesIO(blobs['predictions.csv']))
    if list(pred)!=['image_id','target','probability_dog'] or not np.array_equal(pred.image_id,v.image_id) or not np.array_equal(pred.target,v.target):raise ValueError('Validation image incompatible')
    scores=binary_scores(pred.target.to_numpy(),pred.probability_dog.to_numpy());reported=json.loads(blobs['metrics.json'])
    if any(not np.isclose(scores[k],reported[k],atol=1e-9) for k in scores):raise ValueError('Métrique image incohérente')
    dest=Path(root)/'runs'/('import_image_'+uuid.uuid4().hex[:12]);dest.mkdir(parents=True)
    for n,b in blobs.items():(dest/n).write_bytes(b)
    return dest

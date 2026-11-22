"""Détection et segmentation préentraînées, puis fusion tardive texte/image."""
from pathlib import Path
import argparse,json

def analyze(image_path,output_dir='runs/vision'):
    import torch,numpy as np
    from PIL import Image
    from torchvision.models.detection import ssdlite320_mobilenet_v3_large,SSDLite320_MobileNet_V3_Large_Weights
    from torchvision.models.segmentation import lraspp_mobilenet_v3_large,LRASPP_MobileNet_V3_Large_Weights
    torch.set_num_threads(2);out=Path(output_dir);out.mkdir(parents=True,exist_ok=True)
    image=Image.open(image_path).convert('RGB')
    # Diminuer la résolution borne la mémoire du segmentateur.
    image.thumbnail((640,640))
    dw=SSDLite320_MobileNet_V3_Large_Weights.DEFAULT
    detector=ssdlite320_mobilenet_v3_large(weights=dw).eval()
    with torch.inference_mode(): d=detector([dw.transforms()(image)])[0]
    keep=d['scores']>=.5
    detections=[{'label':dw.meta['categories'][int(l)],'score':round(float(s),4),'box':[round(float(v),2) for v in b]}
                for b,l,s in zip(d['boxes'][keep],d['labels'][keep],d['scores'][keep])]
    sw=LRASPP_MobileNet_V3_Large_Weights.DEFAULT
    segmenter=lraspp_mobilenet_v3_large(weights=sw).eval()
    with torch.inference_mode(): mask=segmenter(sw.transforms()(image).unsqueeze(0))['out'][0].argmax(0).cpu().numpy()
    Image.fromarray(mask.astype('uint8')).save(out/'mask.png')
    classes=[sw.meta['categories'][int(i)] for i in np.unique(mask)]
    report={'detections':detections,'segmentation_classes':classes,'mask_shape':list(mask.shape),
            'detector_weights':str(dw),'segmenter_weights':str(sw),'image':Path(image_path).name,
            'limit':'Inférences sans annotation de référence : aucune mesure de mAP ou IoU réelle.'}
    (out/'report.json').write_text(json.dumps(report,indent=2))
    # Illustration du résultat réel : boîtes et masque, pas une vérité terrain.
    from PIL import ImageDraw
    overlay=image.copy();draw=ImageDraw.Draw(overlay)
    for row in detections:draw.rectangle(row['box'],outline='red',width=3);draw.text(row['box'][:2],row['label'],fill='red')
    overlay.save(out/'detections.png')
    return report

def retrieve(query,report):
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    # Petit catalogue rédigé pour le cours, non extrait des prédictions.
    catalog=[('dog','dog animal pet chien animal domestique'),('cat','cat animal pet chat animal domestique'),
             ('transport','bus car vehicle voiture transport'),('sport','ball sports sport ballon')]
    labels=' '.join(x['label'] for x in report['detections'])
    v=TfidfVectorizer();matrix=v.fit_transform([query+' '+labels]+[x[1] for x in catalog])
    scores=cosine_similarity(matrix[0],matrix[1:])[0]
    return {'query':query,'image_labels':labels,'ranking':sorted(zip([x[0] for x in catalog],scores.tolist()),key=lambda x:-x[1]),
            'fusion':'Fusion tardive de labels visuels prédits et de texte ; aucun espace joint appris.'}
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('image');p.add_argument('--download-and-run',action='store_true');p.add_argument('--query',default='animal domestique');a=p.parse_args()
    if not a.download_and_run:p.error('Confirmer le téléchargement des poids avec --download-and-run')
    r=analyze(a.image);print(json.dumps({'vision':r,'application':retrieve(a.query,r)},ensure_ascii=False,indent=2))

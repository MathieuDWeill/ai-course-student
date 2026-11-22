from pathlib import Path
import tempfile,time
import streamlit as st
from vision import analyze,retrieve
st.title('Recherche texte et image')
st.write('Fusion tardive pédagogique : labels visuels prédits et recherche textuelle. Les poids peuvent être téléchargés au premier calcul.')
upload=st.file_uploader('Image autorisée',type=['jpg','jpeg','png'])
query=st.text_input('Votre recherche','animal domestique')
if st.button('Analyser'):
    if upload is None: st.warning('Choisir une image avant de lancer.')
    else:
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'input.jpg';path.write_bytes(upload.getvalue());start=time.perf_counter()
            with st.spinner('Analyse locale en cours…'):report=analyze(path,Path(tmp)/'results')
            st.image(str(Path(tmp)/'results/detections.png'),caption='Détections prédites, sans vérité terrain')
            st.json(report)
            for label,q,r in [('Texte seul',query,{'detections':[]}),('Image seule','',report),('Combinaison',query,report)]:
                st.subheader(label);st.json(retrieve(q,r)['ranking'])
            st.write('Durée totale, chargement compris :',round(time.perf_counter()-start,2),'s')
            st.info('Un classement ne prouve pas que la demande est satisfaite. Vérifier les labels et les contradictions.')

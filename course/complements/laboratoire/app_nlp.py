import re
import streamlit as st
from generative import extractive_summary,generate
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
st.title('Résumé et assistant documentaire')
text=st.text_area('Document autorisé','Le match commence à 18 h. La billetterie ouvre à 16 h. Aucun report annoncé.')
question=st.text_input('Question sur le document','Quand ouvre la billetterie ?')
use_gpt=st.checkbox('Exécuter aussi DistilGPT2 (poids à télécharger, texte anglais recommandé)',value=False)
if st.button('Analyser'):
    if not text.strip():st.warning('Saisir un document.')
    else:
        st.subheader('Résumé de référence : première phrase')
        st.write(extractive_summary(text))
        docs=[x.strip() for x in re.split(r'(?<=[.!?])\s+',text.strip()) if x.strip()]
        if question.strip():
            try:
                v=TfidfVectorizer();m=v.fit_transform(docs+[question]);scores=cosine_similarity(m[-1],m[:-1])[0]
                idx=int(scores.argmax());st.subheader('Passage retrouvé')
                if scores[idx]==0:st.write('Aucun recouvrement lexical ; je ne dispose pas de passage pertinent.')
                else:st.write(docs[idx]);st.caption('Proximité lexicale : vérifier que ce passage répond vraiment à la question.')
            except ValueError:st.warning('Texte trop court ou vocabulaire vide pour cette représentation.')
        if use_gpt:
            if len(text)>1200:st.warning('Réduire le texte à 1 200 caractères pour cet atelier.')
            else:
                with st.spinner('Chargement et génération locale…'):result=generate(text+'\nSummary:',40)
                st.subheader('Continuation réelle du modèle')
                st.code(repr(result['completion']));st.json({k:v for k,v in result.items() if k!='completion'})
        st.info('Auditer faits conservés, ajoutés et omis. La référence première phrase peut manquer l’essentiel ; une continuation plausible peut être fausse.')

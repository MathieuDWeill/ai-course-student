# NLP_C1 — GPT, résumé et assistant documentaire

Conception pédagogique : Mathieu Weill.

## Question et progression

Comment générer du texte tout en vérifiant ce qu’il affirme ?

À placer après NLP_02. Durée indicative : 75 minutes, à adapter aux acquis.

Preuve attendue : Comparer une référence extractive et une génération réelle ; auditer les faits, omissions et refus.

## BERT et GPT ne font pas le même calcul

Un encodeur de type BERT représente le contexte. Un modèle de type GPT prédit le prochain token à partir des tokens précédents.

Un token est une unité de texte déterminée par le tokenizer ; ce n’est pas toujours un mot. BERT et GPT utilisent des transformers, mais l’objectif et le masque changent. GPT désigne ici la famille des transformers génératifs préentraînés ; notre démonstration locale utilise DistilGPT2, issu de GPT-2. Ce modèle anglophone n’est pas un assistant entraîné à suivre nos consignes.

Question de vérification : Prédire le prochain token est-il la même chose que vérifier un fait ?

## Le résumé a une référence simple

Une référence extractive recopie une partie du texte. Un résumé génératif peut reformuler et peut aussi ajouter un fait absent.

Nous commencerons par prendre la première phrase. C’est une référence très limitée mais reproductible, sans apprentissage. Nous comparerons ensuite une génération. Notre grille regarde les faits conservés, les faits ajoutés, les omissions et la longueur. ROUGE peut mesurer du recouvrement lexical ; il ne garantit pas la fidélité factuelle. Une faible génération n’est pas remplacée par une sortie inventée.

Question de vérification : Un résumé fluide mais qui change une date est-il réussi ?

## Un assistant doit annoncer ses limites

Question → recherche dans des documents → éléments trouvés → réponse ou abstention. La présence de documents ne garantit pas une réponse fondée.

Notre petit assistant de référence retrouve une phrase avec TF-IDF et la cite. Il ne génère pas une conversation libre. Nous pouvons ensuite donner le passage à un modèle génératif, avec une consigne d’abstention, mais cette consigne ne prouve pas qu’il s’abstiendra. Il faut vérifier des questions répondables, absentes et ambiguës. Le texte utilisateur ou documentaire peut contenir des instructions malveillantes ; il doit rester une donnée, sans accès à des outils sensibles.

Question de vérification : Que faire si aucun passage ne répond à la question ?

## Le protocole de génération

Consigner modèle et révision, prompt, tokenizer, longueur maximale et décodage. Tester sur des documents réservés et mesurer aussi latence et coût.

Les poids sont téléchargés uniquement à la demande. La génération gloutonne choisit le token de plus forte probabilité à chaque étape ; elle peut répéter et reste dépendante du modèle. Pour les exercices en français, choisir ensuite un modèle compatible avec cette langue et cet usage, avec sa licence et ses exigences matérielles. Un petit GPT-2 sert ici à comprendre les limites, pas à simuler un assistant commercial.

Question de vérification : Une température plus faible garantit-elle des réponses vraies ?

## NLP_C1-D1 — Auditer un résumé fabriqué

Prévoir une sortie, exécuter, puis expliquer une assertion.

```python
source='Le match commence à 18 h. La billetterie ouvre à 16 h. Aucun report annoncé.'
candidate='Le match commence à 20 h après un report.'
checks={'heure_correcte':'18 h' in candidate,
        'report_invente':'après un report' in candidate}
print(checks)
assert not checks['heure_correcte'] and checks['report_invente']
# Ces contrôles de chaînes illustrent deux erreurs connues, pas un juge automatique.
```

## NLP_C1-D2 — Assistant extractif de référence

Prévoir une sortie, exécuter, puis expliquer une assertion.

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
docs=['La billetterie ouvre à seize heures.',
      'Le match commence à dix-huit heures.',
      'Les billets ne sont pas remboursables.']
question='Quand ouvre la billetterie ?'
v=TfidfVectorizer();m=v.fit_transform(docs+[question])
scores=cosine_similarity(m[-1],m[:-1])[0]
idx=int(scores.argmax())
print('Passage cité :',docs[idx])
assert idx==0
print('Limite : ce score ne prouve pas que la question a une réponse.')
```

## Application locale de résumé et questions-réponses

Dans `laboratoire`, installer Streamlit puis lancer :

```bash
python -m pip install "streamlit>=1.40,<2"
python -m streamlit run app_nlp.py
```

Ouvrir l’adresse locale affichée. Saisir un document et une question ; comparer le résumé première phrase et le passage retrouvé. La case DistilGPT2 ajoute une vraie génération locale, avec téléchargement initial des poids. Examiner aussi une question absente du document : un score lexical positif ne prouve pas que le passage répond. Cette application fournit une référence observable, pas un assistant génératif fiable.

## Génération réelle avec un modèle GPT-2 distillé

Dans le dossier `laboratoire`, après installation de `requirements-ia.txt` :

```bash
python generative.py --download-and-run
```

Le premier lancement télécharge des poids de plusieurs centaines de Mo. Il faut une connexion et de l’espace disque. DistilGPT2 est anglophone et non instruction-tuned : sa continuation peut répéter ou inventer. Conserver la sortie réelle, même médiocre. Comparer au résumé de référence « première phrase » sur trois textes anglais courts et réservés. Noter les faits conservés, ajoutés et omis, ainsi que le modèle et sa révision. Aucun score de qualité n’est préannoncé.

Faire varier le prompt avec une seule modification à la fois. Une limite de tokens borne la sortie ; elle ne garantit pas une longueur exacte en mots. Si les poids sont indisponibles, poursuivre les calculs et la grille d’audit, mais noter « inférence préentraînée non réalisée ». Ne pas la remplacer par une sortie fabriquée.

## Sorties résolues et limites

Notre génération réelle sur « The match was cancelled because of heavy rain. Summary: » produit seulement des retours à la ligne. C’est un échec de résumé, que nous conservons comme tel. Sur « Artificial intelligence can help scientists », elle prolonge par « to better understand the world around them. », puis répète des retours à la ligne. Cela montre une continuation de texte et ne prouve aucune qualité d’assistant. Le modèle GPT-2 distillé n’est pas instruction-tuned.

## NLP_C1-E — Exercice individuel

Un assistant cite un document correct mais sa réponse affirme le contraire. Proposer une grille de quatre critères et un cas où il doit s’abstenir.

Écrire une réponse justifiée avant la correction collective.

## Bilan

Comparer une référence extractive et une génération réelle ; auditer les faits, omissions et refus.

Une sortie expliquée : …

Une limite : …

Une prochaine vérification : …

## Références

- https://huggingface.co/distilbert/distilgpt2
- https://huggingface.co/docs/transformers/main/en/main_classes/text_generation

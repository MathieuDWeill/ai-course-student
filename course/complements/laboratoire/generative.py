"""Génération réelle, option explicite nécessitant un téléchargement de poids."""
import argparse,json

def generate(prompt,max_new_tokens=40):
    from transformers import AutoTokenizer,AutoModelForCausalLM
    import torch
    torch.set_num_threads(2)
    name='distilbert/distilgpt2'
    revision='2290a62682d06624634c1f46a6ad5be0f47f38aa'
    tokenizer=AutoTokenizer.from_pretrained(name,revision=revision)
    model=AutoModelForCausalLM.from_pretrained(name,revision=revision,use_safetensors=True).eval()
    inputs=tokenizer(prompt,return_tensors='pt')
    if inputs['input_ids'].shape[1]+max_new_tokens>model.config.n_positions:
        raise ValueError('Contexte trop long pour ce modèle.')
    with torch.inference_mode():
        ids=model.generate(**inputs,max_new_tokens=max_new_tokens,do_sample=False,pad_token_id=tokenizer.eos_token_id)
    return {'model':name,'revision':revision,
            'prompt':prompt,'completion':tokenizer.decode(ids[0,inputs['input_ids'].shape[1]:],skip_special_tokens=True),
            'limit':'Modèle GPT-2 distillé anglophone, non entraîné à suivre des instructions. Pas un assistant fiable.'}

def extractive_summary(text):
    import re
    sentences=[s.strip() for s in re.split(r'(?<=[.!?])\s+',text.strip()) if s.strip()]
    if not sentences: raise ValueError('Texte vide')
    # Référence simple annoncée : première phrase, sans apprentissage.
    return sentences[0]
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--download-and-run',action='store_true');a=p.parse_args()
    if not a.download_and_run:p.error('Confirmer le téléchargement des poids avec --download-and-run')
    print(json.dumps(generate('The match was cancelled because of heavy rain. Summary:'),ensure_ascii=False,indent=2))

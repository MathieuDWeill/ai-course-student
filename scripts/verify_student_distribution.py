"""Check the catalog and common teacher-only leaks; never certifies visible lesson content."""
from pathlib import Path
import json,re,sys,zipfile,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
def check(root):
 errors=[];catalog=json.loads((root/'course/catalogue.json').read_text());sessions=catalog['sessions'];seen=set()
 for s in sessions:
  if s['id'] in seen:errors.append('Duplicate session: '+s['id'])
  seen.add(s['id'])
  for key in ['notebook','powerpoint_complementaire','pdf_projection','cours_redige','demarrage']:
   value=s.get(key)
   if value and not (root/value).is_file():errors.append('Missing resource: '+value)
  if not (root/'course/seances'/f"{s['id']}.md").is_file():errors.append('Missing session card: '+s['id'])
  if s.get('supports_complets') and not all(s.get(k) for k in ['notebook','powerpoint_complementaire','pdf_projection']):errors.append('Incomplete session marked complete: '+s['id'])
  if s.get('notes_professeur_autorisees') or s.get('corriges_exercices_autorises'):errors.append('Teacher material authorized in student catalog: '+s['id'])
 for f in (root/'slides').glob('*.pptx'):
  with zipfile.ZipFile(f) as z:
   if z.testzip():errors.append('Invalid ZIP: '+f.name)
   for name in z.namelist():
    if re.match(r'ppt/(notesSlides|notesMasters|comments|persons)/|ppt/commentAuthors',name):errors.append('Private PowerPoint part: '+f.name+'/'+name)
    if name.endswith('.rels'):
     for rel in ET.fromstring(z.read(name)):
      typ=rel.attrib.get('Type','').lower()
      if any(t in typ for t in ['notesslide','notesmaster','comment','person']):errors.append('Private PowerPoint relationship: '+f.name)
 # The public repo must not regain files explicitly named as exercise corrections.
 for f in root.rglob('*'):
  if '.git' in f.parts or not f.is_file():continue
  if re.match(r'(?:CORRECTION_|.*_corrig[eé](?:\.|_))',f.name,re.I):errors.append('Correction file in student tree: '+str(f.relative_to(root)))
 for folder in [root/'teacher',root/'teaching']:
  if folder.exists():errors.append('Teacher directory in student tree: '+folder.name)
 for f in [root/'README.md',root/'course/README.md',*list((root/'course').glob('*.md')),*list((root/'course/seances').glob('*.md'))]:
  for target in re.findall(r'\]\(([^)]+)\)',f.read_text()):
   if re.match(r'[a-z]+://|#',target):continue
   local=target.split('#')[0].split('?')[0]
   if not (f.parent/local).exists():errors.append('Broken link: '+str(f.relative_to(root))+' -> '+target)
 return errors
if __name__=='__main__':
 errors=check(ROOT)
 if errors:
  print('\n'.join(errors));sys.exit(1)
 print('PASS: catalog resources, local navigation and PowerPoint privacy checks.')
 print('Visible exercise answers and PDF content still require editorial review.')

import json
from pathlib import Path
import shutil
import tempfile
import unittest
import zipfile
from verify_student_distribution import check
SOURCE=Path(__file__).resolve().parents[1]
class DistributionTests(unittest.TestCase):
 def setUp(self):
  self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup);self.root=Path(self.temp.name)/'repo';shutil.copytree(SOURCE,self.root,ignore=shutil.ignore_patterns('.git','__pycache__'))
 def test_clean_distribution(self):self.assertEqual(check(self.root),[])
 def test_hidden_speaker_note_is_rejected(self):
  slide=next((self.root/'slides').glob('*.pptx'))
  with zipfile.ZipFile(slide,'a') as z:z.writestr('ppt/notesSlides/notesSlide999.xml','private note')
  self.assertTrue(any('Private PowerPoint part' in e for e in check(self.root)))
 def test_exercise_correction_is_rejected(self):
  (self.root/'CORRECTION_EXERCICE.md').write_text('private correction')
  self.assertTrue(any('Correction file' in e for e in check(self.root)))
 def test_missing_catalog_resource_is_rejected(self):
  f=self.root/'course/catalogue.json';c=json.loads(f.read_text());c['sessions'][0]['notebook']='missing.ipynb';f.write_text(json.dumps(c))
  self.assertTrue(any('Missing resource' in e for e in check(self.root)))
 def test_teacher_notebook_metadata_is_rejected(self):
  f=self.root/'course/chapitres/PY_01/notebook.ipynb';n=json.loads(f.read_text());n['metadata']['audience']='teacher';f.write_text(json.dumps(n))
  self.assertTrue(any('Teacher notebook metadata' in e for e in check(self.root)))
 def test_executed_student_output_is_rejected(self):
  f=self.root/'course/chapitres/PY_01/notebook.ipynb';n=json.loads(f.read_text());c=next(c for c in n['cells'] if c['cell_type']=='code');c['outputs']=[{'output_type':'stream','name':'stdout','text':['private output']}];f.write_text(json.dumps(n))
  self.assertTrue(any('Executed outputs' in e for e in check(self.root)))
 def test_supplement_speaker_notes_are_rejected(self):
  slide=self.root/'course/complements/AML_C2/presentation.pptx'
  with zipfile.ZipFile(slide,'a') as z:z.writestr('ppt/notesSlides/notesSlide999.xml','private note')
  self.assertTrue(any('Private PowerPoint part' in e for e in check(self.root)))
 def test_supplement_teacher_metadata_is_rejected(self):
  f=self.root/'course/complements/NLP_C1/notebook.ipynb';n=json.loads(f.read_text());n['metadata']['audience']='teacher';f.write_text(json.dumps(n))
  self.assertTrue(any('Teacher notebook metadata' in e for e in check(self.root)))
if __name__=='__main__':unittest.main()

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
if __name__=='__main__':unittest.main()

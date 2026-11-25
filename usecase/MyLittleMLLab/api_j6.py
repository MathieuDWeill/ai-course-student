"""Démonstration locale J6 : python -m uvicorn api_j6:app --host 127.0.0.1 --port 8006."""
from pathlib import Path
import os
from mllab.delivery_j56 import create_app
ROOT=Path(__file__).resolve().parent
FOLDER=Path(os.environ.get('MLLAB_J6_RELEASE',str(ROOT/'runs/J6/release')))
app=create_app(FOLDER)

# config.py
from dotenv import load_dotenv
import os

load_dotenv()

CODE_PATH = os.getenv('CODE_PATH')
TCGA_PATH = os.getenv('TCGA_PATH')
RAW_THYROID_PATH = os.getenv('RAW_THYROID_PATH')
THYROID_PATH = os.getenv('THYROID_PATH')

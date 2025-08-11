import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TMP_DIR = os.path.join(BASE_DIR, 'resources')

UPLOADED_FILE = os.path.join(TMP_DIR, 'file.txt')
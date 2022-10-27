import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
TELEGRAM_CONFIG_PATH = os.path.join(BASE_DIR, "tg_config.ini")
STATIC_DIR = os.path.join(BASE_DIR, 'main', 'static')
PROFILE_IMG_DIR = os.path.join(STATIC_DIR, 'images', "candidates")
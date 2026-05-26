import os
from dotenv import load_dotenv

load_dotenv()  # Carga variables desde .env

APP_NAME = os.getenv("APP_NAME", "Sistema Desconocido")
APP_VERSION = os.getenv("APP_VERSION", "0.0")
ADMIN_USER = os.getenv("ADMIN_USER", "admin")
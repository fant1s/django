import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG")
DATABASE_URL = os.getenv("DATABASE_URL")

INSTALLED_APPS = [
    "homepage",
    "catalog",
    "about",
]

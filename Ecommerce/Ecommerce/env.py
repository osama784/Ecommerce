from functools import lru_cache
from pathlib import Path
from decouple import config as decouple_config, Config, RepositoryEnv
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_DIR = BASE_DIR.parent
ENV_FILE_PATH = '.env'

@lru_cache
def get_config():
    if ENV_FILE_PATH:
        return Config((RepositoryEnv(str(ENV_FILE_PATH))))
    return decouple_config


config = get_config()
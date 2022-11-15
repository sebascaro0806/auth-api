import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

class AppSettings:
    
    #Api settings
    PROJECT_NAME = "ISA_2 - API Authentication"
    PROJECT_VERSION = "0.0.1"
    PROJECT_DESCRIPTION = "API para manejar authenticacion del usuario y generacion del token"
    URL_PREFIX="/authentication/api/v1"

    #Auth settings
    PROJECT_SECRET_KEY= os.getenv('SECRET_KEY')
    PROJECT_PROJECT_ALGORITHM= os.getenv('ALGORITHM')
    PROJECT_ACCESS_TOKEN_EXPIRE_MINUTES= int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES'))
    
    #Database settings
    DB_HOST=os.getenv('DB_HOST')
    DB_USER=os.getenv('DB_USER')
    DB_USER_PASSWORD=os.getenv('DB_USER_PASSWORD')
    DB=os.getenv('DB')

settings = AppSettings()
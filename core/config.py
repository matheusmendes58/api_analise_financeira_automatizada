# All settings in project is here example passwords, string connections, etc

import os
from dotenv import load_dotenv

load_dotenv()

class AllSettings:
    """
    General settings from application

    """

    def __init__(self):
        #API

        self.api_v1_str = '/analise/rpa'

        #Db

        self.user_db = os.getenv('USER_DB')
        self.pwd_db = os.getenv('PWD_DB')
        self.host_db = os.getenv('HOST_DB')
        self.db = os.getenv('DB')
        self.connect_db = f'mysql+pymysql://{self.user_db}:{self.pwd_db}@{self.host_db}/{self.db}'

        #AI

        self.hugginface_api_url = 'https://api-inference.huggingface.co/models/google/flan-t5-large'
        self.hugginface_token = os.getenv('HUGGINFACE_TOKEN')
        self.cohere_token = os.getenv('COHERE_TOKEN')
        self.google_token = os.getenv('GOOGLE_TOKEN')

        #Xlsx file
        #choose a number that will read lines from the file, remembering that as this is a beta version,
        # the ideal is to leave 20 lines for reading to avoid errors.

        self.lines_for_read = 20

settings = AllSettings()

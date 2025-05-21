# All settings in project is here example passwords, string connections, etc

class AllSettings:
    """
    General settings from application

    """

    def __init__(self):
        #API

        self.api_v1_str = '/analise/rpa'

        #Db

        self.user_db = 'root'
        self.pwd_db = '12345'
        self.host_db = 'localhost'
        self.db = 'api_analise_financeira_automatizada'
        self.connect_db = f'mysql+pymysql://{self.user_db}:{self.pwd_db}@{self.host_db}/{self.db}'

        #AI

        self.hugginface_api_url = 'https://api-inference.huggingface.co/models/google/flan-t5-large'
        self.hugginface_token = ''

        #Xlsx file
        #choose a number that will read lines from the file, remembering that as this is a beta version,
        # the ideal is to leave 20 lines for reading to avoid errors.

        self.lines_for_read = 20

settings = AllSettings()

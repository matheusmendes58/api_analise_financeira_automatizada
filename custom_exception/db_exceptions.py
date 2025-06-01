# DB exception handling

class CredentialsErrorConnection(Exception):

    def __init__(self, msg_error: str = f'Database connection error check user, '
                                        f'password and database credentials'):
        super().__init__(msg_error)

class StringConnection(Exception):
    def __init__(self, msg_error: str = 'Error in database connection string'
                                        'Example: myysql+pymysql://root:xxxx@localhost/estudo_api_fastapi '
                                        '- mysql written wrong'):

        super().__init__(msg_error)

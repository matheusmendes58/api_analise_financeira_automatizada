#File exception handling

class ExtensionError(ValueError):

    def __init__(self, msg_error: str = f'Unsupported file extension'):
        super().__init__(msg_error)

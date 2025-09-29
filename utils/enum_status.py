# support enums status

from enum import Enum

class StatusDbEnum(Enum):
    """
    This class represents a state of the database.
    """

    ok_db = 'OK'
    error_db = 'ERROR'
    extension_file_name_ok = 'XLSX'
    extension_file_name_error = 'UNKNOWN'


class StatusApiEnum(Enum):
    """
    This class represents a state of the api.
    """

    status_ok_201 = '201'
    status_ok_200 = '200'
    status_error_422 = '422'
    status_error_400 = '404'

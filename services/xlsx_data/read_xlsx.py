# Reading and processing xlsx files

import io
from pathlib import Path
from core.config import settings
from pandas import DataFrame
import pandas as pd

class FileXlsx:
    """
    This class performs reading and processing of data from xlsx files
    """

    def __init__(self, file_name: str = None):
        self.lines = settings.lines_for_read
        self.file_name = file_name
        self.dataframe = None

    def extension_check(self) -> dict:
        """
        This function check extension file

        :return: A dict
        """

        extension = Path(self.file_name)

        if extension.suffix not in ['.xls', '.xlsx']:
            return {'file': f'Unsupported file extension {extension}'}

    def read_xlsx_file(self, file: bytes) -> 'DataFrame':

        """
        This function performs read xlsx file

        :return: a dataframe from the file
        """

        self.dataframe = pd.read_excel(io.BytesIO(file))

        return self.dataframe

    def convert_to_text(self, file: DataFrame) -> str:
        """
        This function convert file in readable text

        :param file: Dataframe pandas

        :return: A string text
        """

        lines = self.lines

        text = file.head(lines).to_string(index=False)

        return text

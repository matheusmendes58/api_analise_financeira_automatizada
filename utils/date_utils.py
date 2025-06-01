# support functions for date

from datetime import datetime
from pytz import timezone

class DatesUtil:


    @classmethod
    def cur_datetime(cls):
        """
        Collect the current time

        :return: Date from selected region
        """

        return datetime.now(tz=timezone('America/Sao_Paulo'))

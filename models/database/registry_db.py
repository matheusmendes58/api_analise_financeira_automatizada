# Table that allocates records used in AI

from models.database.base import BASE, DBSESSION
from utils.date_utils import DatesUtil
from sqlalchemy import VARCHAR, INTEGER, TEXT, DATETIME, Column, desc

class RegistryAI(BASE):

    """
    Table that reference registry AI in database
    """

    __tablename__ = 'registry_ia_error_or_success'

    _id = Column(INTEGER, primary_key=True, autoincrement=True)
    execution = Column(DATETIME)
    file_name = Column(VARCHAR(250))
    extension_file_name = Column(VARCHAR(100))
    url_ia = Column(TEXT)
    prompt_ia = Column(TEXT)
    status = Column(VARCHAR(100))
    status_api = Column(VARCHAR(200))
    error_api = Column(TEXT)
    ai_error = Column(TEXT)
    ai_text_success = Column(TEXT)


    @classmethod
    def insert_registry_ia(cls,
                           execution=DatesUtil.cur_datetime(),
                           file_name: str = None,
                           extension_file_name: str = None,
                           url_ia: str = None,
                           prompt_ia: str = None,
                           status: str = None,
                           status_api: str = None,
                           error_api: str = None,
                           ai_error: str = None,
                           ai_text_success: str = None
                           ) -> None:

        """
        Insert into in DB

        :param execution: Api execution date
        :param file_name: Name of file
        :param extension_file_name: Name extension file
        :param url_ia: Url of AI
        :param prompt_ia: Prompt used in AI
        :param status: Status of Api example - OK, Error, Etc
        :param status_api: Code status api example 200 OK , 404, Etc
        :param error_api: Internal error api description
        :param ai_error: Error AI description
        :param ai_text_success: text returned AI

        :return: None
        """

        try:
            DBSESSION.merge(
                RegistryAI(
                    execution=execution,
                    file_name=file_name,
                    extension_file_name=extension_file_name,
                    url_ia=url_ia,
                    prompt_ia=prompt_ia,
                    status=status,
                    status_api=status_api,
                    error_api=error_api,
                    ai_error=ai_error,
                    ai_text_success=ai_text_success

                )
            )
            DBSESSION.commit()
        except Exception as e:
            DBSESSION.rollback()
            raise e
        finally:
            DBSESSION.close()

    @classmethod
    def select_all_registry(cls) -> list:

        """
        Select all registry in database

        :return: A list of registry

        """

        try:
            return DBSESSION.query(RegistryAI).all()
        except Exception as e:
            raise e

    @classmethod
    def select_last_registry_in_table(cls) -> dict:
        """
        Select last registry in table

        :return: Return last record inserted in table

        """

        try:
            return DBSESSION.query(RegistryAI).order_by(desc(RegistryAI._id)).first()
        except Exception as e:
            raise e

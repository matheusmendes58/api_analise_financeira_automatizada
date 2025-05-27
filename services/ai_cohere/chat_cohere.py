# All about AI cohere

from cohere.client import Client

class AiCohereChat:

    def __init__(self, token: str = None):

        self.token = token
        self.cohere = Client(api_key=token)

    def chat_cohere(self, prompt: str) -> dict:
        """
        This function call chat in AI from cohere

        :param prompt: PROMPT used from AI

        :return: Response of AI
        """

        response = self.cohere.chat(model='command',  message=prompt)

        return {'analise': response.text}

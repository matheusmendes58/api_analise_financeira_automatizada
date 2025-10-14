# All about google gemini

from google import genai

class AiGoogle:

    def __init__(self, api_token: str = None):

        self.client_google = genai.Client(api_key=api_token)

    def chat_ai_google(self, prompt: str) -> dict:
        """
        This function call chat in AI from Google

        :param prompt: PROMPT used from AI

        :return: Response of AI
        """

        response = self.client_google.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return {'analise': response.text}

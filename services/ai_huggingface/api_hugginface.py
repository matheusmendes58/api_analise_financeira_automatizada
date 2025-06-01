# All about api hugginface

import requests

class HuggingfaceIA:


    def __init__(self, huggingface_url: str = None, token: str = None):

        self.huggingface_url = huggingface_url
        self.token = token
        self.max_new_tokens = 250
        self.headers = {
            "Authorization": f"Bearer {self.token}"
        }


    def create_payload(self, prompt: str = None) -> dict:
        """
        Create payload for send api

        :param prompt: Text for AI

        :return: A dict with payload for api
        """

        payload = {
            "inputs": prompt,
            "parameters": {"max_new_tokens": self.max_new_tokens}
        }

        return payload

    def send_api_huggingface(self, payload: dict) -> dict:
        """
        Send request for api

        :param payload: Payload for api

        :return: A json
        """

        response = requests.post(self.huggingface_url, headers=self.headers, json=payload)

        if response.status_code == 200:
            result = response.json()[0]['generated_text']
            return {"analise": result}
        else:
            return {"error": "Falha ao consultar o modelo", "detalhes": response.text}

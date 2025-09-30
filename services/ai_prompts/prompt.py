# Prompt AI

class PromptIA:
    """
    This class is just about PROMPT AI
    """

    def __init__(self, data_text: str = None):

        self.data_text = data_text

        self.prompt_huggingface = f"""
        Você é um analista financeiro. Analise os dados abaixo e indique se há sinais de crise financeira,
        como prejuízos recorrentes, aumento de dívidas, queda de receita ou baixa liquidez.
        Dados financeiros:
        
        {self.data_text}
        
        """

        self.prompt_cohere = f"""
        Você é um analista financeiro. Analise os dados abaixo e indique se há sinais de crise financeira,
        como prejuízos recorrentes, aumento de dívidas, queda de receita ou baixa liquidez, explique cada dado de maneira
        que leigos entendam na lingua portugues do brasil.
        Dados financeiros:
        
        {self.data_text}
        
        """

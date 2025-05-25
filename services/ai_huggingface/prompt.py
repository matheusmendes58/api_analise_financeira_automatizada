# Prompt AI

class PromptIA:
    """
    This class is just about PROMPT AI
    """

    def __init__(self, data_text: str = None):

        self.data_text = data_text
        self.prompt = f"""
        Você é um analista financeiro. Analise os dados abaixo e indique se há sinais de crise financeira,
        como prejuízos recorrentes, aumento de dívidas, queda de receita ou baixa liquidez, explique cada dado.
        Dados financeiros:
        
        {self.data_text}
        
        """

import google.generativeai as genai
from decouple import config

genai.configure(api_key=config('API_KEY_GEMINI'))


def get_car_ai_bio(model: str, brand: str, year: int) -> str:
    """
    Gera uma descrição de venda para um carro específico.
    Esta função utiliza a API do Google Generative AI para criar
    uma descrição de venda concisa para o carro especificado,
    incluindo o modelo, a marca e o ano. A descrição gerada
    é limitada a 250 caracteres e deve destacar características
    específicas do modelo.

    Args:
        model (str): O modelo do carro.
        brand (str): A marca do carro.
        year (int): O ano do carro.

    Returns:
        str: Uma descrição de venda gerada para o carro.
    """

    prompt = f"""
        Me mostre uma descrição de venda para o carro {brand} {model} {year}
        em apenas 250 caracteres. Fale coisas específicas desse modelo.
        """

    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(
        prompt,
        generation_config=genai.GenerationConfig(
            max_output_tokens=300,
        ),
    )
    return response.text

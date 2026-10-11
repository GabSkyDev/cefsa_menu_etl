from dotenv import load_dotenv

import requests
import os

load_dotenv()

# Carrega token da API do Telegram a partir das variáveis de ambiente
TELEGRAM_API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")

# Carrega chat_id do Telegram a partir das variáveis de ambiente
TELEGRAM_CHAT_ID =  os.getenv("TELEGRAM_CHAT_ID")

# URL Padrão
URL = f"https://api.telegram.org/bot{TELEGRAM_API_TOKEN}/sendMessage" 

# Função para enviar uma mensagem para o Telegram usando a API Token
def send_telegram_message(message: str):
    if not TELEGRAM_API_TOKEN:
        raise ValueError("TELEGRAM_API_TOKEN não configurada.")

    if not TELEGRAM_CHAT_ID:
        raise ValueError("TELEGRAM_CHAT_ID não configurado.")

    try:
        response = requests.post(
            URL,
            json = {
                "chat_id": TELEGRAM_CHAT_ID,
                "text": message,
                "parse_mode": "Markdown"
            }
        )

        print("Cardápio enviado ao Telegram com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar mensagem para o Telegram: {e}")
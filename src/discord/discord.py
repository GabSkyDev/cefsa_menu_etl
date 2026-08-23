from dotenv import load_dotenv

import requests
import os

load_dotenv()

# Carrega a URL do webhook do Discord a partir das variáveis de ambiente
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

# Função para enviar uma mensagem para o Discord usando o webhook
def send_message(message: str):
    if not DISCORD_WEBHOOK_URL:
        raise ValueError("DISCORD_WEBHOOK_URL não configurada.")

    response = requests.post(
        DISCORD_WEBHOOK_URL,
        json={
            "content": message
        },
        timeout = 10
    )

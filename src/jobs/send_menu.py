from datetime                   import date
from pathlib                    import Path
from src.discord.discord        import send_message
from src.transform.formatter    import format_menu 

import json
import os

# Função para carregar o cardápio do arquivo JSON
def load_menu():
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    
    caminho = os.path.normpath(os.path.join(diretorio_atual, "..", "database", "json_repository.json"))

    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

# Função para encontrar o cardápio do dia atual
def find_day(menu, data_atual):
    for dia in menu["dias"]:

        if dia["data"] == data_atual:
            return dia

    return None

# Função principal que carrega o cardápio, encontra o cardápio do dia atual, formata a mensagem e envia para o Discord
def main():
    menu = load_menu()

    hoje = date.today().isoformat()

    dia = find_day(menu, hoje)

    # Se não houver cardápio para o dia atual, imprime uma mensagem e retorna
    if not dia:
        print(f"Nenhum cardápio encontrado para {hoje}.")
        return

    mensagem = format_menu(dia)

    print(mensagem)

    send_message(mensagem)

    print("Cardápio enviado com sucesso!")

if __name__ == "__main__":
    main()
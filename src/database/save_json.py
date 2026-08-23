import json
import os

# Função para salvar o cardápio em um arquivo JSON 
def save_json(menu: dict):
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))

    caminho = os.path.normpath(os.path.join(diretorio_atual, "..", "database", "json_repository.json"))
    
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(menu, arquivo, indent=4, ensure_ascii=False)
from src.cefsa.client       import extract_menu
from src.transform.parser   import parse_menu
from src.database.save_json import save_json

# Função principal que atualiza o cardápio
def update_menu():
    print("Iniciando atualização do cardápio...")   

    texto = extract_menu()

    print("Cardápio extraído.")

    cardapio = parse_menu(texto)

    print("Cardápio tratado.")

    save_json(cardapio)

    print("Cardápio salvo com sucesso.")

if __name__ == "__main__":
    update_menu()
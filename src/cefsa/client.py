from playwright.sync_api    import sync_playwright
from dotenv                 import load_dotenv

import os

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

USUARIO = os.getenv("CEFSA_USUARIO")
SENHA   = os.getenv("CEFSA_SENHA")

def extract_menu() -> str:
    with sync_playwright() as p:
        # Inicia o navegador Chromium em modo não headless (visível)
        browser = p.chromium.launch(
            headless=True
        )

        # Abre uma nova página no navegador
        page = browser.new_page()

        # Navega até a página de login do CEFSA
        page.goto("https://aluno.cefsa.edu.br/")

        # Preenche os campos de usuário e senha e clica no botão de login
        page.locator("#Usuario").fill(USUARIO)
        page.locator("#senhaAluno").fill(SENHA)
        page.locator("button.btn_login").first.click()

        # Espera até que a página esteja completamente carregada
        page.wait_for_load_state("networkidle")

        # Navega até a página do cardápio
        texto = page.locator("body").inner_text()

        inicio = texto.find("Cardápio Semanal")
        fim = texto.find("Faltas", inicio)

        cardapio_raw = texto[inicio:fim]

        return cardapio_raw
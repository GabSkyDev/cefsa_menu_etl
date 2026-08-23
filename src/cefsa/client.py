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

        # Aguarda o conteúdo do cardápio, pois a página mantém requisições ativas.
        page.wait_for_function(
            "Boolean(document.body && document.body.innerText.includes('Cardápio Semanal'))",
            timeout=60000
        )

        # Navega até a página do cardápio
        texto = page.locator("body").inner_text()

        inicio = texto.find("Cardápio Semanal")
        fim = texto.find("Faltas", inicio)

        if inicio == -1 or fim == -1:
            raise RuntimeError("Não foi possível localizar o cardápio na página autenticada.")

        cardapio_raw = texto[inicio:fim]

        return cardapio_raw
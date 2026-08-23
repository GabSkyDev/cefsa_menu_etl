from datetime import datetime
import re

PADRAO_DIA = re.compile(
    r"^(segunda|terça|quarta|quinta|sexta)[- ]feira\s*\((\d{2}/\d{2})\)$",
    re.IGNORECASE
)

def clean_lines(text: str) -> list[str]:
    linhas = []

    for linha in text.splitlines():
        linha = linha.strip()

        if linha:
            linhas.append(linha)

    return linhas

def identify_meal(linha: str):
    linha = linha.replace("*", "").strip().upper()

    refeicoes = {
        "CAFÉ DA MANHÃ": "cafe_da_manha",
        "ALMOÇO/JANTAR": "almoco_jantar",
        "LANCHE": "lanche",
        "LANCHE REFORÇADO": "lanche_reforcado",
    } 

    return refeicoes.get(linha)


def clean_item(linha: str) -> str:
    linha = re.sub(r"^-\s*", "", linha)
    linha = re.sub(r"\s*\([^)]*\)", "", linha)

    return linha.strip()

def parse_menu(texto: str) -> dict:

    linhas = clean_lines(texto)

    cardapio = {
        "semana": None,
        "dias": []
    }

    dia_atual = None
    refeicao_atual = None
    ano_semana = datetime.now().year

    for linha in linhas:

        # Semana
        if linha.startswith("Cardápio Semanal") and "à" in linha:
            cardapio["semana"] = linha.replace(
                "Cardápio Semanal ",
                ""
            )
            match_ano = re.search(r"\d{2}/\d{2}/(\d{4}|\d{2})", linha)

            if match_ano:
                ano_semana = int(match_ano.group(1))
                if ano_semana < 100:
                    ano_semana += 2000

            continue

        # Dia
        match = PADRAO_DIA.match(linha)

        if match:
            nome_dia = match.group(1).capitalize()
            data = match.group(2)
            data_iso = datetime.strptime(
                f"{data}/{ano_semana}",
                "%d/%m/%Y"
            ).date().isoformat()

            dia_atual = {
                "dia": nome_dia,
                "data": data_iso,
                "refeicoes": {}
            }

            cardapio["dias"].append(dia_atual)

            refeicao_atual = None

            continue

        # Refeição
        refeicao = identify_meal(linha)

        if refeicao and dia_atual:
            refeicao_atual = refeicao
            dia_atual["refeicoes"][refeicao] = []
            continue

        # Item
        if linha.startswith("-") and dia_atual and refeicao_atual:
            item = clean_item(linha)

            if item:
                dia_atual["refeicoes"][refeicao_atual].append(item)

    return cardapio

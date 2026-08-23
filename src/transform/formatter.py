NOMES_REFEICOES = {
    "cafe_da_manha": "Café da manhã",
    "almoco_jantar": "Almoço / Jantar",
    "lanche": "Lanche",
    "lanche_reforcado": "Lanche reforçado",
}


def format_menu(dia: dict) -> str:
    mensagem = [
        f"**CARDÁPIO — {dia['dia'].upper()}**",
        f"Dia: {dia['data']}",
        ""
    ]

    for tipo, itens in dia["refeicoes"].items():

        nome_refeicao = NOMES_REFEICOES.get(
            tipo,
            tipo.replace("_", " ").title()
        )

        mensagem.append(f"**{nome_refeicao}**")

        for item in itens:
            mensagem.append(f"• {item}")

        mensagem.append("")

    mensagem.append("_Cardápio sujeito a alterações!_")

    return "\n".join(mensagem)
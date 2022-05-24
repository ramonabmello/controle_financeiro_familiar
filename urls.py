# monta dicionário com urls dos meses
urls = {"Janeiro": "",
     "Fevereiro": "",
     "Março": "",
     "Abril": "https://docs.google.com/spreadsheets/d/e/2PACX-1vTSVBDzPtj-Eedp0h2r58Yyx7WUBpAIR59x9Xlyfdzcjs9aa9GJNc_BtIPFjaT6Zw/pub?output=xlsx",
     "Maio": "https://docs.google.com/spreadsheets/d/e/2PACX-1vTPFqvirf507tQ0TVeF9hlmBDuWk3bQbPg5vjiHTy7dCskhr7HgQjNp-knblqpCSA/pub?output=xlsx",
     "Junho": "https://docs.google.com/spreadsheets/d/e/2PACX-1vRD6ZrJdCihKBE4LCgV-hdDirkHr4W4ZrQ0eZDEGAn3GF7bUI0YrMh4I7F-F2YbpQ/pub?output=xlsx",
     "Julho": "https://docs.google.com/spreadsheets/d/e/2PACX-1vT8_L0S_fmt3WkLyTS2Mf3fCPjdS7EQocXUjXhrIgxNChFsnlg5jgVW4Vg6U3y-WA/pub?output=xlsx",
     "Agosto": "",
     "Setembro": "",
     "Outubro": "",
     "Novembro": "",
     "Dezembro": ""
}

# retorna url do mês selecionado
def load_url(mes):
    if mes in range(1,12):
        url_mes = list(urls.values())[mes - 1]
    return url_mes

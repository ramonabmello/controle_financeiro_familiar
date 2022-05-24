# monta dicionário com urls dos meses
urls = {"Janeiro": "",
     "Fevereiro": "",
     "Março": "",
     "Abril": "https://docs.google.com/spreadsheets/d/e/2PACX-1vQhWUvK_dmgIrhXrLWD2eynoCTtbkeZ-SsoSMJ80da1nNqB83LcetFEiR4nwazOeg/pub?output=xlsx",
     "Maio": "https://docs.google.com/spreadsheets/d/e/2PACX-1vTciiHRpvyHzxPDYyQbBeXVCMAU5rHvKZIte8IwCd-ZXqu8mWTYYs-7DqI6sPGD7w/pub?output=xlsx",
     "Junho": "https://docs.google.com/spreadsheets/d/e/2PACX-1vQZRPep1sgySQFlHYDsy5zpqdFiU_HKjxlTt6Hg1Ufsn8Hoq5RfMqM8PB4h_zaiEA/pub?output=xlsx",
     "Julho": "https://docs.google.com/spreadsheets/d/e/2PACX-1vTkqbe3RztE8oB3jV7mHRg2CCU8EjRR3hXiNbZXSW_TT4Y5IYMwblxOKnWvf-68Hw/pub?output=xlsx",
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
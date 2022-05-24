# importar pacotes
import pandas as pd
import streamlit as st
import urls

@st.cache
# função que carrega entradas
def carrega_entradas(url):
  entradas = pd.read_excel(url, 0)

  return round(entradas, 2)

# função que carrega gastos
def carrega_gastos(url):
  gastos = pd.read_excel(url, 1)

  return gastos

st.title("Controle financeiro familiar")

# cria dicionário com nomes dos meses
meses = {"Janeiro": 1,
         "Fevereiro": 2,
         "Março": 3,
         "Abril": 4,
         "Maio": 5,
         "Junho": 6,
         "Julho": 7,
         "Agosto": 8,
         "Setembro": 9,
         "Outubro": 10,
         "Novembro": 11,
         "Dezembro": 12
         }

select_mes = st.sidebar.selectbox(
    "Selecione o mês:",
    (list(meses.keys())))

if select_mes in list(meses.keys()):
    select_mes = meses.get(select_mes)
    url = urls.load_url(select_mes)

if url[-4::] == 'xlsx' and len(url) > 4:
  # carrega entradas
  entradas = carrega_entradas(url)

  # carrega gastos
  gastos = carrega_gastos(url)

  # armazena dias de gasto zero
  dias_gasto_zero = gastos.loc[gastos.Valor.isnull(), "Dia"]

  # soma dos gastos por categoria
  gastos_totais = gastos.groupby(gastos.Categoria).sum()

  # acrescentar 3 colunas ao dataframe gastos_totais
  porcent_gastos = []
  porcent_entradas = []

  if len(gastos_totais.index) == 12:
      for n in range(len(gastos_totais.index)):
        valor_gastos = round(float(gastos_totais.Valor[n] / gastos_totais.sum() * 100), 2)
        porcent_gastos.append(valor_gastos)

        valor_entradas = round(float(gastos_totais.Valor[n] / entradas.Valor.sum() * 100), 2)
        porcent_entradas.append(valor_entradas)

      # calcula excedente sodexo
      total_mercado = gastos_totais.loc["Mercado", "Valor"]
      sodexo = entradas.loc[1, "Valor"]
      exced_sodexo = total_mercado - sodexo

      gastos_totais["% Valor Gasto"] = porcent_gastos
      gastos_totais["% Valor Recebido"] = porcent_entradas
      gastos_totais["Excedente Sodexo"] = 0
      gastos_totais.loc["Mercado", "Excedente Sodexo"] = exced_sodexo
      gt = gastos_totais.style.format('{:.2f}')

      # busca nome do mês analisado
      n = gastos.Dia.dt.month[0]
      if n in list(meses.values()):
        mes = list(meses.keys())[n - 1]

      st.markdown(f"Análise dos gastos do mês de {mes}")

      # retorna análise
      # st.write(gt)
      st.table(gt)

      # soma gastos
      soma = round(gastos_totais.Valor.sum(), 2)
      st.markdown(f"TOTAL: R${soma}")
  else:
      st.text("O mês selecionado não possui dados válidos para análise. Por favor, selecione outro.")
else:
  st.text("O mês selecionado não possui dados válidos para análise. Por favor, selecione outro.")
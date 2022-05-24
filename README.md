# Controle financeiro familiar
Dashboard para analisar gastos mensais de uma família.

### Pacotes utilizados:
1. Pandas
2. Streamlit

### Instalando o Streamlit:
Para instalar o Streamlit, abra o Terminal e digite:
```
$ pip install streamlit
```

### Inicializando a aplicação:
Para rodar o dashboard, no Terminal acesse o diretório controle_financeiro_familiar e digite:
```
$ streamlit run script_financeiro.py
```

# Navegando pela aplicação:
Para carregar os dados a serem analisados, no menu lateral selecione o mês a ser analisado:
![image](https://user-images.githubusercontent.com/25406715/170107738-fb4ba2fd-5cc9-4c7a-b582-8b3168bea340.png)

Após selecionar o mês Abril, esse deverá ser o resultado na página principal:
![image](https://user-images.githubusercontent.com/25406715/170107967-b57b7daa-68d5-4b51-b5ef-da2be4f40417.png)

---
### Você pode incluir seus próprios dados na aplicação.

1. Para isso, duplique o arquivo `abril_2022.xlsx` para o seu Google Sheets e preencha a planilha com os seus gastos do mês.

2. Para capturar a URL do arquivo, vá em `Arquivo > Compartilhar > Publicar na Web`, altere o tipo do arquivo para `Microsoft Excel (.xlsx)` e copie a URL que aparece no campo embaixo ('https://docs.google.com/*'):<br>
![image](https://user-images.githubusercontent.com/25406715/170109258-81a8425b-be46-4862-989a-90e9553693f5.png)

3. Cole a URL copiada no arquivo `urls.py`, substituindo a URL do mês de Abril.

4. Faça isso também para os outros meses e você poderá utilizar a aplicação para analisar seus próprios gastos mensais.

import pandas as pd
import requests

# Função para enviar os dados para o endpoint
def enviar_dados_para_endpoint(dados):
    # Substitua 'URL_DO_SEU_ENDPOINT' pela URL real do seu endpoint
    url_endpoint = 'http://localhost:3000'
    response = requests.post(url_endpoint, json=dados)
    if response.status_code == 200:
        print("Dados enviados com sucesso para o endpint!")
    else:
        print("Erro ao enviar dados para o endpoint:", response.status_code)

# Função para ler o arquivo Excel e enviar os dados para o endpoint
def ler_excel_e_enviar_para_endpoint(nome_arquivo):
    try:
        # Carrega o arquivo Excel
        df = pd.read_excel(nome_arquivo)

        # Itera sobre as linhas do DataFrame
        for index, linha in df.iterrows():
            # Converte a linha para um dicionário para enviar como JSON
            dados = linha.to_dict()

            # Enviar os dados para o endpoint
            enviar_dados_para_endpoint(dados)
    except Exception as e:
        print("Erro ao ler o arquivo Excel", e)

# Chama da função para ler o arquivo Excel e enviar os dados para o endpoint
ler_excel_e_enviar_para_endpoint('arquivo_excel.xlsx') 
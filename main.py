import pandas as pd
import requests

# Função para enviar os dados para o endpoint
def enviar_dados_para_endpoint(dados):
    # Substitua 'URL_DO_SEU_ENDPOINT' pela URL real do seu endpoint
    url_endpoint = 'http://localhost:3000/api/cadastro'
    response = requests.post(url_endpoint, json=dados)
    if response.status_code == 200:
        print("Dados enviados com sucesso para o endpint!")
    else:
        print("Erro ao enviar dados para o endpoint:", response.status_code)


# Mapeamento dos nomes dos campos do arquivo Excel para os nomes esperados pelo endpoint
MAPEAMENTO_CAMPOS = {
    'Escola': 'school',
    'Aluno': 'student',
    'Nome da Mãe ': 'mother',
    'Telefone da Mãe': 'motherTel',
    'Nome do Pai ': 'father',
    'Telefone do Pai ': 'fatherTel',
    'R.A': 'tuition',
    'Responsável': 'responsable',
    'Telefone da Responsável': 'responsableTel',
    'cidade': 'cidade',
    'escola': 'escola',
    # Adicione mais mapeamentos conforme necessário
}
# Função para ler o arquivo Excel e enviar os dados para o endpoint
def ler_excel_e_enviar_para_endpoint(nome_arquivo):
    try:
        # Carrega o arquivo Excel
        df = pd.read_excel(nome_arquivo)

        # Itera sobre as linhas do DataFrame
        for index, linha in df.iterrows():
            # Converte a linha para um dicionário para enviar como JSON
            dados = linha.to_dict()

            # Ajusta os nomes dos campos conforme o mapeamento
            dados_corrigidos = {}
            for nome_antigo, nome_esperado in MAPEAMENTO_CAMPOS.items():
                if nome_antigo in dados:
                    # Converte valores numéricos para string
                    valor = dados.pop(nome_antigo)
                    if isinstance(valor, (float, int)):
                        valor = str(valor)
                    dados_corrigidos[nome_esperado] = valor
                    
            # Envia os dados para o endpoint
            enviar_dados_para_endpoint(dados_corrigidos)
    except Exception as e:
        print("Erro ao ler o arquivo Excel", e)

# Chama da função para ler o arquivo Excel e enviar os dados para o endpoint
ler_excel_e_enviar_para_endpoint('arquivo_excel.xlsx') 
import requests
import json
from config import DATABASE_URL


# Função que pega as coletas direto do firebase
def get_cloud_data():
    try:
        response = requests.get(f'{DATABASE_URL}/.json')
        coletas = json.loads(response.content)
        return coletas
    except Exception as e:
        print('Sem conexão para acessar o firebase, aplicação rodando offline!')

# Função que salva a coleta do formulario na tela para o firebase
def save_data(collect_data):
        try:
            response = requests.post(f'{DATABASE_URL}/coletas.json',data=json.dumps(collect_data))
            if response.status_code == 200:
                return True
            else:
                 return response.status_code
        except requests.ConnectionError as timeout:
            return 'Rede indisponivel!'

# Função que vai deletar a coleta no firebase
def delete_data(id_coleta):
     pass

def teste():
    # Chave da API do Firebase
    api_key = 'AIzaSyAKZE6juivJ39G43DO_WZNgTmt6DnU63jA'
    uid = 'PeUADiHGzLSJgaLoygTK1eMaARI3'

    # Parâmetros da requisição (opcional)
    params = {
        # Adicione parâmetros adicionais, se necessário
    }

    # Define os cabeçalhos com a chave da API do Firebase
    
    # Faz a requisição GET
    response = requests.get(f'{DATABASE_URL}/coletas.json?auth={uid}')

    # Verifica se a requisição foi bem sucedida
    if response.status_code == 200:
        # Se a resposta for bem sucedida, imprime o conteúdo da resposta
        print(response.content)
    else:
        # Se a resposta não for bem sucedida, imprime o código de status
        print("Erro:", response.status_code)
                
            


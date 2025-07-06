from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/message')
def hello_world():
    '''
    Endpoint que exibe mensagem

    '''
    return {'message': 'Hello World'}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    '''
    Endpoint para visualizar cardápios dos restaurante

    '''

    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {'Dados': dados_json}
            

        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:            
                dados_restaurante.append({
                    "item": item['Item'], 
                    "price": item['price'],
                    "description": item['description']
                })
        return {'Restaurante': restaurante, 'Cardapio': dados_restaurante}
    else:
        return {'Erro': f'{response.status_code} - {response.text}'}
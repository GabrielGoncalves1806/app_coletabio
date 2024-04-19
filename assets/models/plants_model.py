import flet as ft
import json
from datetime import datetime
from assets.models import fb_model

# Função que pega as especies de plantas do json local
def get_plants_from_data(): 
    with open('assets/data/plants_data.json','r') as file:
        plants = json.load(file)
    return plants

def get_plants_info(): 
    with open('assets/data/plants_info.json','r') as file:
        plants = json.load(file)
    return plants

# Função que cria um arquivo json com os dados temporarios da coleta
def save_temporary_data(page_body):
    date = datetime.now()
    timestamp = str(date.strftime("%d-%m-%Y"))
    # Cria um dicionario com a chave sendo a data e a hora do momento da coleta no formato dd-mm-aaaa-hh-MM
    collect = {timestamp: {}}

    # Varredura dos valores digitados no formulario
    for pos, form in enumerate(page_body.controls):
        collect[timestamp][str(form.controls[0].value)] = str(form.controls[1].value)

    # Salva os valores varridos em um arquivo json temporario
    with open('assets/data/temporary_data.json', "w") as file:
        json.dump(collect,file)

# Função que limpa o arquivo temporario
def erase_temporary_data():
    with open('assets/data/temporary_data.json','w') as file:
        blank_dict = {}
        json.dump(blank_dict,file)

# Função que salva no banco de dados em nuvem os dados temporarios locais
def save_data_on_cloud():
    with open('assets/data/temporary_data.json','r') as file:
        data = json.load(file)

    post_status = fb_model.save_data(data)
    if post_status == True:
        erase_temporary_data()
        return post_status
    else:
        return post_status
    

def verify_temporary_data():
    with open('assets/data/temporary_data.json', "r") as file:
        data = json.load(file)
        if data:
            return True
        else:
            return False



    
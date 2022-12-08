import requests
import json
from email_stvm import clientes_e_acessores
from credentials import api_key, token
from datetime import datetime, timedelta

main_endpoint = "https://api.trello.com/1/"
app_list_id = '638f81631b6d1d019af9e8fe' #lista STVM
daqui_a_15_dias = str((datetime.today() + timedelta(days=15)).strftime("%d/%m/%Y"))
data_hoje = (datetime.today()).strftime("%d/%m/%Y")


def cria_card(nome_card, desc_card):
  endpoint_cria_card = main_endpoint+"cards"
  jsonObj = {"key":api_key, "token":token, "idList": app_list_id, "name":nome_card, "desc": desc_card}
  
  new_card = requests.post(endpoint_cria_card, json=jsonObj)
  
  print(json.loads(new_card.text))
  
for el in clientes_e_acessores():
  desc = 'Cliente: ' + el[0] + "\nAssessor: " + el[1] + "\nData: " + data_hoje + "\nEm 15 dias: " + daqui_a_15_dias
  cria_card("STVM Validada", desc)
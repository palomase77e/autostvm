import win32com.client
import os
from datetime import datetime

date_today = (datetime.today()).strftime("%d/%m/%Y")
#date_today = '23/11/2022'
user = 'psette'
dir_arquivos_stvm = 'C:/Users/{}/Desktop/arquivos_STVM'.format(user)

outlook = win32com.client.Dispatch('outlook.application')
mapi = outlook.GetNamespace("MAPI")
pastaEmailSTVM = mapi.GetDefaultFolder(6).Items.Restrict("[Subject] = 'STVM Validada' And" + \
    "[SenderName] = 'Paloma Fernanda Loureiro Sette' And " + \
    "[SentOn] > '{0} 00:00' And [SentOn] < '{1} 23:59'".format(date_today, date_today)
)

#função que cria uma pasta dentro de um diretório específico
def create_dir(path_new_dir):
    try:
        os.mkdir('{}'.format(path_new_dir))
    except FileExistsError:
        print("O diretório {0} já existe.".format(path_new_dir))

# função que retorna uma lista de bodies de emails de STVMs validadas
def emails_stvm():
    lista_emails_body = []
    for email in pastaEmailSTVM:
        lista_emails_body.append(email.body)
        print(lista_emails_body)
        for arquivo in email.Attachments:
            arquivo.SaveASFile(dir_arquivos_stvm + arquivo.FileName)  
    return lista_emails_body
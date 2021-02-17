import os
from dotenv import load_dotenv, find_dotenv
from datetime import datetime
from netmiko import ConnectHandler
import json
import getDeviceOption

#Recebe o valor da data em que o script é executado (ano-mês-dia)
todays_date = f'{datetime.now():%Y-%m-%d}'

#Aqui é realizada a leitura do arquivo .json onde estão as informações dos dispositivos
with open('devlist.json') as json_file:
    devList = json.load(json_file)

#Função para verificar o tipo de dispositivo (família e modo de conexão) e apartir disso enviar os comandos correspondentes
def executeCMD():

    #Lista de comandos, obtida pelo módulo getDeviceOption
    cmdList = getDeviceOption.option()

    #Loop que percorre cada disopsitivo no arquivo .json
    for dev in devList:
        #Verifica se o dispositivo existe
        if dev:
            print(f'{dev["device_type"]}')
            #Cria uma pasta com o tipo do dispositivo e a data de execução do script
            folder_name = f'{dev["device_type"]}_{todays_date}'
            if folder_name not in os.listdir():
                os.mkdir(folder_name)
            #Realiza a conexão a partir da lib netmiko, com os parâmetros obtidos no arquivo .json
            net_connect = ConnectHandler(device_type=f'{dev["device_type"]}', ip=f'{dev["ip"]}', port=f'{dev["port"]}', username=f'{dev["username"]}', password=f'{dev["password"]}')
            #Cria um arquivo TXT dentro da pasta com o IP do dispositivo
            file = open(f'{folder_name}/{dev["ip"]}.txt', 'a')
            print(f'SCANNING {dev["device_type"]} {dev["ip"]}')

            #Loop para percorrer a lista de comandos
            for cmd in cmdList:
                file.write(f"#"*100 + "\n\n")
                output = net_connect.send_command(cmd)
                print(f"EXECUTANDO {cmd}")
                print(f"#"*70 + "\n")
                file.write(f"#"*100 + "\n\n")
                file.write(f"RESPOSTA PARA {cmd}:\n")
                file.write(output)
                file.write(f"#"*100 + "\n\n")
            file.close()

def main():
    executeCMD()

if __name__=='__main__':
    main()
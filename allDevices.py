import os
from dotenv import load_dotenv, find_dotenv
from datetime import datetime
from netmiko import ConnectHandler
import deviceList

todays_date = f'{datetime.now():%Y-%m-%d}'

ipList = deviceList.exportDeviceList()

mensagem =  ('''
Escolha o dispositivo e o modo de conexão:
1) Cisco SSH
2) Cisco Telnet
3) HP SSH
4) HP Telnet
5) Dell SSH
6) Dell Telnet
''')

def getDevice(option):
    devices = {
        1: [
            'enable',
            'show cdp nei',
            'show lldp nei',
            'show module',
            'show ip interface',
            'show interface brief',
            'show ip route',
            'show version',
            'show run'
        ],
        2:
            ['Display lldp neig',
            'Display module',
            'Display ip intergace',
            'Display interface sum',
            'Display ip route',
            'Display Version',
            'Display cur'
        ],
        3:
            ['enable',
            'show lldp nei',
            'show module',
            'show ip interface',
            'show interface status',
            'show ip route',
            'show version',
            'show run'
        ]
    }
    print(devices[option](dev))
    return devices[option](dev)


def obterTemperatura(option):

    temp = float( input ("Qual é a temperatura ? "))

    calculos = {
        1: lambda temp: temp * 1.8 + 32,
        2: lambda temp: 5 * (temp - 32) / 9,
        3: lambda temp: temp + 273.15,
        4: lambda temp: temp - 273.15,
        5: lambda temp: (temp + 459.67) / 1.8,
        6: lambda temp: temp * 1.8 - 459.67
        }
    return calculos[option](temp)


try:
    option = int( input(mensagem) )
    getDevice(option)
except:
    if not 0 < option < 7:
        raise ValueError("Escolha uma opção válida")

for ip in ipList:
    if ip:
        folder_name = f'{ip['device_type']}_{todays_date}'
        if folder_name not in os.listdir():
            os.mkdir(folder_name)
        net_connect = ConnectHandler(device_type=f'{ip['device_type']}', ip=f'{ip['ip']}', port=f'{'port'}', username=f'{'username'}', password=f'{'password'}')
        file = open(f'{folder_name}/{ip['ip']}.txt', 'a')
        print(f"SCANNING {ip['device_type']} {ip['ip']}")

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

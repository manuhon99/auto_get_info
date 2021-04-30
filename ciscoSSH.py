import os
from dotenv import load_dotenv, find_dotenv
from datetime import datetime
from netmiko import ConnectHandler

device_type = "cisco_ios"
port = 22
username = "developer"
password = "C1sco12345"



ipList = open(r'ipListCisco.txt','r') 


todays_date = f'{datetime.now():%Y-%m-%d}'


#Lista de comandos
cmdList = ['enable', 'show cdp nei', 'show lldp nei', 'show module', 'show ip interface', 'show interface brief',
'show ip route', 'show version', 'show run']


for ip in ipList:
    ip=ip.strip()
    if ip:
        folder_name = f'Cisco_{ip}_{todays_date}'
        if folder_name not in os.listdir():
            os.mkdir(folder_name)
        net_connect = ConnectHandler(device_type=device_type, ip=ip, port=port, username=username, password=password)
        file = open(f'{folder_name}/{ip}.txt', 'a')
        print(f"SCANNING CISCO {ip}")

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

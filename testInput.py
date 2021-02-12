import getCommands

mensagem =  ('''
Escolha o dispositivo e o modo de conexão:
1) Cisco SSH
2) Cisco Telnet
3) HP SSH
4) HP Telnet
5) Dell SSH
6) Dell Telnet
''')

devices = getCommands.exportDeviceList()
for device in devices:
    print(device["device_type"])
    #net_connect.disconnect()

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

try:
    option = int( input(mensagem) )
    getDevice(option)
except:
    if not 0 < option < 7:
        raise ValueError("Escolha uma opção válida")
#Função para mapear a lista de comandos, a partir da opção escolhida pelo usuário
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
        2: [
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
        3:  [
            'Display lldp neig',
            'Display module',
            'Display ip intergace',
            'Display interface sum',
            'Display ip route',
            'Display Version',
            'Display cur'
        ],
        4:  [
            'Display lldp neig',
            'Display module',
            'Display ip intergace',
            'Display interface sum',
            'Display ip route',
            'Display Version',
            'Display cur'
        ],
        5:  [
            'enable',
            'show lldp nei',
            'show module',
            'show ip interface',
            'show interface status',
            'show ip route',
            'show version',
            'show run'
        ],
        6:  [   
            'enable',
            'show lldp nei',
            'show module',
            'show ip interface',
            'show interface status',
            'show ip route',
            'show version',
            'show run'
        ]
    }
    return devices[option]

 


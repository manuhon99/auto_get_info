import deviceType

# Função para o usuário escolher a qual família e tipo de conexão irá direcionar os comandos
def option():
    message =  ('''
    Escolha o dispositivo e o modo de conexão:
    1) Cisco SSH
    2) Cisco Telnet
    3) HP SSH
    4) HP Telnet
    5) Dell SSH
    6) Dell Telnet
    ''')
    try:
        option = int(input(message))
        deviceType.getDevice(option)
    except:
        if not 0 < option < 7:
            raise ValueError("Escolha uma opção válida")

    return deviceType.getDevice(option)

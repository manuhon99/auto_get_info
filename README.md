# Coleta de informações equipamentos Cisco, Dell e HP
 
* Executar pip install -r requirements.txt

* Alterar os arquivos .txt ipList para cada tipo de dispositivo, com os IPs (um por linha)

Os scripts utilizam a biblioteca Netmiko, sendo necessário especificar qual o tipo do dispositivo nos scripts Dell e HP

Em cada .py, é necessário alterar a porta, usuário e senha da conexão (no momento está como exemplo o login da Sandbox gratuita da Cisco)

Para executar, realizar o comando: python nomedoarquivo.py

O script realiza a leitura dos IPs no arquivo .txt e realiza os comandos para cada dispositivo detectado, gerando uma pasta com a data de execução do script e, dentro desta pasta, um arquivo nomeado com o IP contendo os resultados obtidos

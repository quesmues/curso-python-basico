#Cotação e previsão do tempo em tempo real

import requests
import json
import time
import os
import datetime
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

while True:
    try:
        dolar = requests.get('https://api.hgbrasil.com/finance/quotations?format=json', verify=False)
        tempo = requests.get('https://api.hgbrasil.com/weather/?format=json&woeid=455896', verify=False)
        os.system('cls')
        dolar = json.loads(dolar.text)
        tempo = json.loads(tempo.text)

        print('Previsão do tempo para hoje', datetime.datetime.now())
        print(tempo['results']['city'],
              'Máx', tempo['results']['forecast'][0]['max']+'Cº',
              'Min', tempo['results']['forecast'][0]['min']+'Cº','\n')
        print('Cotação do dolar')
        print('Dolar', dolar['results']['currencies']['USD']['buy'])

        print('\n'+'Pressione Ctrl+C para sair')
        time.sleep(2)
    except KeyboardInterrupt:
        print('\nSaindo...')
        exit()



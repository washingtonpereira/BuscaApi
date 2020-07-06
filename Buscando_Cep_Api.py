import requests
import json

__author__ = 'washington'

while True:
    print("Para sair digite sair!")
    busca = input("Digite seu CEP sem pontos ou traços:")
    if busca == 'sair':
        print("saindo")
        break
    if len(busca)!=8:
        print("Impossível buscar, pois os CEPs tem 8 digitos , reinicie o programa")
        break
    else:
        req = requests.get('https://cep.awesomeapi.com.br/json/'+busca)
        ceq = json.loads(req.text)
        if req.status_code == 200:
            print("Dados encontrados")
            print()
            print("Cep:",ceq["cep"])
            print("Estado:",ceq["state"])
            print("Cidade:",ceq["city"])
            print("Rua:",ceq["address_name"])
            print("Bairro:",ceq["district"]+'\n')
        else:
            print("CEP inválido!")

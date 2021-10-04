import requests

def retornaEnd(cep):#retornando cep
    ende = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    endereco = ende.json()
    print(f'{endereco["logradouro"]}')

def retornaHTML(url):#retornando HTML de paginas
    url = requests.get(url)
    return url.text

def retornaMoeda(moeda):
    conversao = requests.get(f'https://economia.awesomeapi.com.br/json/last/{moeda}')
    conver = conversao.text
    conver = conver.split(',')
    conver.pop(0)
    for c in range(len(conver)):
        print(conver[c])

cep = int(input('Insira seu cep: '))
retornaEnd(cep)
#site = retornaHTML('https://web.whatsapp.com/')
#print(site)
#moeda = str(input('Conversao desejada: ')).upper()
#retornaMoeda(moeda)
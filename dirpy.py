import requests

url = input('Url: ')
url2 = url + "/"
wordlist = input('Nome ou caminho do arquivo: ')
lista = []

with open(wordlist, 'r', encoding='utf-8') as f:
    for linha in f:
        linha2 = linha.strip()
        lista.append(linha2)

for itens in lista:
    resposta = requests.get(url2 + itens)
    if resposta.status_code == 200:
        print(f'[+] Diretorio encontrado {itens}')
    else:
        print(f'[-] Diretorio não encontrado {itens}')

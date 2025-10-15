import requests

lista = []

url = input('Url: ')
if not url:
    print('URL not found')

url = url + '/'

while True:
    try:
        wordlist = input('File name or path: ')

        with open(wordlist, 'r', encoding='utf-8') as f:
            for linha in f:
                linha2 = linha.strip()
                lista.append(linha2)
        break

    except FileNotFoundError:
        print('File Not Found')

try:
    for itens in lista:
        resposta = requests.get(url + itens)
        if resposta.status_code == 200:
            print(f'[+] Directory found {itens}')
        else:
            print(f'[-] Directory not found {itens}')

except KeyboardInterrupt:
    print('Intermediate process: KeyboardInterrupt')

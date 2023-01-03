from bs4 import BeautifulSoup
from produto import Produto
from colorama import Fore, Style
from datetime import date
import csv
import requests

links = []
produtos = []

# Captura os links dado o nome do arquivo txt que possui os mesmos
def capturar_links(nome_arquivo):
    try:
        # Arquivo que tem os links dos produtos que devem ser monitorados
        arquivo_links = open(f'{nome_arquivo}', 'r', encoding='UTF-8')
        print(Fore.GREEN + f'[+] {nome_arquivo} aberto com sucesso!')
        for linha in arquivo_links:
            linha = linha.replace('\n', '')
            links.append(linha)
        print(Fore.GREEN + f'[+] Links do arquivo {nome_arquivo} foram capturados!')
    except OSError:
        print(Fore.RED + f'[-] Não foi possível abrir o arquivo {nome_arquivo}!')

def formatar_preco(string):
    # Remover R$
    string = string.replace('R$', '')
    # Remover espaço em branco
    string = string.strip()

    if '.' in string:
        string = string.replace('.', '')
    string = string.replace(',', '.')
    return string

# Realiza o processo de captura dos dados de determinado link, isto é, um produto da KaBuM
def capturar_dados_link(link):
    # Caso vá utilizar o script, coloque seu User Agent verdadeiro para conseguir fazer o scraping de dados
    # User Agent aleatório da internet
    headers = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 RuxitSynthetic/1.0 v3556852051 t3569072820071885698 athfa3c3975 altpub cvcv=2 smf=0'} 

    pagina = requests.get(link, headers=headers)
    if pagina.status_code == 200:
        print(Fore.GREEN + '[+] Página carregada com sucesso!')            
        soup = BeautifulSoup(pagina.content, 'lxml')
        try:
            nome = soup.find('h1', {'class' : 'sc-fb499f01-5 kXcukN'}).get_text()
            preco = soup.find('h4', {'class' : 'sc-d6a30908-1 cRUUoc finalPrice'}).get_text()

            produto = Produto()
            produto.set_nome(nome)
            produto.set_preco(formatar_preco(preco))
            produto.set_link(link)
            print(Fore.GREEN + '[+] Dados do produto foram scrapados com sucesso!')
            return produto
        except:
            print(Fore.RED + '[-] Não foi possível scrapar os dados do produto!')
    else:
        print(Fore.RED + '[-] Não foi possível entrar na página, portanto, os dados do produto contido no link não foram consultados!')

def scrape_todos_links():
    from time import sleep
    for url in links:
        produtos.append(capturar_dados_link(url))
        print()
        sleep(4)

def registrar_dados(nome_arquivo, produtos):
    data_atual = date.today()
    data_atual = data_atual.strftime("%d/%m/%Y")
    contador = 1

    try:
        arquivo = open(f'{nome_arquivo}.csv', 'a+', encoding='UTF-8', newline='')
        print(Fore.GREEN + f'[+] {nome_arquivo}.csv aberto com sucesso!')
        writer = csv.writer(arquivo, delimiter=';')

        for produto in produtos:
            try:
                linha = [produto.get_nome(), produto.get_preco(), data_atual, produto.get_link()]
                writer.writerow(linha)
                print(Fore.GREEN + f'[+] Produto {contador} registrado...')
            except:
                print(Fore.RED + f'[-] Não foi possível registrar o produto {contador}...')
            contador += 1
        arquivo.close()
    except:
        print(Fore.RED + f'[-] Não foi possível abrir o arquivo {nome_arquivo}.csv para registrar os dados!')

nome_arquivo = str(input('Digite o nome do arquivo que possui os links: '))
capturar_links(nome_arquivo)
print()
scrape_todos_links()
print(Style.RESET_ALL, end='')
nome_bd_produtos = str(input('Digite o nome do arquivo (csv) que vai registrar os dados dos produtos: '))
registrar_dados(nome_bd_produtos, produtos)
print(Style.RESET_ALL, end='')
print('Programa finalizado!')
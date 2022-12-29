from bs4 import BeautifulSoup
from produto import Produto
import requests

links = []

# Função que vai capturar os links dado o nome do arquivo txt que possui os mesmos
def capturar_links(nome_arquivo):
    try:
        # Arquivo que tem os links dos produtos que devem ser monitorados
        arquivo_links = open(f'{nome_arquivo}', 'r', encoding='UTF-8')
        print(f'{nome_arquivo} aberto com sucesso!')
        for linha in arquivo_links:
            linha = linha.replace('\n', '')
            links.append(linha)
        print('Links do arquivo foram capturados')
    except OSError:
        print(f'Não foi possível abrir o arquivo {nome_arquivo}!')
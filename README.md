# Sobre o projeto
Este projeto de WebScraper foi feito utilizando Python, com o intuito de apenas obter os dados de produtos oriundos da loja KaBuM (para quem gosta de se manter atualizado quanto às variações de preço, etc).

Ao executar o projeto, fornecendo um arquivo de texto que contém os links de quaisquer produtos da loja, você poderá manter um histórico dos mesmos, visto que o projeto vai registrar em um arquivo csv, os dados dos produtos (nomes, preços [no pix]), assim como, a data em que tal produto foi consultado e registrado.

# Requisitos
- Python 3.10+
## Bibliotecas
- lxml
- requests
- beautifulsoup4
- colorama

# Instruções para executar o projeto
```python
pip install lxml requests beautifulsoup4 colorama
```
```bash
git clone https://github.com/feli0x1/webscraperkabum
cd webscraperkabum
python main.py
```
# Demo do projeto em execução
YouTube link: https://youtu.be/OzvPyHFzguE

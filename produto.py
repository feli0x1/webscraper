class Produto:
    def __init__(self):
        self.nome = ''
        self.preco = 0.0
        self.link = ''

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_preco(self):
        return self.preco

    def set_preco(self, preco):
        self.preco = preco
    
    def get_link(self):
        return self.link

    def set_link(self, link):
        self.link = link

    def imprimirAtributos(self):
        print(f'{self.get_nome()}')
        print(f'R$ {self.get_preco()}')
        print(f'{self.get_link()}')
class Produto:
    def __init__(self, nome, preco, tipo, link):
        self.nome = nome
        self.preco = preco
        self.tipo = tipo
        self.link = link

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_preco(self):
        return self.preco

    def set_preco(self, preco):
        self.preco = preco

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, tipo):
        self.tipo = tipo

    def get_link(self):
        return self.link
        
    def set_link(self, link):
        self.link = link
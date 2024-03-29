from modelo.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init___(nome, preco)
        self.tamanho = tamanho
    def __str__(self):
        return self.nome
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.08)
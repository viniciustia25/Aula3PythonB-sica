from abc import ABC, abstractmethod

class ItemCardapio(ABC)
    def __inti__(self, nome, preco):
        self._nome = nome
        self._preco = preco

@abstractmethod
def aplicar_desconto(self):
    pass


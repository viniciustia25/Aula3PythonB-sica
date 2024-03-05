from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5.00, 'grande')
bebida_suco.aplicar_desconto()
prato_couvert = Prato('Couvert', 2.00, 'O melhor pão da cidade')
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_couvert)


def main():
    print(bebida_suco)
    print(prato_couvert)

if __name__ == '__main__':
    main()
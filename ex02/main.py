from pedido import Pedido
from itempedido import ItemPedido
from produto import Produto

hamburguer = Produto(1234, 15.00, "Hamburger comum")
xburguer  = Produto(2, 20.00, "X-Burguer")
xtudo = Produto(33, 22.90, "X-Tudo")
xfranstudo = Produto(3213, 25.00, "X-Franstudo")
gurana = Produto(442, 4.00, "Guaraná Lata")
cocacola = Produto(244, 6.00, "Coca-Cola Lata")

pedido1 = Pedido()
item = ItemPedido(xtudo,1)
pedido1.adicionar_item(item)
item = ItemPedido(hamburguer,1)
pedido1.adicionar_item(item)
item = ItemPedido(xburguer,1)
pedido1.adicionar_item(item)
item = ItemPedido(gurana,1)
pedido1.adicionar_item(item)
print("Valor total do pedido 1 = ", pedido1.obter_total())

pedido2 = Pedido()
item = ItemPedido(xfranstudo, 1)
pedido2.adicionar_item(item)
item = ItemPedido(cocacola, 1)
pedido2.adicionar_item(item)
print("Valor total do pedido 2 = ", pedido2.obter_total())
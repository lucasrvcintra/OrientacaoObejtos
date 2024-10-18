# Classe Produto:
# Atributos: nome, preco, quantidade_estoque, categoria
# Métodos: adicionar_estoque, remover_estoque, aplicar_desconto
# adicionar_estoque(quantidade): Adiciona quantidade ao quantidade_estoque.
# remover_estoque(quantidade): Remove quantidade do quantidade_estoque, se houver quantidade suficiente.
# aplicar_desconto(percentual): Aplica um desconto de percentual ao preco do produto.

class Produto:
  def __init__(self, nome, preco, quantidade_estoque, categoria):
    self.nome = nome
    self.preco = preco
    self.quantidade_estoque = quantidade_estoque
    self.categoria = categoria

  def adicionar_estoque(self, quantidade):
    if quantidade >= 0:
      self.quantidade_estoque += quantidade
    else:
      print("Quantidade invalida")

  def remover_estoque(self, quantidade):
    if self.quantidade_estoque >= quantidade:
      self.quantidade_estoque -= quantidade
    else:
      print("Quantidade invalida")

  def aplicar_desconto(self, percentual):
    self.preco -= self.preco * (percentual / 100)

  def __str__(self):
    return f"{self.nome}, {self.preco}, {self.quantidade_estoque}, {self.categoria}"  
  
print ("Produto criado")

p = Produto("Caneta", 1.99, 10, "Escolar")
p.adicionar_estoque(10)
p.remover_estoque(5)
p.aplicar_desconto(10)
print(p)  


# Classe Pessoa:
# Atributos: nome, idade, altura, peso
# Métodos: envelhecer, crescer, ganhar_peso, perder_peso
# envelhecer(): Aumenta a idade da pessoa em um ano.
# Crescer(entímetros): Aumenta a altura da pessoa em centímetros, se a pessoa tiver menos de 21 anos.
# Ganhar_peso(quilos): Aumenta o peso da pessoa em quilos.
# Perder_peso(quilos): Diminui o peso da pessoa em quilos.

class Pessoa:

  def __init__(self, nome, idade, altura, peso):
    self.nome = nome
    self.idade = idade
    self.altura = altura
    self.peso = peso

  def envelhecer(self):
    self.idade += 1

  def crescer(self, ent):
    if self.idade < 21:
      self.altura += ent

  def ganhar_peso(self, kg):
    self.peso += kg

  def perder_peso(self, kg):
    self.peso -= kg 
  
print("Pessoa criada")

pessoa = Pessoa("Joaquim", 20, 1.80, 80.0)

print(pessoa.nome)
print(pessoa.idade)
print(pessoa.altura)
print(pessoa.peso)

pessoa.envelhecer()
pessoa.crescer(0.05)
pessoa.ganhar_peso(10.0)
pessoa.perder_peso(5.0)

print(pessoa.nome)
print(pessoa.idade)
print(pessoa.altura)
print(pessoa.peso)
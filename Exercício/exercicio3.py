class Estado:
  def __init__(self, nome):
    self.nome = nome

class Cidade:
  def __init__(self, nome, estado):
    self.nome = nome
    self.estado = estado

class Filial:
  def __init__(self, nome, cidade):
    self.nome = nome
    self.cidade = cidade

class Funcionario:
  def __init__(self, nome, filial):
    self.nome = nome
    self.filial = filial
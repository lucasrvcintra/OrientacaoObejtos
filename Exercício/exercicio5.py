class Filial:
  def __init__(self, nome, cidade):
    self.nome = nome
    self.cidade = cidade

class Empresa:
  def __init__(self, nome, filial):
    self.nome = nome
    self.filial = filial

class Funcionario:
  def __init__(self, nome, filial):
    self.nome = nome
    self.filial = filial
class Departamento:
  def __init__(self, nome):
    self.nome = nome

class Funcionario:
  def __init__(self, nome, cargo, salario, departamento):
    self.nome = nome
    self.cargo = cargo
    self.salario = salario
    self.departamento = departamento

class Escolaridade:
  def __init__(self, nome):
    self.nome = nome
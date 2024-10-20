class Departamento:
  def __init__(self):
    self.chefe = None

  def get_chefe(self):
    return self.chefe
  
  def set_chefe(self, chefe):
    self.chefe = chefe
  
  def get_nome_escolaridade_chefe(self):
    if self.chefe == None:
      print("Departamento nao possui chefe")
      exit()
    return self.chefe.get_nome_escolaridade()
  

class Funcionario:
  def __init__(self, escolaridade):
    self.set_escolaridade(escolaridade)

  def get_escolaridade(self):
    return self.escolaridade
  
  def set_escolaridade(self, escolaridade):
    if escolaridade == None:
      print("Funcionario nao pode ficar sem escolaridade")
      exit()
    self.escolaridade = escolaridade

  def get_nome_escolaridade(self):
    return self.escolaridade.get_nome()

class Escolaridade:
  def __init__(self):
    self.nome = ""
  
  def get_nome(self):
    return self.nome
  
  def set_nome(self, nome):
    self.nome = nome

escolaridade = Escolaridade()
escolaridade.set_nome("Graduacao")

funcionario = Funcionario(escolaridade)

departamento = Departamento()
departamento.set_chefe(funcionario)

print(departamento.get_nome_escolaridade_chefe())
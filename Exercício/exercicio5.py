class Filial:
  def __init__(self):
    self.diretor = None

  def get_diretor(self):
    return self.diretor

  def set_diretor(self, nome):
    self.diretor = nome
  
  def get_nome_diretor_empresa(self):
    if self.diretor == None:
      print("Diretor não informado")
      exit()
    else:
      return self.diretor.get_nome_funcionario()

class Empresa:
  def __init__(self, funcionario):
    self.set_funcionario(funcionario)
  
  def get_funcionario(self):
    return self.funcionario

  def set_funcionario(self, funcionario):
    if funcionario == None:
      print("Funcionario não informado")
      exit()
    else:
      self.funcionario = funcionario
  
  def get_nome_funcionario(self):
    return self.funcionario.get_nome()
    

class Funcionario:
  def __init__(self):
    self.nome = ""

  def get_nome(self):
    return self.nome

  def set_nome(self, nome):
    self.nome = nome
  
funcionario = Funcionario()
funcionario.set_nome("Lucas")

empresa = Empresa(funcionario)

filial = Filial()
filial.set_diretor(empresa)

print(filial.get_nome_diretor_empresa())
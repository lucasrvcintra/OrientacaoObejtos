class Funcionario:
  def __init__(self):
    self.estado = None

  def get_estado(self):
    return self.estado
  
  def set_estado(self, estado):
    self.estado = estado

  def get_nome_estado_filial(self):
    return self.estado.get_nome_estado_cidade()

class Filial:
  def __init__(self):
    self.cidade = None

  def get_cidade(self):
    return self.cidade
  
  def set_cidade(self, estado):
    self.cidade = estado
  
  def get_nome_estado_cidade(self):
    return self.cidade.get_nome_estado()


class Cidade:
  def __init__(self, estado):
    self.set_estado(estado)

  def get_estado(self):
    return self.estado
  
  def set_estado(self, estado):
        if estado == None:
            print("Cidade não pode ficar sem estado")
            exit()
        self.estado = estado

  def get_nome_estado(self):
    return self.estado.get_nome()
    

class Estado:
  def __init__(self):
    self.nome = None

  def get_nome(self):
    return self.nome
  
  def set_nome(self, estado):
    self.nome = estado


estado = Estado()
estado.set_nome("Minas Gerais")

cidade = Cidade(estado)

filial = Filial()
filial.set_cidade(cidade)

funcionario = Funcionario()
funcionario.set_estado(filial)

print(funcionario.get_nome_estado_filial())
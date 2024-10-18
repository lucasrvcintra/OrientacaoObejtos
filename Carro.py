class Carro():
    def __init__(self, marca, modelo):
        self.marca = marca 
        self.modelo = modelo
        self.ano = 0
        self.velocidade_atual = 0
        self.ligado = False


    def get_modelo(self):
        return self.modelo

    def set_modelo(self, modelo):
        if modelo == "":
          print("Modelo invalido")
        else:
          self.modelo.nome = modelo

    def get_ano(self):
        return self.ano

    def set_ano(self, ano):
        if ano <= 1886 or ano >= 2025:
          print("Ano invalido")
        else:
          self.ano = ano

    def get_velocidade_atual(self):
        return self.velocidade_atual

    def set_velocidade_atual(self, velocidade):
        if velocidade >= 0:
          self.velocidade_atual = velocidade
        else:
            print("Velocidade invalida")

    def get_ligado(self):
        return self.ligado

    def set_ligado(self, ligado):
        if ligado == True or ligado == False:
          self.ligado = ligado
        else:
            print("ligado invalido")

    def ligar(self):
        if not self.ligado:
          self.ligado = True
        else:
            print("Carro ja esta ligado")

    def desligar(self):
        if self.ligado:
          self.ligado = False
          self.velocidade_atual = 0
        else:
            print("Carro ja esta desligado")
    
    def acelerar(self, velocidade): #adicionar validacao de ligado e desligado para acelerar e frear
        if velocidade < 0 and type(velocidade) != int and not self.ligado:
          return print("Velocidade invalida")
        
        if velocidade >= 0:
          self.velocidade_atual += velocidade
        else:
            if self.velocidade_atual < 0: 
              self.velocidade_atual -= velocidade
            else:
               self.velocidade_atual = 0;

    def frear(self, velocidade):
       if self.velocidade_atual-velocidade>=0 and type(velocidade) == int and self.ligado:
           self.velocidade_atual = self.velocidade_atual - velocidade
       else:
           self.velocidade_atual = 0
    
    def get_nome_marca(self):
        if self.marca == None:
          print("Marca vazia")
        else:
          return self.marca.get_nome()
    def set_marca(self, marca):
        if marca == None:
          print("Modelo sem marca")
        else:
          self.marca.nome = marca

    def get_nome_modelo(self):
        if self.modelo == None:
          print("Modelo sem nome")
        else:
          return self.modelo.get_nome()
class Marca():
    def __init__(self):
        self.nome = ""

    def set_nome(self, nome):
       if nome == "":
          print("Carro está sem marca")
       else:
        self.nome = nome
    def get_nome(self):
        return self.nome
    
class Modelo ():
    def __init__(self):
        self.nome = ""

    def set_nome(self, nome):
       self.nome = nome
    def get_nome(self):
        return self.nome

modelo = Modelo()
marca = Marca()
carro = Carro(marca, modelo)

carro.set_marca("Fiat")
carro.set_modelo("Marea")


print(carro.get_nome_marca())
print(carro.get_nome_modelo())




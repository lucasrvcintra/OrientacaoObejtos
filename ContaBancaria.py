# Classe ContaBancaria:
#Atributos: titular, numero_conta, saldo
#Métodos: depositar, sacar
#depositar(valor): adiciona o valor ao saldo da conta.
#sacar(valor): subtrai o valor do saldo da conta, se houver saldo suficiente.

class ContaBancaria():

  def __init__(self, titular, numero_conta): 
    self.titular = titular
    self.numero_conta = numero_conta
    self.saldo = 0

  def get_titular(self):
    return self.titular

  def get_saldo(self):
    return self.saldo
  
  def get_numero_conta(self):
    return self.numero_conta
  
  def depositar(self, valor):
    if valor >= 0:
      self.saldo += valor
    else:
      print("Valor invalido")
  
  def sacar(self, valor):
    if self.saldo - valor >= 0:
      self.saldo -= valor
    else:
      print("Saldo disponível: ", self.saldo)


contaBancaria = ContaBancaria("Lucas Cintra", "123456")
contaBancaria.depositar(1000)

print(contaBancaria.get_titular())
print(contaBancaria.get_saldo())
print(contaBancaria.get_numero_conta())

contaBancaria.depositar(500)
print(contaBancaria.get_saldo())

contaBancaria.sacar(200)
print(contaBancaria.get_saldo())
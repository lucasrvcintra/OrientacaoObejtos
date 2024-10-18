# Classe Funcionario:
# Atributos: nome, cargo, salario, departamento
# Métodos: receber_aumento, mudar_departamento, exibir_dados
# receber_aumento(percentual): Aplica um aumento de percentual ao salario.
# mudar_departamento(novo_departamento): Altera o departamento para o novo_departamento.
# exibir_dados(): Exibe os dados do funcionário, incluindo nome, cargo, salário e departamento.

class Funcionario:
  def __init__(self, nome, cargo, salario, departamento):
    self.nome = nome
    self.cargo = cargo
    self.salario = salario
    self.departamento = departamento

  def receber_aumento(self, percentual):
    self.salario += self.salario * (percentual / 100)

  def mudar_departamento(self, novo_departamento):
    self.departamento = novo_departamento

  def exibir_dados(self):
    print(f"Nome: {self.nome}")
    print(f"Cargo: {self.cargo}")
    print(f"Salário: {self.salario}")
    print(f"Departamento: {self.departamento}")

print("Funcionario criado")

func = Funcionario("Joaquim", "Programador", 2000, "TI")
func.receber_aumento(10)
func.mudar_departamento("RH")
func.exibir_dados()

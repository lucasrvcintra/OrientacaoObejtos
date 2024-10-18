class Funcionario:
    def __init__(self):
        self.departamento = None

    def get_pais_alocacao(self):
        if self.departamento is None or self.departamento.empresa is None or self.departamento.empresa.grupo is None:
            print("Informações incompletas sobre o funcionário, empresa ou grupo.")
            return None
        else:
            return self.departamento.empresa.grupo.pais.get_nome()

    def set_departamento(self, departamento):
        self.departamento = departamento


class Departamento:
    def __init__(self):
        self.empresa = None

    def set_empresa(self, empresa):
        self.empresa = empresa


class Empresa:
    def __init__(self):
        self.grupo = None

    def set_grupo(self, grupo):
        self.grupo = grupo


class Grupo:
    def __init__(self):
        self.pais = None

    def set_pais(self, pais):
        self.pais = pais


class Pais:
    def __init__(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome


# Criando instâncias e exemplo de uso
pais_brasil = Pais("Brasil")
grupo = Grupo()
grupo.set_pais(pais_brasil)

empresa = Empresa()
empresa.set_grupo(grupo)

departamento = Departamento()
departamento.set_empresa(empresa)

funcionario = Funcionario()
funcionario.set_departamento(departamento)

# Obtendo o país de alocação do funcionário
print(funcionario.get_pais_alocacao())  # Deve imprimir "Brasil"

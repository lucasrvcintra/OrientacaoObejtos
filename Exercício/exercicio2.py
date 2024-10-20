class Funcionario:
    def __init__(self):
        self.pais_alocacao = None

    def get_pais_alocacao(self):
        return self.pais_alocacao

    def set_pais_alocacao(self, pais_alocacao):
        self.pais_alocacao = pais_alocacao

    def get_nome_pais_alocacao_departamento(self):
        if self.pais_alocacao == None:
            print("Não existe pai")
            exit()
        else:
            return self.pais_alocacao.get_pais_alocacao_departamento()


class Departamento:
    def __init__(self):
        self.empresa = None

    def get_empresa(self):
        return self.empresa

    def set_empresa(self, empresa):
        self.empresa = empresa

    def get_pais_alocacao_departamento(self):
        if self.empresa == None:
            print("Não existe empresa")
            exit()
        else:
            return self.empresa.get_nome_pais_grupo()

class Empresa:
    def __init__(self):
        self.grupo = None
    
    def get_grupo(self):
        return self.grupo

    def set_grupo(self, grupo):
        self.grupo = grupo

    def get_nome_pais_grupo(self):
        if self.grupo == None:
            print("Não existe grupo")
            exit()
        else:
            return self.grupo.get_nome_pais()


class Grupo:
    def __init__(self, pais):
        self.set_pais(pais)

    def get_pais(self):
        return self.pais

    def set_pais(self, pais):
        if pais == None:
            print("Grupo não pode ficar sem pais")
            exit()
        self.pais = pais

    def get_nome_pais(self):
        return self.pais.get_nome()


class Pais:
    def __init__(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

        

class Grupo:
    def _init_(self):
        self.presidente = None
    def get_presidente(self):
        return self.presidente
    def set_presidente(self, presidente):
        self.presidente = presidente
    def get_nome_escolaridade_presidente(self):
        if self.presidente == None:
            print("Grupo está sem presidente")
        else:
            return self.presidente.get_nome_escolaridade()

class Funcionario:
    def _init_(self, escolaridade):
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
    def _init_(self):
        self.nome = ""
    def get_nome(self):
        return self.nome
    def set_nome(self, nome):
        self.nome = nome


escolaridade = Escolaridade()
escolaridade.set_nome("Graduacao")
funcionario = Funcionario(escolaridade)
grupo = Grupo()
grupo.set_presidente(funcionario)
print(grupo.get_nome_escolaridade_presidente())
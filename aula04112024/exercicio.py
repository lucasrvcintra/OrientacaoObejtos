class Curso:
    def __init__(self):
        self.alunos = []
    def matricular(self, aluno):
        self.alunos.append(aluno)
    def matricular_alunos(self, alunos):
        for aluno in alunos:
            self.alunos.append(aluno)
    def get_alunos(self):
        for aluno in self.alunos:
            print(aluno.get_nome())
    def verificar_matricula(self, aluno):
        return aluno in self.alunos
    def remover_aluno(self, aluno):
        self.alunos.remove(aluno)

class Aluno:
    def __init__(self):
        self.nome = ""
    def set_nome(self, nome):
        self.nome = nome
    def get_nome(self):
        return self.nome

aluno1 = Aluno()
aluno1.set_nome("Ana")
aluno2 = Aluno()
aluno2.set_nome("Maria")
aluno3 = Aluno()
aluno3.set_nome("Joao")
curso = Curso()
curso.matricular(aluno1)
curso.matricular(aluno2)
curso.get_alunos()
print(curso.verificar_matricula(aluno1))
print(curso.verificar_matricula(aluno2))
print(curso.verificar_matricula(aluno3))
curso.remover_aluno(aluno2)
print(curso.verificar_matricula(aluno2))


matriculas = []
aluno4 = Aluno()
aluno4.set_nome("Maria Angelica")
aluno5 = Aluno()
aluno5.set_nome("Maria Joana")
aluno6 = Aluno()
aluno6.set_nome("Jose")
matriculas.append(aluno4)
matriculas.append(aluno5)
matriculas.append(aluno6)
curso.matricular_alunos(matriculas)
curso.get_alunos()
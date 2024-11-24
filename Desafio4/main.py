class Pessoa:
    def __init__(self):
        self.nome = ""
    
    def set_nome(self, nome):
        self.nome = nome
    
    def get_nome(self):
        return self.nome

class Professor(Pessoa):
    pass

class Aluno(Pessoa):
    pass

class Curso:
    def __init__(self):
        self.nome = ""
        self.turmas = []
    
    def set_nome(self, nome):
        self.nome = nome
    
    def get_nome(self):
        return self.nome

    def adicionar_turma(self, turma):
        self.turmas.append(turma)
    
    def exibir_turmas(self):
        for turma in self.turmas:
            print(f"Turma: {turma.nome}")
    
    def verificar_turma(self, turma):
        return turma in self.turmas
    
    def excluir_turma(self, turma):
        self.turmas.remove(turma)

class Turma:
    def __init__(self):
        self.nome = ""
        self.professor = None
        self.alunos = []
        self.disciplinas = []
    
    def set_nome(self, nome):
        self.nome = nome
    
    def get_nome(self):
        return self.nome
    
    def set_professor(self, professor):
        self.professor = professor
    
    def get_professor(self):
        return self.professor
    
    def get_nome_professor(self):
        if self.professor is None:
            return "Turma sem professor"
        else:
            return self.professor.get_nome()
    
    def matricular(self, aluno):
        self.alunos.append(aluno)
    
    def exibir_alunos(self):
        for aluno in self.alunos:
            print(aluno.get_nome())
    
    def verificar_aluno(self, aluno):
        return aluno in self.alunos
    
    def excluir_aluno(self, aluno):
        self.alunos.remove(aluno)
    
    def adicionar_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)
    
    def exibir_disciplinas(self):
        for disciplina in self.disciplinas:
            print(disciplina.get_nome())

    def verificar_disciplina(self, disciplina):
        return disciplina in self.disciplinas

class Disciplina:
    def __init__(self):
        self.nome = ""
    
    def set_nome(self, nome):
        self.nome = nome
    
    def get_nome(self):
        return self.nome


# Instanciando objetos para testar as funcionalidades

# Criando professor
professor = Professor()
professor.set_nome("Ana")

# Criando turma e associando professor
turma = Turma()
turma.set_nome("Turma 1")
turma.set_professor(professor)

# Criando alunos e matriculando-os
aluno1 = Aluno()
aluno1.set_nome("José")
aluno2 = Aluno()
aluno2.set_nome("João")
turma.matricular(aluno1)
turma.matricular(aluno2)

# Criando curso e associando turma
curso = Curso()
curso.set_nome("Curso de Programação")
curso.adicionar_turma(turma)

# Criando disciplinas e adicionando à turma
disciplina1 = Disciplina()
disciplina1.set_nome("Matemática")
disciplina2 = Disciplina()
disciplina2.set_nome("Física")
turma.adicionar_disciplina(disciplina1)
turma.adicionar_disciplina(disciplina2)

# Respostas às perguntas
print(f"1) Nome do professor da turma: {turma.get_nome_professor()}")

print("2) Alunos da turma:")
turma.exibir_alunos()

print("3) Professores das turmas do curso:")
for turma in curso.turmas:
    print(turma.get_nome_professor())

print("4) Alunos das turmas do curso:")
for turma in curso.turmas:
    turma.exibir_alunos()

print("5) Alunos registrados no curso:")
for turma in curso.turmas:
    turma.exibir_alunos()

print("6) Disciplinas nas turmas do curso:")
for turma in curso.turmas:
    turma.exibir_disciplinas()

print(f"7) José está na turma? {'Sim' if turma.verificar_aluno(aluno1) else 'Não'}")

print(f"8) José está no curso? {'Sim' if turma.verificar_aluno(aluno1) else 'Não'}")

print(f"9) Turma 1 está no curso? {'Sim' if curso.verificar_turma(turma) else 'Não'}")

turma.excluir_aluno(aluno1)
print(f"10) José excluído da turma. Ele está na turma? {'Sim' if turma.verificar_aluno(aluno1) else 'Não'}")

curso.excluir_turma(turma)
print(f"11) Turma excluída do curso. Turma está no curso? {'Sim' if curso.verificar_turma(turma) else 'Não'}")

print(f"12) José no curso após exclusão da turma? {'Sim' if turma.verificar_aluno(aluno1) else 'Não'}")
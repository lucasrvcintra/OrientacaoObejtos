class Curso:
  def __init__(self):
    self.turmas = []
    self.alunos = []

class Turma:
  def __init__(self):
    self.disciplina = ""
    self.professor = None
    self.alunos = []

  def get_professor(self):
     return self.professor.get_nome()

  def set_professor(self, professor):
     self.professor.set_nome(professor)
  
  
class Pessoa:
    def _init_(self, nome):
        self.set_nome(nome)
        self.nome = nome
    def get_nome(self):
        return self.nome
    def set_nome(self, nome):
        if nome == "":
            print("Nome invalido")
            exit()
        self.nome = nome

class Professor(Pessoa):
    def _init_(self, nome):
        Pessoa._init_(self, nome)
        

    
class Aluno(Pessoa):
    def _init_(self, nome):
        Pessoa._init_(self, nome)


professor = Professor()
professor.set_nome("Charles")

turma = Turma()
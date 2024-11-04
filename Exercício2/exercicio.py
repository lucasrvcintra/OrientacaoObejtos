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
        self.titulacao = ""
        
    def setTitulacao(self, titulacao):
      self.titulacao = titulacao
      
    def getTitulacao(self):
      return self.titulacao

class Aluno(Pessoa):
    def _init_(self, nome):
        Pessoa._init_(self, nome)
        self.nota1= 0
        self.nota2= 0
        self.matricula=0
        
    def setMatricula(self, matricula):
      self.matricula = matricula
        
    def getMatricula(self):
      return self.matricula
    
    def setNota1(self, nota1):
      if nota1 < 0 or nota1 > 10:
        print("Nota Invalida")
        exit()
      self.nota1 = nota1
    
    def setNota2(self, nota2):
      if nota2 < 0 or nota2 > 10:
        print("Nota Invalida")
        exit()
      self.nota2 = nota2
        
class AlunoEnsinoMedio(Aluno):
  def media(self):
    media = (self.nota1 + self.nota2)/2
    if media >= 6:
      return "Aprovado"
    else:
      return "Reprovado"
      

class AlunoGraduação(Aluno):
  def media(self):
    media = (self.nota1 + self.nota2)/2
    if media >= 7:
      return "Aprovado"
    else:
      return "Reprovado"

aluno1 = AlunoEnsinoMedio("Ana")
aluno1.setMatricula(12365478)
aluno1.setNota1(3)
aluno1.setNota2(5)
print(f"O nome da aluna é {aluno1.get_nome()}, sua matriucla é {aluno1.getMatricula()} e ela foi {aluno1.media()}")

aluno2 = AlunoEnsinoMedio("Claudia")
aluno2.setMatricula(987456320)
aluno2.setNota1(10)
aluno2.setNota2(8)
print(f"O nome da aluna é {aluno2.get_nome()}, sua matriucla é {aluno2.getMatricula()} e ela foi {aluno2.media()}")


professor = Professor("Joao")
professor.setTitulacao("Doutorado")
print(f"O nome do professor é {professor.get_nome()}, e a sua titulação é {professor.getTitulacao()}")
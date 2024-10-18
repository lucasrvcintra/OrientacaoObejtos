# Atributos: titulo, autor, ano_publicacao, numero_paginas, genero
# Métodos: abrir, fechar, marcar_pagina, avancar_pagina, retroceder_pagina
# abrir(): Exibe uma mensagem indicando que o livro foi aberto.
# fechar(): Exibe uma mensagem indicando que o livro foi fechado.
# marcar_pagina(pagina): Marca a página atual do livro.
# avancar_pagina(): Avança uma página, se não estiver na última página.
# retroceder_pagina(): Retrocede uma página, se não estiver na primeira página.

class Livro:
  def __init__(self, titulo, autor, ano_publicacao, numero_paginas, genero):
    self.titulo = titulo
    self.autor = autor
    self.ano_publicacao = ano_publicacao
    self.numero_paginas = numero_paginas
    self.genero = genero
    self.pagina = 0
    self.aberto = False

  def abrir(self):
    if not self.aberto:
      self.aberto = True
      print("Livro aberto")
    else:
      print("Livro ja foi aberto")

  def fechar(self):
    if self.aberto:
      print("Livro ja foi fechado")
    else:
      self.aberto = False
      print("Livro fechado")

  def marcar_pagina(self, pagina):
    self.pagina = pagina
    print("Pagina marcada")

  def avancar_pagina(self):
    if self.pagina < self.numero_paginas:
      self.pagina += 1
      print("Avancando para a proxima pagina")

  def retroceder_pagina(self):
    if self.pagina > 0:
      self.pagina -= 1
      print("Retrocedendo para a pagina anterior")

print("Livro criado")

livro = Livro("O Hobbit", "J.R.R. Tolkien", 1937, 295, "Fantasia")
livro.abrir()
livro.fechar()
livro.marcar_pagina(50)
livro.avancar_pagina()
livro.retroceder_pagina()

print(livro.pagina)
print(livro.titulo)
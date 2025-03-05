import re

# EX 1
def iso_8601(texto):
  padrao = r'(\d{2})\/(\d{2})\/(\d{4})'
  return re.sub(padrao, r'\3-\2-\1', texto)

# EX 2
def checkNames(files):
  padrao = r'[\w\-\.]+\.\w+$'
  for file in files:
    print(file, end="")

# EX 2.1
def checkNames1(files):
  dicionario = dict()
  for file in files:
    if m := re.match(r"[\w\-\.]+(\.\w+)$",file):
      extensao = m.group(1)
      if extensao not in dicionario:
        dicionario[extensao] = []
      dicionario[extensao].append(file)

  print(dicionario)

# EX 3
def searchNames(texto):
  padrao = r'([A-Z]\w+)(?:\s[A-Z]\w+| d[oae]s?)+ ([A-Z]\w+)'
  print(re.sub(padrao, r'\2, \1', texto))

# EX 5
def filtro(abreviaturas, texto):
  for abrev, expressao in abreviaturas.items():
    texto = re.sub(rf'/abrev\{{{abrev}\}}', expressao,texto)
  print(texto)

  #OU
  texto = re.sub(r'/abrev\{(\w+)\}', lambda m: abreviaturas.get(m.group(1)),texto)




def main():
  # EX 1
  texto = """A 03/01/2022, V foi de férias com a sua família.
Ficaram hospedados num hotel e aproveitaram as férias para passear e descobrir novos locais.
Mais tarde, no dia 12/01/2022, V voltou para casa e começou a trabalhar num novo projeto.
Passou muitas horas no computador, mas finalmente terminou o projeto a 15/01/2022.

Alguns meses depois, a 26/09/2023, V casou-se com Judy e no dia 30/09/2023 partiram na
sua lua-de-mel para o local onde V tinha ido de férias no ano anterior."""
  #print(iso_8601(texto))

  # EX 2
  file_names = [
  "document.txt", # válido
  "file name.docx", # inválido
  "image_001.jpg", # válido
  "script.sh.txt", # válido
  "test_file.txt", # válido
  "file_name.", # inválido
  "my_resume.docx", # válido
  ".hidden-file.txt", # válido
  "important-file.text file", # inválido
  "file%name.jpg" # inválido
  ]
  #checkNames(file_names) 
  #checkNames1(file_names)

  # EX 3
  texto = """Este texto foi feito por Sofia Guilherme Rodrigues dos Santos, com
base no texto original de Pedro Rafael Paiva Moura, com a ajuda
do professor Pedro Rangel Henriques e do professor José João Antunes Guimarães
Dias De Almeida.
Apesar de partilharem o mesmo apelido, a Sofia não é da mesma família do famoso
autor José Rodrigues dos Santos."""
  searchNames(texto)

  #EX 5
  abreviaturas = {
    "UM": "Universidade do Minho",
    "LEI": "Licenciatura em Engenharia Informática",
    "UC": "Unidade Curricular",
    "PL": "Processamento de Linguagens"
  }

  texto = "A /abrev{UC} de /abrev{PL} é muito fixe! É uma /abrev{UC} que acrescenta muito ao curso de /abrev{LEI} da /abrev{UM}."
  filtro(abreviaturas, texto)

main()

import re

def getTexto():
  with open(r'C:\Users\Cerqueira\OneDrive\Área de Trabalho\PL\PL2025-A104188\TPC2\obras.csv', mode='r', encoding='utf-8') as file:
    texto = file.read().strip()  # Agora é uma única string

  padrao = r'([^;]+);"(.*?)";([^;]+);([^;]+);([^;]+);([^;]+);([^;\n]+)'
  matches = re.findall(padrao, texto, re.DOTALL)

  if matches:
    print(matches)
  return matches

def compositores(lista):
  compositores = []
  for obra in lista:
    compositores.append(obra[4])
  return sorted(set(compositores))

def obrasPorPeriodo(lista):
  periodos = {}
  for obra in lista:
    if obra[3] not in periodos:
      periodos[obra[3]] = 1
    else:
      periodos[obra[3]] += 1
  return periodos

def obrasPorPeriodoNome(lista):
  periodos = {}
  for obra in lista:
    if obra[3] not in periodos:
      periodos[obra[3]] = [obra[0].lstrip()]
    else:
      periodos[obra[3]].append(obra[0].lstrip())
  return periodos


def main():
  entradas = getTexto()

  #ex1
  print(compositores(entradas))
  #ex2
  print(obrasPorPeriodo(entradas))
  #ex3
  print(obrasPorPeriodoNome(entradas))


main()
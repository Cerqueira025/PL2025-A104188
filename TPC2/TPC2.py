import re

def getTexto():
  with open(r'C:\Users\Cerqueira\OneDrive\Área de Trabalho\PL\PL2025-A104188\TPC2\obras.csv', mode='r', encoding='utf-8') as file:
    texto = file.read()  # Agora é uma única string

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


def main():
  entradas = getTexto()

  print(compositores(entradas))

main()
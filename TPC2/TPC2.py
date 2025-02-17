import re

def compositores(list):
  compositores = []
  for obra in list:
    compositores.append(obra[0])
  return compositores.sort()


def getTexto():
  with open(r'C:\Users\Cerqueira\OneDrive\Área de Trabalho\PL\PL2025-A104188\TPC2\obras.csv', mode='r', encoding='utf-8') as file:
    texto = file.read().strip()

  whitespace = ' \t\n\r\x0b\x0c'
  entradas = []
  bloco = []
  i = 0
  t = ""
  for letra in texto:
    if letra != ';':
      if letra not in whitespace:
        t += letra
    else:
      bloco.append(t)
      t = ""
      i+=1
    if i == 6 and letra in whitespace:
      bloco.append(t)
      entradas.append(bloco)
      bloco = []
      t = ""
      i=0

  #print(entradas)
  return entradas

def ler_dataset():
  with open(r'C:\Users\Cerqueira\OneDrive\Área de Trabalho\PL\PL2025-A104188\TPC2\obras.csv', "r", encoding="utf-8") as file:
    texto = file.read()

def main():
  entradas = getTexto()
  #entradas = ler_dataset()
  print(entradas)

  #print(compositores(entradas))

main()

#nome;desc;anoCriacao;periodo;compositor;duracao;_id
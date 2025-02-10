import csv

def somador(texto):
  contador = 0
  i = 0
  numeros = "0123456789"
  stop = False
  while i < len(texto):
    valor = 0
    if texto[i] == '=':
      print(contador)
    if texto[i] in numeros and stop == 0:
      while texto[i] in numeros:
        valor = valor * 10 + int(texto[i])
        i +=1
      contador += valor
    if texto[i] in "Oo" and texto[i+1] in "Nn":
      stop = False
      i+=1
    if texto[i] in "Oo" and (texto[i+1] and texto[i+2]) in "Ff":
      stop = True
      i+=2
    else:
      i = i+1
  return contador

def somadorR(texto):
  contador = 0
  i = 0
  numeros = "0123456789"
  stop = False
  while i < len(texto):
    valor = 0
    if texto[i] == '=':
      print(contador)
    if texto[i] in numeros and stop == 0:
      while texto[i] in numeros:
        valor = valor * 10 + int(texto[i])
        i +=1
      contador += valor
    if texto[i] in "Oo" and texto[i+1] in "Nn":
      stop = False
      i+=1
    if texto[i] in "Oo" and (texto[i+1] and texto[i+2]) in "Ff":
      stop = True
      i+=2
    else:
      i = i+1
  return contador

def teste():
  with open('testes.csv', mode ='r', encoding="utf-8")as file:
    ficheiro = csv.reader(file)
    i = 1
    for linha in ficheiro:
        texto = linha[0]
        resultado = int(linha[1])
        if(somador(texto)!= resultado):
          print("função errada para a entrada ", i)
          print("resultado esperado: ", resultado)
          print("resultado obtido: ", somador(texto))
        i+=1


def main():
  l1 = "adgEGmesADVZomdb45dsfbgfnv"
  l2 = "dzbaSVdDVfbd2025-02-07sfba"
  l3 = "sd=svsaOFfwvsAVDsgddfbsbdb"
  l4 = "dngfSSDsf789eshREEhdh43gff"
  l5 = "ensAFdfbonabfdxs2nxggnSDGf"
  l6 = "wegaHFETSGF5ebfd=dfbxnFFFd"
  texto = l1+l2+l3+l4+l5+l6
  print("somador:")
  somador(texto)
  print("somadorR:")
  somadorR(texto)
  print("testes:")
  teste()

main()
import csv

def somador(texto):
  contador = 0
  i = 0
  numeros = "0123456789"
  stop = False
  frase = ""

  while i < len(texto):
    valor = 0
    frase += texto[i]
    if texto[i] == '=':
      print(frase)
      print(">>", contador)
      frase = ""
    if texto[i] in numeros and stop == 0:
      while texto[i] in numeros:
        valor = valor * 10 + int(texto[i])
        i +=1
        frase+=texto[i]
      contador += valor
    if texto[i] in "Oo" and texto[i+1] in "Nn":
      stop = False
      frase+=texto[i+1]
      i+=1
    if texto[i] in "Oo" and (texto[i+1] and texto[i+2]) in "Ff":
      stop = True
      frase+=texto[i+1]
      i+=2
    else:
      i = i+1
  print(frase)
  print(">>", contador)
  return contador

def teste():
  with open(r'C:\Users\Cerqueira\OneDrive\Área de Trabalho\PL\PL2025-A104188\TPC1\testes.csv', mode ='r', encoding="utf-8")as file:
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
  texto =(
    "adgEGmesADVZomdb45dsfbgfnv"
    "dzbaSVdDVfbd2025-02-07sfba"
    "sd=svsaOFfwvsAVDsgddfbsbdb"
    "dngfSSDsf789eshREEhdh43gff"
    "ensAFdfbonabfdxs2nxggnSDGf"
    "wegaHFETSGF5ebfd=dfbxnFFFd"
  )
  print("somador:")
  somador(texto)

  with open(r'C:\Users\Cerqueira\OneDrive\Área de Trabalho\PL\PL2025-A104188\TPC1\texto1.txt', mode ='r', encoding="utf-8")as file:
      texto1 = file.read()
  print("\nsomador:")
  somador(texto1)

  print("\ntestes:")
  teste()

main()
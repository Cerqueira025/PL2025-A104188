import json
import re



def listar(stock):
  print("cod     |  nome                 |  quantidade |  preço")
  print("------------------------------------------------------")
  for prod in stock:
    print(f"{prod['cod']}       {prod['nome']:<20}       {prod['quant']:<5}       {prod['preco']}")

def moeda(moedas):
  valores = re.findall(r'(\d+[ec])', moedas)
  cent = 0
  euro = 0
  for valor in valores:
    if valor in '2e1e50c20c10c5c2c1c':
      if valor[-1] == 'e':
        euro+=int(valor[:-1])
      elif valor[-1] == 'c':
        cent+=int(valor[:-1])
      else:
        pass
    else:
      print("Moeda "+valor+" inválida")
  if cent >= 100:
    euro+=cent//100
    cent=cent%100
  return euro,cent

def main():
  #leitura de dados do ficheiro
  with open(r"C:\Users\Cerqueira\OneDrive\Área de Trabalho\PL\PL2025-A104188\TPC5\stock.json", mode='r', encoding="utf-8") as f:
    stock = json.load(f)
  
  user = True
  while user:
    inp = input()
    if inp == 'listar':
      listar(stock)
    if 'MOEDAS' in inp:
      print(moeda(inp))
    if inp == 'q':
      user = False

      
  

main()
import json
from datetime import date
import re



def listar(stock):
  print("cod     |  nome                 |  quantidade |  preço")
  print("------------------------------------------------------")
  for prod in stock:
    print(f"{prod['cod']}       {prod['nome']:<20}       {prod['quant']:<5}       {prod['preco']}")



def moedas(moedas, saldo):
  valores = re.findall(r'(\d+[ec])', moedas)
  saldo = tuplaToFloat(saldo)
  moedas_validas = {
        '2e': 2.00, '1e': 1.00, '50c': 0.50, '20c': 0.20, '10c': 0.10,
        '5c': 0.05, '2c': 0.02, '1c': 0.01
  }
  for valor in valores:
    if valor in moedas_validas:
      saldo += moedas_validas[valor]
    else:
      print("Moeda "+valor+" inválida")

  return floatToTupla(saldo)



def selec(stock, inp, saldo):
  match = re.search(r'SELECIONAR (\w\d\d)', inp)
  #código inválido
  if not match:
    print("maq: Código de produto inválido.")
    return stock, saldo
  
  cod = match.group(1)
  #produto não existe
  if cod not in stock:
    print("maq: Produto não encontrado.")
    return stock, saldo
  #produto esgotado
  if stock[cod]['quant'] <= 0:
    print(f"maq: Produto {stock[cod]['nome']} esgotado.")
    return stock, saldo

  custo = stock[cod]['preco']
  saldo = tuplaToFloat(saldo)
  
  if saldo >= custo:
    saldo-=custo
    saldo = floatToTupla(saldo)
    stock[cod]['quant']-=1
    print(f'maq:  Pode retirar o produto dispensado {stock[cod]["nome"]}')
    print(f'maq: Saldo = {saldo[0]}e {saldo[1]}c')
  else:
    saldo = floatToTupla(saldo)
    custo = floatToTupla(custo)
    print(f'maq: Saldo insufuciente para satisfazer o seu pedido')
    print(f'maq: Saldo = {saldo[0]}e {saldo[1]}c; Pedido = {custo[0]}e {custo[1]}c')

  return stock, saldo



def troco(saldo):
  saldo = tuplaToFloat(saldo)
  moedas_validas = {
        '2e': 2.00, '1e': 1.00, '50c': 0.50, '20c': 0.20, '10c': 0.10,
        '5c': 0.05, '2c': 0.02, '1c': 0.01
    }
  troco = []
  
  for moeda, valor in moedas_validas.items():
    count=0
    while saldo >= valor:
      saldo = round(saldo - valor, 2)
      count+=1
    if count>0:
      troco.append((moeda, count))

  troco_t = ", ".join(f"{c}x {m}" for m, c in troco)
  return troco_t + "."

#FUNÇÕES PARA CONTROLAR SALDO
def tuplaToFloat(a):
  return round(a[0]+a[1]/100,2)

def floatToTupla(a):
  euros = int(a)
  centimos = int(round((a - euros) * 100))
  return euros,centimos


def main():
  caminho_ficheiro = r"C:\Users\Cerqueira\OneDrive\Área de Trabalho\PL\PL2025-A104188\TPC5\stock.json"
  #leitura de dados do ficheiro
  with open(caminho_ficheiro, mode='r', encoding="utf-8") as f:
    stock_l = json.load(f)
  
  #Converte a lista para dicionário
  stock = {p['cod']: p for p in stock_l}
  saldo = (0,0)
  user = True

  print(f"maq: {date.today()}, Stock carregado, Estado atualizado.")
  print("maq: Bom dia. Estou disponível para atender o seu pedido.")

  while user:
    inp = input(">> ")

    if inp == 'LISTAR':
      listar(stock.values())

    if inp == 'SALDO':
      print(f"Saldo: {saldo[0]}e {saldo[1]}c")

    if inp.startswith('MOEDAS'):
      saldo = moedas(inp, saldo)
      print(f'maq: Saldo = {saldo[0]}e {saldo[1]}c')

    if inp.startswith('SELECIONAR'):
      stock, saldo = selec(stock, inp, saldo)
    
    if inp == 'SAIR':
      print(f"maq: Pode retirar o troco: {troco(saldo)}")
      stock_l = list(stock.values()) #atualizar a lista original
      with open(caminho_ficheiro, 'w', encoding='utf-8') as f:
        json.dump(stock_l, f, ensure_ascii=False, indent=4)
      print("maq: Até à próxima")
      user = False


main()
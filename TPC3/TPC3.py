import re

## Titulos
def titulos(text):
  padrao = r'^(#+) (.*)'
  matches = re.search(padrao, text)
  if not matches:
    return text
  i = len(matches.group(1))
  return "<h"+ str(i) +">"+ matches.group(2)+ "</h"+str(i)+">"+'\n'

## Bold
def bold(text):
  return "<b>"+ text.strip()+ "</b>" 

## Italico
def italico(text):
  return "<i>"+ text.strip()+ "</i>" 

####################
# FUNCAO PRINCIPAL #
####################
def markDownToHTML(text):
  n_text = ""
  for linha in text:
    #print("Linha: "+ linha)
    if not linha:  # Se a linha estiver vazia
      continue
    
    #Titulos
    if linha[0] == "#":
      n_text += titulos(linha)

    if linha[0] == "*":
      #bold
      if len(linha) > 1 and linha[1] =="*":
        n_text += bold(linha)
      #italico
      else:
        n_text += italico(linha)
  return n_text

def main():
  with open(r'C:\Users\Cerqueira\OneDrive\Área de Trabalho\PL\regex.md', mode='r', encoding='utf-8') as file:
    text = file.read().splitlines()
  print(markDownToHTML(text))

main()

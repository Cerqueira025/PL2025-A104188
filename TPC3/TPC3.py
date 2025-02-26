import re

## Titulos
def titulos(text):
  padrao = r'^(#+) (.*)'
  matches = re.search(padrao, text)
  if not matches:
    return text
  i = len(matches.group(1))
  return "<h"+ str(i) +">"+ matches.group(2)+ "</h"+str(i)+">"

## Listas
#def listas(text, i, n_text):


## Bold
def bold(text):
  padrao = r'\*\*([^\*]+)\*\*'
  return re.sub(padrao, r'<b>\1</b>', text) 

## Italico
def italico(text):
  padrao = r'\*([^\*]+)\*'
  return re.sub(padrao, r'<i>\1</i>', text) 

####################
# FUNCAO PRINCIPAL #
####################
def markDownToHTML(text):
  n_text = ""
  i = 0
  while(i<len(text)):
    linha = text[i]
    
    #Linha vazia
    if not linha:
      i+=1
      n_text+='\n'
      continue
    
    #Titulos
    if linha[0] == "#":
      n_text += titulos(linha) +'\n'

    #Bold
    if "**" in linha:
      print(linha)
      n_text += bold(linha) +'\n'
    #Italico
    elif "*" in linha:
      n_text += italico(linha) +'\n'
    
    i+=1
  return n_text

def main():
  with open(r'C:\Users\Cerqueira\OneDrive\Área de Trabalho\PL\regex.md', mode='r', encoding='utf-8') as file:
    text = file.read().splitlines()
  print("\nRESULTADO:\n" + markDownToHTML(text))

main()

import re

## Titulos
def titulos(text):
  padrao = r'^(#+) (.*)'
  matches = re.search(padrao, text)
  if not matches:
    return text
  i = len(matches.group(1))
  return "<h"+ str(i) +">"+ matches.group(2)+ "</h"+str(i)+">"

## Bold
def bold(text):
  padrao = r'\*\*([^\*]+)\*\*'
  return re.sub(padrao, r'<b>\1</b>', text) 

## Italico
def italico(text):
  padrao = r'\*([^\*]+)\*'
  return re.sub(padrao, r'<i>\1</i>', text) 

## Listas
def listas(text, i, n_text):
  n_text += "<ol>\n"
  
  while(i < len(text)):
    padrao = r'^[\s]*\d.\s*(.*)'
    match = re.search(padrao, text[i].strip()) 
    if not match:
      break
    n_text += "<li>"+ match.group(1)+"</li>\n" 
    i+=1
  print("Saí do loop!\n")
  n_text += "</ol>\n"
  return i, n_text

##Link
def link(text):
  padrao = r'\[([^\\]*)\]\(([^\)]*)\)'
  return re.sub(padrao, r'<a href="\2">\1</a>', text)

##Imagem
def imagem(text):
  padrao = r'\!\[([^\\]*)\]\(([^\)]*)\)'
  return re.sub(padrao, r'<img src="\2" alt="\1"/>', text)

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
      n_text += bold(linha) +'\n'
    #Italico
    elif "*" in linha:
      n_text += italico(linha) +'\n'

    #Lista
    if "1." in linha:
      i , n_text = listas(text, i, n_text)

    #Imagem
    if "![" in linha:
      n_text += imagem(linha) + '\n'
    #Link
    elif "[" in linha:
      n_text += link(linha) + '\n'
    
    i+=1
  return n_text

def main():
  with open(r'C:\Users\Cerqueira\OneDrive\Área de Trabalho\PL\PL2025-A104188\regex.md', mode='r', encoding='utf-8') as file:
    text = file.read().splitlines()
  print("\nRESULTADO:\n" + markDownToHTML(text))

main()

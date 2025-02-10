import csv
import json

#func que eleva uma base a um dado expoente
def exp(base, exp):
  result = 1
  while exp > 0:
    result*=base
    exp-=1
  return result

#retorna o maior elem de uma lista
def maior(list):
  maior = 0
  for l in list:
    if maior < l:
      maior = l
  return maior

#fazer duas listas a partir de uma lista de tuplos
def make2L(list):
  l1 = []
  l2 = []
  for (p1,p2) in list:
    l1.append(p1)
    l2.append(p2)

  print("lista 1: ", l1)
  print("lista 2: ", l2)

  return l1

#lê um número inteiro positivo e cria um dicionário 
# com chaves de 1 até esse número, em que o valor 
# associado a cada chave é o quadrado dessa chave.

def makeDic():
  v = int(input("introduz um valor: "))
  d = {}
  num = 1
  while num < v:
    d[num]=num*num
    num+=1
  return d

#1.1
def lerEntradas():
  with open('alunos.csv', mode ='r', encoding="utf-8")as file:
    ficheiro = csv.reader(file)
    for linha in ficheiro:
        print(linha)

#1.2
def countLines():
  with open('alunos.csv', mode ='r', encoding="utf-8")as file:
    ficheiro = csv.reader(file)
    numLinhas = len(list(ficheiro))
  return numLinhas

#1.3
#{id_aluno : (notas:[TPC1,TPC,TPC3,TPC4], nome:"NOME", curso:"CURSO")}
def makeDicAluno():
  d = {}
  with open('alunos.csv', mode ='r', encoding="utf-8")as file:
    ficheiro = csv.reader(file)
    for linha in ficheiro:
      id_aluno = linha[0]
      nome = "nome: " + linha[1]
      curso = "curso: " + linha[2]
      notas = [linha[3], linha[4], linha[5], linha[6]]
      d[id_aluno] = (notas, nome, curso)
    return d
  
#3.1
#alunos com melhor média
def bestM(dic):
  bestM = 0
  for key in dic.keys():
    notas, nome, curso = dic[key]
    notas = [int(nota) for nota in notas if nota.isdigit()]
    media = sum(notas)/4
    if media > bestM:
      bestM = media
  return bestM

#3.2
#alunos de LEI com média > 15
def leiStudents(dic):
  leiStudents = []
  for key in dic.keys():
    notas, nome, curso = dic[key]
    if curso == "curso: LEI":
      notas = [int(nota) for nota in notas if nota.isdigit()]
      media = sum(notas)/4
      if media > 15: 
        leiStudents.append(nome)
  return leiStudents

#2.1
def cinemaDic():
  with open("cinemaATP.json", mode='r', encoding="utf-8") as f:
    dados = json.load(f) 
  d = {}
  for filme in dados:
    title = filme.get("title", "Título Desconhecido")
    # title = filme["title"]
    year = filme.get("year", "Ano Desconhecido")
    castL = filme.get("cast", [])
    genresL = filme.get("genres", [])
          
    d[title] = (year, castL, genresL)      
    
  #print(d)
  return(d)

#2.2
#consultar todos os filmes com 'office' no nome
def search(dic):
  list = []
  for title in dic.keys():
    if "28" in title.lower():
      list.append(title)
  return list

#ordem alfabética
def ord(dic):
  lista = list(dic.keys())
  return sorted(lista)

#filmes por genero
def gen(dic, gen):
  list = []
  for title in dic.keys():
    (year, castL, genresL) = dic[title]
    if gen in genresL:
      list.append(title)
  return list
  

def main():
  print("exp: ", exp(2, 3))
  print("maior: ", maior([1,6,3,9,2]))

  print("make2L")
  lista = [(1, "banana"), (2, "maçã"), (3, "melancia"), (4, "cereja")]
  make2L(lista)

  #print("makeDic: ", makeDic())

  #print("lerEntradas: ")
  #lerEntradas()
  print("O ficheiro tem ", countLines(), " linhas")
  alunosDic = makeDicAluno()
  print(alunosDic)
  print(bestM(alunosDic))
  print(leiStudents(alunosDic))

  cinDic = cinemaDic()
  #print("Os filmes com'28' no nome: ", search(cinDic))
  #print(ord(cinDic))
  print(gen(cinDic, "Science Fiction"))

main()
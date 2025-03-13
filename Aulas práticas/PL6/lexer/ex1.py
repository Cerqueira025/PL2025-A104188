import ply.lex as lex

frase_exemplo = """x=a+1
                  b=2
                  a = b-1
                  a*=2"""

tokens = (
  "NUMBER",
  "CHAR",
  "EQUALS", # =
  "OPERADOR",
  "NEWLINE"
)

operadores = {
  'add' : 'ADD',
  'sub' : 'SUB',
  'mult' : 'MULT',
  'div' : 'DIV'
}

t_ADD = r'\+'
t_SUB = r'\-'
t_MULT = r'\*'
t_DIV = r'\\'

def t_CHAR(t):
  r'\w+'
  print(f"variavel {t.value}")
  return t

def t_NUMBER(t):
  r'\d+'
  t.value = int(t.value)
  return t

t_ignore = ' \t\n'

def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)

lexer = lex.lex()

while r := lexer.token():
  print(r)

def main():
  read = True
  while(read):
    inp = input(">> ")
    if inp == "STOP":
      read = False
    else:
      lexer.input(inp)
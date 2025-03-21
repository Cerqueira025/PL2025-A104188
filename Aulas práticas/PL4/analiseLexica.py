import ply.lex as lex

frase_exemplo = "3 * (5 + 2)"

tokens = (
  "NUMBER",
  "ADD", # +
  "SUB", # -
  "MULT", # *
  "DIV", # /
  "AP", # (
  "FP" # )
)

t_ADD = r'\+'
t_SUB = r'\-'
t_MULT = r'\*'
t_DIV = r'\\'
t_AP = r'\('
t_FP = r'\)'

def t_NUMBER(t):
  r'\d+'
  t.value = int(t.value)
  return t

t_ignore = ' \t\n'

def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)

lexer = lex.lex()

lexer.input(frase_exemplo)

while r := lexer.token():
  print(r)
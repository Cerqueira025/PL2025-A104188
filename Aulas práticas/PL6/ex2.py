import ply.lex as lex

tokens = (
  "PALAVRA",
  "INT",
  "FLOAT",
  "BOOL",
  "AL", #[
  "FL", #]
  "VIRGULA"
)

t_PALAVRA = r'\w+'
t_AL = r'\['
t_FL = r'\]'
t_VIRGULA = r'\,'

def t_BOOL(t):
  r'True|False'
  return t

def t_FLOAT(t):
  r'\d+\.\d+'
  t.value = float(t.value)
  return t

def t_INT(t):
  r'\d+'
  t.value = int(t.value)
  return t

t_ignore = ' \t\n'

def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)

lexer = lex.lex()

lexer.input(frase_de_input)

while r := lexer.token():
  print(r)

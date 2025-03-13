import ply.lex as lex

frase_de_input = "Bom dia! Hoje é dia 13 de março, do ano 2025..."

tokens = (
  "PALAVRA",
  "VIRGULA",
  "PONTOFINAL",
  "PONTOINTERROG",
  "PONTOEXCL",
  "RETICENCIAS"
)

t_PALAVRA = r'\w+'
t_VIRGULA = r'\,'
t_PONTOFINAL = r'\.'
t_PONTOINTERROG = r'\?'
t_PONTOEXCL = r'\!'
t_RETICENCIAS = r'\.\.\.'

t_ignore = ' \t\n'

def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)

lexer = lex.lex()

lexer.input(frase_de_input)

while r := lexer.token():
  print(r)

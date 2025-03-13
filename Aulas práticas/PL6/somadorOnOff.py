import ply.lex as lex

states = (
    ('on', 'inclusive'),
    ('off', 'inclusive')
)

tokens = (
    'PALAVRA',
    'NUMERO',
    'ON',
    'OFF',
    'IGUAL',
    'SIMBOLO'
)

t_IGUAL = r'='
t_SIMBOLO = r'[\,\-\+\\\!\.]'

def t_ON(t):
  r'[oO][Nn]'
  t.lexer.begin('on')
  return t

def t_OFF(t):
  r'[oO][fF][fF]'
  t.lexer.begin('off')
  return t

def t_NUMERO(t):
  r'\d+'
  t.value = int(t.value)
  return t

def t_off_NUMERO(t):
  r'\d+'
  return None

def t_PALAVRA(t):
  r'\w+'
  t.value = len(t.value)
  return t

def t_on_PALAVRA(t):
  r'\w+'
  t.value = len(t.value)
  return t

def t_off_PALAVRA(t):
  r'\w+'
  return None

t_ignore = ' \t\n'
t_on_ignore = ' \t\n'
t_off_ignore = ' \t\n'

def t_ANY_error(t):
    print(f"Carácter ilegal: {t.value[0]}")
    t.lexer.skip(1)


data = '''
Hoje, 7 de Fevereiro de 2025, o professor de Processamento de Linguagens
deu-nos este trabalho para fazer.=OfF
E deu-nos 7= dias para o fazer...ON
Cada trabalho destes vale 0.25 valores da nota final!
'''

lexer = lex.lex()

lexer.stack = list()

lexer.input(data)

soma = 0
while tok := lexer.token():
  if tok.type in ('NUMERO', 'PALAVRA'):
    soma += tok.value

print("Soma dos valores:", soma)

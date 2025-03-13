import ply.lex as lex
# List of token names. This is always required
toks = ('VAR',
        'OPENP',
        'CLOSEP',
        'DOT',
        'SEMICOLON',
        'STRING',
        'URI',
        'KEYWORD',
        'NUMBER',
        'ID',
        'ERRO')

reserved = {
  'select' : 'SELECT',
  'where' : 'WHERE',
  'LIMIT' : 'LIMIT'
}

tokens = toks + tuple(reserved.values())

t_VAR = r'\?\w+'
t_OPENP = r'\{'
t_CLOSEP = r'\}'
t_DOT = r'\.'
t_SEMICOLON = r'\;'
t_STRING = r'"[^"]+"(?:@\w+)?'

def t_NUMBER(t):
  r'\d+'
  t.value = int(t.value)
  return t

def t_URI(t):
  r'\w+:\w+'
  return t

def t_ID(t):
  r'[a-zA-Z_][a-zA-Z_0-9]*'
  t.type = reserved.get(t.value,'ID')
  return t

t_ignore = ' \t\n'

def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)
  
lexer = lex.lex()
  
code = '''select ?nome ?desc where { 
    ?s a dbo:MusicalArtist. 
    ?s foaf:name "Chuck Berry"@en . 
    ?w dbo:artist ?s. 
    ?w foaf:name ?nome. 
    ?w dbo:abstract ?desc 
} LIMIT 1000'''

lexer.input(code)
for tok in lexer:
    print(tok)
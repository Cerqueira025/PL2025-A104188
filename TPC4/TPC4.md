# Analisador Léxico

Para a costrução deste programa foi utilizado **PLY (Python Lex-Yacc)**. O objetivo do analisador é identificar e categorizar tokens numa linguagem de consulta semelhante ao **SPARQL**.

---

## 1. Definição de Tokens

A variável `toks` contém uma tupla com os nomes dos tokens que serão reconhecidos pelo lexer:

```python
toks = ('VAR', 'OPENP', 'CLOSEP', 'DOT', 'SEMICOLON', 'STRING', 'URI', 'KEYWORD', 'NUMBER', 'ID', 'ERRO')
```

### Tokens Reservados

Palavras-chave (ou **tokens reservados**) são definidos em um dicionário chamado `reserved`:

```python
reserved = {
  'select' : 'SELECT',
  'where' : 'WHERE',
  'LIMIT' : 'LIMIT'
}
```

A lista final de tokens é formada pela junção de `toks` e os valores do dicionário `reserved`:

```python
tokens = toks + tuple(reserved.values())
```

---

## 2. Regras de Reconhecimento de Tokens

Cada token é definido por uma expressão regular. As regras simples são definidas diretamente por variáveis iniciadas com `t_`. Por exemplo:

```python
t_VAR = r'\?\w+'
```

### Tokens Simples

- **`VAR`**: Reconhece variáveis que começam com `?` seguidas por caracteres alfanuméricos.
- **`OPENP`**: Reconhece o caractere `{`.
- **`CLOSEP`**: Reconhece o caractere `}`.
- **`DOT`**: Reconhece o caractere `.`.
- **`SEMICOLON`**: Reconhece o caractere `;`.

### Tokens com Funções Especiais

#### 1. `t_NUMBER`
Converte números em inteiros:

```python
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t
```

#### 2. `t_URI`
Reconhece URIs no formato `prefixo:sufixo`:

```python
def t_URI(t):
    r'\w+:\w+'
    return t
```

#### 3. `t_ID`
Identifica identificadores genéricos e palavras reservadas:

```python
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t
```
Se o valor do token corresponder a uma palavra reservada (ex: `select`), será classificado como tal. Caso contrário, será considerado um `ID` comum.

### Ignorar Espaços

O comando abaixo faz com que o lexer ignore espaços em branco, tabulações e quebras de linha:

```python
t_ignore = ' \t\n'
```

### Tratamento de Erros

Quando um caractere inválido é encontrado, ele é ignorado e uma mensagem de erro é exibida:

```python
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
```

---

## 3. Construção do Lexer

O lexer é construído com a chamada:

```python
lexer = lex.lex()
```

---

## 4. Teste do Lexer

A variável `code` contém um exemplo de entrada no formato de uma consulta SPARQL simplificada:

```python
code = '''select ?nome ?desc where {
    ?s a dbo:MusicalArtist.
    ?s foaf:name "Chuck Berry"@en .
    ?w dbo:artist ?s.
    ?w foaf:name ?nome.
    ?w dbo:abstract ?desc
} LIMIT 1000'''
```

A entrada é passada para o lexer através do método `input()`:

```python
lexer.input(code)
```

Os tokens reconhecidos são impressos em um loop:

```python
for tok in lexer:
    print(tok)
```

---

## 5. Saída Esperada

A saída do programa imprime os tokens reconhecidos, por exemplo:

```
LexToken(SELECT,'select',1,0)
LexToken(VAR,'?nome',1,7)
LexToken(VAR,'?desc',1,13)
LexToken(WHERE,'where',1,19)
LexToken(OPENP,'{',1,25)
LexToken(VAR,'?s',2,31)
LexToken(ID,'a',2,34)
LexToken(URI,'dbo:MusicalArtist',2,36)
...
```

Cada linha representa um token com o seguinte formato:

```
LexToken(<TIPO>, '<VALOR>', <LINHA>, <POSIÇÃO>)
```

Por exemplo:

```
LexToken(URI,'dbo:MusicalArtist',2,36)
```
Indica que um token do tipo `URI` com o valor `dbo:MusicalArtist` foi encontrado na linha 2, posição 36.

---
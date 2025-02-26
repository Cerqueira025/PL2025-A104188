# SINTAXE REGEX

## 1. Metacaracteres (Devem ser antecedidos de `\` se usados literalmente)
```
. ^ $ * + ? { } [ ] \ | ( )
```
  1. \.
  2. \^
  3. \$
  4. \+

## 2. Classes de Caracteres
| *Classe* | *Descrição* |
|--------|------------|
| `.` | Qualquer caractere (exceto nova linha) |
| `[abc]` | Qualquer caractere dentro dos colchetes |
| `[^abc]` | Qualquer caractere **exceto** os dentro dos colchetes |
| `[a-z]` | Qualquer caractere entre `a` e `z` |
| `\d` | Dígitos (`0-9`) |
| `\D` | Não dígitos |
| `\w` | Palavras (`a-z`, `A-Z`, `0-9`, `_`) |
| `\W` | Não palavras |
| `\s` | Espaço em branco (espaço, tab, nova linha) |
| `\S` | Não espaço em branco |

## 3. Quantificadores
| Quantificador | Descrição |
|--------------|-----------|
| `*` | 0 ou mais ocorrências |
| `+` | 1 ou mais ocorrências |
| `?` | 0 ou 1 ocorrência |
| `{n}` | Exatamente `n` ocorrências |
| `{n,}` | Pelo menos `n` ocorrências |
| `{n,m}` | Entre `n` e `m` ocorrências |

## 4. Grupos e Capturas
| Sintaxe | Descrição | Chamada |
|---------|------------|------------|
| `(abc)` | Grupo capturador | match.group(1) |
| `(?:abc)` | Grupo **não capturador** | Não pode ser acedido |
| `(?P<nome>abc)` | Grupo **nomeado** | match.group("nome") |
| `\1, \2` | Indicam grupos capturados anteriormente | r"(\b\w+\b) \1" |

## 5. Alternância (OU lógico)
 `a|b` Corresponde a `a` **ou** `b`

## 6. Lookarounds (Verificação sem Captura)
| Síntaxe | Descrição |
|---------|------------|
| `(?=abc)` | Lookahead positivo (segue-se `abc`) |
| `(?!abc)` | Lookahead negativo (não segue-se `abc`) |
| `(?<=abc)` | Lookbehind positivo (precedido por `abc`) |
| `(?<!abc)` | Lookbehind negativo (não precedido por `abc`) |

## NOTAS:
  ```
  padrao = r'^(#+) (.*)'
  re.findall(padrao, text)
  >>[(a,b),(c,d)]
  ```
  Retorna uma **lista** de todas as ocorrências no **'text'** dos grupos de captura


## Links 
 Aqui está o link para o caderno da UC: [caderno da UC](https://docs.google.com/document/d/16ajGsYV70V3rO7IiPGfqfwc89R95miCqW1q-CVaGcB0/edit?tab=t.0#heading=h.ne5koqb48aes)

## Imagens
Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com)
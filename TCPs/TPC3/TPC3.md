# Conversor de Markdown para HTML em Python

O programa desenvolvido constitui a base de um conversor de Markdown para HTML.
O código está organizado em diferentes funções, cada uma responsável por converter um elemento específico.

### 1. Títulos
```python
## Titulos
def titulos(text):
  padrao = r'^(#+) (.*)'
  matches = re.search(padrao, text)
  if not matches:
    return text
  i = len(matches.group(1))
  return "<h"+ str(i) +">"+ matches.group(2)+ "</h"+str(i)+">"
```
Esta função:
- Deteta títulos que começam com `#`.
- Converte-os para `<h1>`, `<h2>`, ..., `<h6>` dependendo do número de `#`.

### 2. Texto em Negrito
```python
## Bold
def bold(text):
  padrao = r'\*\*([^\*]+)\*\*'
  return re.sub(padrao, r'<b>\1</b>', text)
```
Esta função:
- Procura texto entre `** **` e substitui por `<b></b>`.

### 3. Texto em Itálico
```python
## Italico
def italico(text):
  padrao = r'\*([^\*]+)\*'
  return re.sub(padrao, r'<i>\1</i>', text)
```
Esta função:
- Procura texto entre `* *` e substitui por `<i></i>`.

### 4. Listas Numeradas
```python
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
  
  n_text += "</ol>\n"
  return i, n_text
```
Esta função:
- Deteta listas numeradas (ex: `1. Item`), converte para `<ol><li>Item</li></ol>`.

### 5. Links
```python
## Link
def link(text):
  padrao = r'\[([^\\]*)\]\(([^\)]*)\)'
  return re.sub(padrao, r'<a href="\2">\1</a>', text)
```
Esta função:
- Deteta links no formato `[texto](url)` e substitui por `<a href="url">texto</a>`.

### 6. Imagens
```python
## Imagem
def imagem(text):
  padrao = r'\!\[([^\\]*)\]\(([^\)]*)\)'
  return re.sub(padrao, r'<img src="\2" alt="\1"/>', text)
```
Esta função:
- Deteta imagens no formato `![alt](url)` e converte para `<img src="url" alt="alt"/>`.

### 7. Função Principal `markDownToHTML`
```python
def markDownToHTML(text):
  n_text = ""
  i = 0
  while(i<len(text)):
    linha = text[i]
    
    # Linha vazia
    if not linha:
      i+=1
      n_text+='\n'
      continue
    
    # Titulos
    if linha[0] == "#":
      n_text += titulos(linha) +'\n'

    # Bold
    if "**" in linha:
      n_text += bold(linha) +'\n'
    # Italico
    elif "*" in linha:
      n_text += italico(linha) +'\n'

    # Lista
    if "1." in linha:
      i , n_text = listas(text, i, n_text)

    # Imagem
    if "![" in linha:
      n_text += imagem(linha) + '\n'
    # Link
    elif "[" in linha:
      n_text += link(linha) + '\n'
    
    i+=1
  return n_text
```
Esta função:
- Percorre o texto linha por linha.
- Aplica as funções necessárias para converter os elementos Markdown para HTML.

### 8. Função `main`
```python
def main():
  with open(r'C:\Users\Cerqueira\OneDrive\Área de Trabalho\PL\PL2025-A104188\regex.md', mode='r', encoding='utf-8') as file:
    text = file.read().splitlines()
  print("\nRESULTADO:\n" + markDownToHTML(text))
```
Esta função:
- Lê um ficheiro Markdown.
- Converte-o para HTML usando `markDownToHTML`.
- Imprime o resultado.

## Exemplo de Uso
Se o ficheiro Markdown contiver:
```markdown
# Título Principal
## Subtítulo
Texto normal com **negrito** e *itálico*.

1. Item 1
2. Item 2

[Google](https://www.google.com)

![Imagem](https://www.example.com/imagem.png)
```
A saída HTML será:
```html
<h1>Título Principal</h1>
<h2>Subtítulo</h2>
Texto normal com <b>negrito</b> e <i>itálico</i>.

<ol>
<li>Item 1</li>
<li>Item 2</li>
</ol>

<a href="https://www.google.com">Google</a>

<img src="https://www.example.com/imagem.png" alt="Imagem"/>
```

---

Este código permite converter um ficheiro Markdown para HTML, interpretando títulos, negrito, itálico, listas, links e imagens automaticamente!


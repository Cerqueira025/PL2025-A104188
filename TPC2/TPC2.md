# Explicação do Código

O código lê um ficheiro CSV que contém informações sobre obras, extrai os dados usando expressões regulares e realiza operações sobre esses dados.

## 1. Função `getTexto()`

- **Objetivo**: Lê o ficheiro `obras.csv` e extrai os dados usando uma expressão regular.
- **Processo**:
  1. Abre e lê o ficheiro como uma string.
  2. Usa a regex `([^;]+);"(.*?)";([^;]+);([^;]+);([^;]+);([^;]+);([^;\n]+)` para dividir os campos.
  3. Retorna os dados extraídos como uma lista de tuplos.

## 2. Função `compositores(lista)`

- **Objetivo**: Retornar uma lista ordenada de compositores sem repetições.
- **Processo**:
  1. Itera sobre a lista de obras e extrai o nome do compositor (posição 4 do tuplo).
  2. Usa `set()` para remover duplicatas.
  3. Ordena os compositores por ordem alfabética.

## 3. Função `obrasPorPeriodo(lista)`

- **Objetivo**: Conta quantas obras pertencem a cada período.
- **Processo**:
  1. Itera sobre a lista de obras.
  2. Usa um dicionário para contar a frequência de cada período (posição 3 do tuplo).
  3. Retorna um dicionário onde a chave é o período e o valor é a contagem de obras.

## 4. Função `obrasPorPeriodoNome(lista)`

- **Objetivo**: Organiza as obras por período musical.
- **Processo**:
  1. Itera sobre a lista de obras.
  2. Usa um dicionário onde a chave é o período e o valor é uma lista com os nomes das obras (posição 0 do tuplo).
  3. Retorna um dicionário com os períodos e as suas respetivas listas de obras.

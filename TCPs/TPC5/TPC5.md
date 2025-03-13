# Máquina de Vendas Automática

## 📋 Estrutura do Programa

### 1. Função `listar(stock)`

**Objetivo**: Imprime no terminal a lista de produtos disponíveis na máquina.

**Parâmetros**:
- `stock`: Lista de dicionários que representa o inventário de produtos.

**Saída**: Exibe os produtos formatados com código, nome, quantidade e preço.

---

### 2. Função `moedas(moedas, saldo)`

**Objetivo**: Atualiza o saldo da máquina com base nas moedas inseridas pelo utilizador.

**Parâmetros**:
- `moedas`: String com as moedas introduzidas (ex: 'MOEDAS 1e 50c').
- `saldo`: Tupla representando o saldo atual (euros, cêntimos).

**Retorna**: Uma tupla com o novo saldo (euros, cêntimos).

**Validações**:
- Apenas são aceites moedas válidas: `2e`, `1e`, `50c`, `20c`, `10c`, `5c`, `2c`, `1c`.
- Moedas inválidas são reportadas no terminal.

---

### 3. Função `selec(stock, inp, saldo)`

**Objetivo**: Permite ao utilizador selecionar um produto pelo código e atualiza o saldo e o stock.

**Parâmetros**:
- `stock`: Dicionário representando o inventário da máquina.
- `inp`: String com o comando de seleção (ex: 'SELECIONAR A01').
- `saldo`: Tupla com o saldo atual (euros, cêntimos).

**Validações**:
- Verifica se o código do produto é válido.
- Informa se o produto está esgotado.
- Se o saldo for insuficiente, apresenta a diferença.

**Retorna**: O stock atualizado e o novo saldo.

---

### 4. Função `troco(saldo)`

**Objetivo**: Calcula e retorna o troco a ser devolvido ao utilizador.

**Parâmetros**:
- `saldo`: Tupla com o saldo atual (euros, cêntimos).

**Retorna**: Uma string indicando a quantidade de cada moeda a ser devolvida.

---

### 5. Função `tuplaToFloat(a)`

**Objetivo**: Converte um saldo representado por uma tupla `(euros, cêntimos)` em um valor `float`.

**Parâmetros**:
- `a`: Tupla representando o saldo.

**Retorna**: Um valor em `float`.

---

### 6. Função `floatToTupla(a)`

**Objetivo**: Converte um valor `float` para uma tupla `(euros, cêntimos)`.

**Parâmetros**:
- `a`: Valor em `float`.

**Retorna**: Uma tupla `(euros, cêntimos)`.

---

## 🚀 Função `main()`

**Objetivo**: Controla o fluxo principal do programa.

### Passos principais:
1. **Carregar Stock**: Lê o ficheiro JSON contendo o inventário dos produtos.
2. **Interface do Utilizador**: Aceita comandos até o utilizador digitar `SAIR`.

### Comandos Disponíveis:
- `LISTAR`: Mostra a lista de produtos disponíveis.
- `SALDO`: Apresenta o saldo atual.
- `MOEDAS <valor>`: Adiciona moedas ao saldo (ex: `MOEDAS 1e 50c`).
- `SELECIONAR <código>`: Seleciona um produto pelo código (ex: `SELECIONAR A01`).
- `SAIR`: Termina o programa e devolve o troco.

### Estado Atualizado:
- Ao encerrar, o stock atualizado é guardado novamente no ficheiro JSON.

---

## 📄 Exemplo de Estrutura do `stock.json`

```json
[
  {
    "cod": "A01",
    "nome": "Água",
    "quant": 10,
    "preco": 0.50
  },
  {
    "cod": "B02",
    "nome": "Sumo",
    "quant": 5,
    "preco": 1.20
  }
]
```

---

## 📊 Exemplo de Execução

```
maq: 2025-03-09, Stock carregado, Estado atualizado.
maq: Bom dia. Estou disponível para atender o seu pedido.

>> LISTAR
cod     |  nome                 |  quantidade |  preço
------------------------------------------------------
A01       Água                    10          0.5
B02       Sumo                    5           1.2

>> MOEDAS 1e 50c
maq: Saldo = 1e 50c

>> SELECIONAR A01
maq: Pode retirar o produto dispensado Água
maq: Saldo = 1e 0c

>> SAIR
maq: Pode retirar o troco: 1x 1e.
maq: Até à próxima
```

---
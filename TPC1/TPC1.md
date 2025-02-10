# Explicação do Código `somador`

Este documento explica o funcionamento da função `somador`, que processa uma string para somar números e interpretam comandos especiais (`ON` e `OFF`) para ativar ou desativar a soma.

## Objetivo
O código analisa um texto contendo números e palavras-chave (`ON`, `OFF`, `=`) e realiza a soma dos números encontrados, dependendo do estado do processamento.

## Estrutura do Código
O código contém três funções principais:

1. **`somador(texto)`** - Processa a string e soma os números, respeitando os comandos `ON` e `OFF`.
2. **`somadorR(texto)`** - Variante da função `somador`, com funcionamento semelhante.
3. **`main()`** - Gera um texto de teste e chama as funções `somador` e `somadorR`.

## Explicação da função

### `somador(texto)`
- **Variáveis**:
  - `contador`: Armazena a soma total.
  - `i`: Índice para percorrer a string.
  - `numeros`: Conjunto de caracteres que representam dígitos.
  - `stop`: Flag para controlar a ativação da soma.
- **Fluxo**:
  - Percorre a string.
  - Identifica números e soma-os caso `stop == False`.
  - `ON` reativa a soma, `OFF` desativa.
  - `=` imprime o resultado acumulado.

**Saída esperada:**
Para o caso do input abc12def34OFfxyz56ON78=:
```
12 + 34 = 46  (Antes de OFF)
56 ignorado   (Durante OFF)
78 somado     (Após ON)
Resultado: 124
```

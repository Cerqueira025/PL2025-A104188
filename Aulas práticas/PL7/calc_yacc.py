import ply.yacc as yacc
from calc_lex import tokens

def p_operacao_1(p):
  "operacao : calc"
  p[0] = p[1]

#SOMA
def p_operacao_2(p):
  "operacao : operacao ADD calc"
  p[0] = p[1] + p[3]

#SUB
def p_operacao_3(p):
  "operacao : operacao SUB calc"
  p[0] = p[1] - p[3]


def p_calc_1(p):
  "calc : expressao"
  p[0] = p[1] 

#MULT
def p_calc_2(p):
  "calc : calc MULT expressao"
  p[0] = p[1] * p[3]

#DIV
def p_calc_3(p):
  "calc : calc DIV expressao"
  if p[3] == 0:
    print("Erro: divisão por zero!")
    p[0] = 0  # Ou podes lançar uma exceção
  else:
    p[0] = p[1] / p[3]


def p_expressao(p):
  "expressao : NUMBER"
  p[0] = p[2]

# (
def p_expressao_1(p):
  "expressao : AP operacao FP"
  p[0] = p[1]

def p_error(p):
  print("Erro de sintaxe!")

parser = yacc.yacc()

def main():
  expr = input("INSIRA A EXPRESSÃO: ")
  r = parser.parse(expr)
  print("Resultado: ", r)

if __name__ == '__main__':
  main()
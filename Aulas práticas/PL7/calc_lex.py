import ply.lex as lex

tokens =[   "NUMBER",
            "ADD",
            "SUB",
            "MULT",
            "DIV",
            "AP",
            "FP" ]


def t_NUMBER(t):
  r"\d+"
  t.value = int(t.value)
  return t
    
t_ADD = r"\+"
t_SUB = r"-"
t_MULT = r"\*"
t_DIV = r"/"
t_AP = r"\("
t_FP = r"\)"

t_ignore = " \t\n"

def t_error(t):
    print(f"\n\nErro found on line: {t.lineno}"
          f"\nWith Element: {t.value[0]}\n\n")
    t.lexer.skip(1)
    pass

lexer = lex.lex()

def main ():
    message = input("INSERT EQUATIONS: ")
    lexer.input(message)
    while token := lexer.token():
        print(token)

if __name__ == "__main__":
    main()
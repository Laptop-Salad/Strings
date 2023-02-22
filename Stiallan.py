# Stiallan
from lexer import tokenize
import s_parser
import interpreter

print("""
 ______  _______ _____  ______   _        _        ______   ______  
/ |        | |    | |  | |  | | | |      | |      | |  | | | |  \ \ 
'------.   | |    | |  | |__| | | |   _  | |   _  | |__| | | |  | | 
 ____|_/   |_|   _|_|_ |_|  |_| |_|__|_| |_|__|_| |_|  |_| |_|  |_| 


Type exit to exit
""")

def main():
    variables = interpreter.variables
    
    while True:
        code = input("> ")

        if code.lower() == "exit":
            return 0
        
        sc_tokens = tokenize(code)

        if type(sc_tokens) != list:
            print(sc_tokens)
            return 1
        
        pos = 0
        
        if sc_tokens[pos].typ != "LBRACKET":
            print("ERROR at position", pos, "expected ( but got", sc_tokens[pos].text)
            return 1

        ast = s_parser.bracket(pos, sc_tokens)

        print(interpreter.start_interpreter(ast, variables))
        variables = interpreter.variables

start = main()

while start != 0:
    start = main()
    

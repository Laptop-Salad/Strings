# Stiallan
from lexer import tokenize
import parser
import interpreter

print("""
 ______  _______ _____  ______   _        _        ______   ______  
/ |        | |    | |  | |  | | | |      | |      | |  | | | |  \ \ 
'------.   | |    | |  | |__| | | |   _  | |   _  | |__| | | |  | | 
 ____|_/   |_|   _|_|_ |_|  |_| |_|__|_| |_|__|_| |_|  |_| |_|  |_| 


Type exit to exit
""")

variables = interpreter.variables

while True:
    code = input("> ")

    if code.lower() == "exit":
        break
    
    sc_tokens = tokenize(code)
    pos = 0
    
    if sc_tokens[pos].typ != "LBRACKET":
        print("ERROR at position", pos, "expected ( but got", sc_tokens[pos].text)
    else:
        ast = parser.bracket(pos, sc_tokens)

    print(interpreter.start_interpreter(ast, variables))
    variables = interpreter.variables
    

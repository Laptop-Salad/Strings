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
    """
    main

    Gets input from user and puts it through the lexer, parser and interpreter. The main function keeps track of variables the
    user declares until a user types "exit".
    """
    variables = interpreter.variables
    
    while True:
        code = input("> ")

        if code.lower() == "exit":
            return 0
        
        sc_tokens = tokenize(code)

        if type(sc_tokens) != list:
            return 1
        
        pointer = 0

        ast = s_parser.bracket(pointer, sc_tokens)
        
        res = interpreter.start_interpreter(ast, variables)
        
        if res != "ERROR Occured":
            print(res)
            
        variables = interpreter.variables

start = main()

while start != 0:
    start = main()
    

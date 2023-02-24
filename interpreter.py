## Interpreter for Stiallan
import err

variables = {}
operators = ["+", "-", "*", "/", "%"]
keywords = [
    "PLUS",
    "MINUS",
    "MULTIPLY",
    "DIVIDE",
    "MODULO",
    "LBRACKET",
    "RBRACKET",
    "DECLARE",
    "AS"
]

def handle_math(ast):
    """
    handle_math
    
    Handles mathematic calculations for the following:
    - Addition
    - Subtraction
    - Multiplication
    - Division
    - Modulo 

    Args:
        ast (list): abstract syntax tree

    Returns:
        integer: result of calculation
    """
    holder = ast[2]
    pointer = 3
    
    while pointer < len(ast):
        if type(ast[pointer]) == int or type(ast[pointer]) == float:
            match ast[1]:
                case "+":
                    holder += ast[pointer]
                case "-":
                    holder -= ast[pointer]
                case "*":
                    holder *= ast[pointer]
                case "/":
                    holder /= ast[pointer]
                case "%":
                    holder %= ast[pointer]
            
            pointer += 1
        else:
            break
    
    return holder                  
    

def lookup_vars(ast, variables):
    """
    lookup_vars

    Search through ast and replace variables with its values

    Args:
    - `ast`: (List) abstract syntax tree

    Returns:
    - `ast`: (List) abstract syntax tree
    """
    i = 0
    while i < len(ast):
        try:
            if ast[i] in variables:
                ast[i] = variables[ast[i]]
            i += 1
        except:
            i += 1
            continue

    return ast


def interpret(ast, variables):
    """
    interpret

    Interprets a single line of code with no nested operations.

    Example:
    (+ 5 5) -> 10
    (declare x as 5) -> 5

    Args:
    - `ast`: (List) abstract syntax tree

    Returns:
    - 'holder': The result on an operation
    """
    # For calculations
    if ast[1] in operators:
        # Check for variables and map it to its value
        ast = lookup_vars(ast, variables)
        
        return handle_math(ast)
        
    # Declaring variables if first token is "DEC"
    elif ast[1] == "DEC":
        # The second token should be the variable name
        if ast[2].isalpha() and ast[2] not in keywords:
            variables[ast[2]] = "NULL"

            # The third token should be "AS"
            if ast[3] == "AS":
                # The fourth token should be the value to map to the variable
                if type(ast[4]) == int:
                    variables[ast[2]] = ast[4]
                    return variables[ast[2]]
                elif type(ast[4]) == str:
                    variables[ast[2]] = ast[4]
                    return variables[ast[2]]
            else:
                return 1, err.expected_error(3, "'AS'", "'" + str(ast[3]) + "'")
        else:
            return 1, err.expected_error(2, "variable name", "'" + str(ast[2]) + "'")
    else:
        return 1, err.invalid_error("operator or statement", "'" + str(ast[1]) + "'")


             
def start_interpreter(ast, dict_vars):
    """
    start_interpreter

    Takes in a line of code, breaks it down and sets it to interpreter to be interpreted.

    Args:
    - `ast`: (List) abstract syntax tree
    - `dict_vars`: (Dictionary) a dictionary of variables

    Returns:
    - `res`: Result
    """
    i = 0
    variables = dict_vars


    while i < len(ast):
        # For nested brackets, handle nested brackets first
        if type(ast[i]) == list:
            
            res = start_interpreter(ast[i], variables)
            ast[i] = res

        i += 1
    
    # If there are no nested brackets left, interpreted the whole ast
    res = interpret(ast, variables)
    
    try:
        if res[0] == 1:
            return "ERROR Occured"
    except:
        pass
    
    return res

### Interpreter for Stiallan
from helpers import *

variables = {}
operators = ["+", "-", "*", "/", "%"]

def check_unmatched(ast):
    """
    check_unmatched

    Checks if brackets are unmatched

    Arguments:
    - `ast`: (List) abstract syntax tree

    Returns:
    - Bool: True (are unmatched)

    """
    ast_string = ''.join(str(ast))
    if ast_string.count('LBRACKET') != ast_string.count('RBRACKET'):
        return True

    return False
    

def lookup_vars(ast, variables):
    """
    lookup_vars

    Search through ast and replace variables with its values

    Arguments:
    - `ast`: (List) abstract syntax tree

    Returns:
    - `ast`: (List) abstract syntax tree
    """
    i = 0
    while i < len(ast):
        if ast[i] in variables:
            ast[i] = variables[ast[i]]
        i += 1

    return ast


def interpret(ast, variables):
    """
    interpret

    Interprets a single line of code with no nested operations.

    Example:
    (+ 5 5) -> 10
    (declare x as 5) -> 5

    Arguments:
    - `ast`: (List) abstract syntax tree

    Returns:
    - 'holder': The result on an operation
    """
    ## For calculations
    if ast[1] in operators:
        # Check for variables and map it to its value
        ast = lookup_vars(ast, variables)

        # Handle Addition if operator is "+"
        if ast[1] == "+":
            holder = 0
            pointer = 2

            # While the pointer 'pointer' is less than the length of the piece of code
            # Add each integer found and return the total
            while pointer < len(ast):
                if type(ast[pointer]) == int or type(ast[pointer]) == float:
                    holder += ast[pointer]
                    pointer += 1
                else:
                    break

            return holder

        # Subtraction if operator is "-"
        elif ast[1] == "-":
            if ast[2] in variables:
                ast[2] = variables[ast[2]]

            # Initialise holder with the first integer
            holder = ast[2]
            pointer = 3

            # While the pointer 'pointer' is less than the length of the piece of code
            # Minus an integer found from holder and return the result
            while pointer < len(ast):
                if type(ast[pointer]) == int or type(ast[pointer]) == float:
                    holder -= ast[pointer]
                    pointer += 1
                else:
                    break

            return holder

        # Division if operator is "/"
        elif ast[1] == "/":
            if ast[2] in variables:
                ast[2] = variables[ast[2]]

            # Initialise holder with first integer
            holder = ast[2]
            pointer = 3

            # While the pointer 'pointer' is less than the length of the piece of code
            # Divide holder by each integer found and return the result
            while pointer < len(ast):
                if type(ast[pointer]) == int or type(ast[pointer]) == float:
                    holder /= ast[pointer]
                    pointer += 1
                else:
                    break

            return holder

        # Multiplication if operator is "*"
        elif ast[1] == "*":
            if ast[2] in variables:
                ast[2] = variables[ast[2]]

            # Initialise holder with first integer
            holder = ast[2]
            pointer = 3

            # While the pointer 'pointer' is less than the length of the piece of code
            # Multiply the holder by each integer found and return the result
            while pointer < len(ast):
                if type(ast[pointer]) == int or type(ast[pointer]) == float:
                    holder *= ast[pointer]
                    pointer += 1
                else:
                    break

            return holder

        # Modulo if operato is "%"
        elif ast[1] == "%":
            pointer = 2
            holder_arr = []

            # While the pointer 'pointer' is looking at an integer/float in a piece of code, append them to holder_arr
            while type(ast[pointer]) == int or type(ast[pointer]) == float:
                # Ensure MOD is only used on two integers
                if pointer > 4:
                    print("ERROR cannot use MOD on a third number")
                    exit()
                else:
                    holder_arr.append(ast[pointer])
                    pointer += 1

            return holder_arr[0] % holder_arr[1]
        
    ## Declaring variables is first token is "DEC"
    elif ast[1] == "DEC":
        try:
            # The second token should be the variable name
            if ast[2].isalpha() and ast[2] != "RBRACKET":
                variables[ast[2]] = "NULL"

                # The third token should be "AS"
                if ast[3] == "AS":

                    # The fourth token should be the value to map to the variable
                    if type(ast[4]) == int:
                        variables[ast[2]] = ast[4]
                    else:
                        print("ERROR expected variable name after AS but got", ast[4])
                        exit()
                else:
                    print(ast[3])
                    
            else:
                print("ERROR expected variable name after DECLARE but got", ast[2])
                exit()

            return variables[ast[2]]
        except:
            print(error(0, "final"))
            exit()


             
def start_interpreter(ast, dict_vars):
    """
    start_interpreter

    Takes in a line of code, breaks it down and sets it to interpreter to be interpreted.

    Arguments:
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
            if check_unmatched(ast[i]):
                return error(0, len(ast)-1)
            
            res = start_interpreter(ast[i], variables)
            ast[i] = res

        i += 1

    if check_unmatched(ast):
        return error(0, len(ast)-1)
    
    # If there are no nested brackets left, interpreted the whole ast
    res = interpret(ast, variables)
    return res

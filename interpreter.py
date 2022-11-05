### Interpreter for Stiallan
from helpers import *

variables = {}
operators = ["+", "-", "*", "/", "%"]

def lookup_vars(ast):
    """
    lookup_vars

    Search through ast and replace variables with its values

    Arguments:
    - `ast`: (Arr) abstract syntax tree

    Returns:
    - `ast`: (Arr) abstract syntax tree
    """
    i = 0
    while i < len(ast):
        if ast[i] in variables:
            ast[i] = variables[ast[i]]
        i += 1

    return ast


def interpret(ast):
    """
    interpret

    Interprets a single line of code with no nested operations.

    Arguments:
    - `ast`: (Arr) abstract syntax tree
    """
    ## For calculations
    if ast[1] in operators:
        # Check for variables
        ast = lookup_vars(ast)

        # Addition
        if ast[1] == "+":
            holder = 0
            pos = 2
            while pos < len(ast):
                if type(ast[pos]) == int or type(ast[pos]) == float:
                    holder += ast[pos]
                    pos += 1
                else:
                    break

            return holder

        # Subtraction
        elif ast[1] == "-":
            if ast[2] in variables:
                ast[2] = variables[ast[2]]
            holder = ast[2]
            pos = 3
            while pos < len(ast):
                if type(ast[pos]) == int or type(ast[pos]) == float:
                    holder -= ast[pos]
                    pos += 1
                else:
                    break

            return holder

        # Division
        elif ast[1] == "/":
            if ast[2] in variables:
                ast[2] = variables[ast[2]]
            holder = ast[2]
            pos = 3
            while pos < len(ast):
                if type(ast[pos]) == int or type(ast[pos]) == float:
                    holder /= ast[pos]
                    pos += 1
                else:
                    break

            return holder

        # Multiplication
        elif ast[1] == "*":
            if ast[2] in variables:
                ast[2] = variables[ast[2]]
            holder = ast[2]
            pos = 3
            while pos < len(ast):
                if type(ast[pos]) == int or type(ast[pos]) == float:
                    holder *= ast[pos]
                    pos += 1
                else:
                    break

            return holder

        # Modulo
        elif ast[1] == "%":
            pos = 2
            holder_arr = []
            while type(ast[pos]) == int or type(ast[pos]) == float:
                if pos > 4:
                    print("ERROR cannot use MOD on a third number")
                    exit()
                else:
                    holder_arr.append(ast[pos])
                    pos += 1


            return holder_arr[0] % holder_arr[1]
    ## Declaring variables
    elif ast[1] == "DEC":
        try:
            if ast[2].isalpha() and ast[2] != "RBRACKET":
                variables[ast[2]] = "NULL"
                if ast[3] == "AS":
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
    - `ast`: (Arr) abstract syntax tree
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

    res = interpret(ast)
    return res
            




    

# Interpreter for Stiallan
from keys import operators

variables = {}

def interpret(ast):
    if ast[1] in operators:
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
            
        elif ast[1] == "-":
            holder = ast[2]
            pos = 3
            while pos < len(ast):
                if type(ast[pos]) == int or type(ast[pos]) == float:
                    holder -= ast[pos]
                    pos += 1
                else:
                    break

            return holder

        elif ast[1] == "/":
            holder = ast[2]
            pos = 3
            while pos < len(ast):
                if type(ast[pos]) == int or type(ast[pos]) == float:
                    holder /= ast[pos]
                    pos += 1
                else:
                    break

            return holder

        elif ast[1] == "*":
            holder = ast[2]
            pos = 3
            while pos < len(ast):
                if type(ast[pos]) == int or type(ast[pos]) == float:
                    holder *= ast[pos]
                    pos += 1
                else:
                    break

            return holder

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
    elif ast[1] == "DEC":
        try:
            if ast[2].isalpha() and ast[2] != "end":
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
            print("ERROR unexpected EOF")
            exit()


            
        
        
def start_interpreter(ast):
    i = 0
    while i < len(ast):
        if type(ast[i]) == list:
            res = start_interpreter(ast[i])
            ast[i] = res

        i += 1

    res = interpret(ast)
    return res
            




    

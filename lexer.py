### Stiallan Lexer
from helpers import error

class Token:
    """
    Token class

    Creates a token object.

    Arguments:
    - `typ`: (Str) the type of token e.g 'PLUS'
    - `text`: (Str) the original text of the token e.g. '+'
    - `start_pos`: (Int) the starting position of the token.

    Returns:
    Token object with values of 'typ', 'text' and 'start_pos'.
    """
    def __init__(self, typ, text, start_pos):
        self.typ = typ
        self.text = text
        self.start_pos = start_pos


types = {
    "+" : "PLUS",
    "-" : "MINUS",
    "*" : "MULTIPLY",
    "/" : "DIVIDE",
    "%" : "MODULO",
    "("     : "LBRACKET",
    ")"     : "RBRACKET",
    "declare": "DEC",
    "as": "AS",
}


def tokenize(code):
    """
    tokenize function

    Takes a line of code and returns an array of token objects.

    Arguments:
    - `code`: (Str) a single line of code

    Returns:
    Array of Token
    """
    pointer = 0
    sc_tokens = []
    try:
        # Ignore whitespaces
        while pointer < len(code):
            if code[pointer].isspace():
                pointer += 1
                continue

            # Handle Keywords, found in 'types' variable
            elif code[pointer] in types:
                sc_tokens.append(Token(types[code[pointer]], code[pointer], pointer))
                pointer += 1

            # Handle Numbers
            elif code[pointer].isnumeric():
                holder = []
                while code[pointer].isnumeric(): ## If more than 1 number, ex 22
                    holder.append(code[pointer])
                    pointer += 1
                
                numbers = int(''.join(holder)) 
                sc_tokens.append(Token("NUMBER", numbers, pointer))

            # Handle Letters
            elif code[pointer].isalpha():
                holder = []
                while code[pointer].isalpha():
                    holder.append(code[pointer])
                    pointer += 1
                
                joined = ''.join(holder)
                if joined in types:
                    sc_tokens.append(Token(types[joined], joined, pointer))
                else:
                    sc_tokens.append(Token("ALPHA", joined, pointer))
            
            # If character is not a letter, number or keyword it is unkown
            else:
                sc_tokens.append(Token("unknown", code[pointer], pointer))
                pointer += 1
    except:
        # If code ends unexpectedly
        return error(0, pointer-1)
    
    # Add EOF token to mark end
    sc_tokens.append(Token("EOF", "EOF", pointer))
    return sc_tokens

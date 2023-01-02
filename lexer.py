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
    i = 0
    sc_tokens = []
    try:
        # Ignore whitespaces
        while i < len(code):
            if code[i].isspace():
                i += 1
                continue

            # Keywords
            elif code[i] in types:
                sc_tokens.append(Token(types[code[i]], code[i], i))
                i += 1

            # Numbers
            elif code[i].isnumeric():
                holder = []
                while code[i].isnumeric(): ## If more than 1 number, ex 22
                    holder.append(code[i])
                    i += 1
                
                numbers = int(''.join(holder)) 
                sc_tokens.append(Token("NUMBER", numbers, i))

            # Letters
            elif code[i].isalpha():
                holder = []
                while code[i].isalpha():
                    holder.append(code[i])
                    i += 1
                
                joined = ''.join(holder)
                if joined in types:
                    sc_tokens.append(Token(types[joined], joined, i))
                else:
                    sc_tokens.append(Token("ALPHA", joined, i))
                
            else:
                sc_tokens.append(Token("unknown", code[i], i))
                i += 1
    except:
        # If code ends unexpectedly
        return error(0, i-1)
    
    sc_tokens.append(Token("EOF", "EOF", i)) # Add EOF token to mark end
    return sc_tokens

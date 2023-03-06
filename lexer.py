## Stiallan Lexer

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
    def __init__(self, typ, txt):
        self.typ = typ
        self.txt = txt


types = {
    "+" : "OP:PLUS",
    "-" : "OP:MINUS",
    "*" : "OP:MULT",
    "/" : "OP:DIV",
    "%" : "OP:MOD",
    "("     : "START",
    ")"     : "END",
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
                sc_tokens.append(Token(types[code[pointer]], code[pointer]))
                pointer += 1

            # Handle Numbers
            elif code[pointer].isnumeric():
                holder = []
                
                # If more than 1 number, ex 22
                while code[pointer].isnumeric():
                    holder.append(code[pointer])
                    pointer += 1
                     
                numbers = int(''.join(holder)) 
                sc_tokens.append(Token("INT", numbers))
            
            # If character is not a letter, number or keyword it is unkown
            else:
                sc_tokens.append(Token("unknown", code[pointer]))
                pointer += 1
    except:
        return 1
    
    # Add EOF token to mark end
    sc_tokens.append(Token("EOF", ""))
    return sc_tokens

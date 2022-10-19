# Stiallan Lexer

# Token Class
class Token:
    def __init__(self, typ, text, start_pos):
        self.typ = typ
        self.text = text
        self.start_pos = start_pos

# Token types
types = {
    "+" : "PLUS",
    "-" : "MINUS",
    "*" : "MULTIPLY",
    "/" : "DIVIDE",
    "%" : "MODULO",
    "("     : "LBRACKET",
    ")"     : "RBRACKET",
}

# List for Tokens in source code
sc_tokens = []

code = input("> ")

def tokenize():
    i = 0
    while i < len(code):
        if code[i].isspace():
            i += 1
            continue
        
        elif code[i] in types:
            ## TODO: Looking up type twice
            sc_tokens.append(Token(types[code[i]], code[i], i))
            i += 1

        elif code[i].isnumeric():
            holder = []
            while code[i].isnumeric(): ## If more than 1 number, ex 22
                holder.append(code[i])
                i += 1
                
            sc_tokens.append(Token("NUMBER", ''.join(holder), i))
        else:
            print("Unexpected character", code[i])
            exit()

        
    sc_tokens.append(Token("EOF", "EOF", i))
    return sc_tokens


sc_tokens = tokenize()

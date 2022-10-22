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
    "declare": "DEC",
    "as": "AS",
}

def tokenize(code):
    i = 0
    sc_tokens = []
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
        

        
    sc_tokens.append(Token("EOF", "EOF", i))
    return sc_tokens

## Stiallan Parser

def inner_bracket(pointer, tokens, ast):
    """
    inner_bracket

    Handles the inner brackets if there are any

    Arguments:
    - `pointer`: (int) current pointerition in tokens.
    - `tokens`: (List) List of tokens
    - `ast`: (List) abstract syntax tree
    
    Returns:
    - `pointer`: (int) current pointerition in tokens
    - `holder`: (List) List of tokens from inner bracket(s)
    """
    holder = []
    holder.append("LBRACKET")
    
    pointer += 1
    while tokens[pointer].typ != "RBRACKET":
        if tokens[pointer].typ == "LBRACKET":
            result = inner_bracket(pointer, tokens, ast)
            pointer = result[0]
            holder.append(result[1])
        else:
            holder.append(tokens[pointer].text)
            pointer += 1


    holder.append("RBRACKET")
    pointer += 1

    return pointer, holder

def bracket(pointer, tokens):
    """
    bracket

    Handles the outside bracket

    Arguments:
    - `pointer`: (int) current pointerition in tokens.
    - `tokens`: (List) of tokens   

    Returns:
    - `ast`: (List) abstract syntax tree
    """
    ast = []
    pointer += 1
    ast.append("LBRACKET")

    while pointer < len(tokens):
        if tokens[pointer].typ == "LBRACKET":
            result = inner_bracket(pointer, tokens, ast)
            pointer = result[0]
            ast.append(result[1])
        elif tokens[pointer].typ == "RBRACKET":
            ast.append("RBRACKET")
            pointer += 1
        elif tokens[pointer].typ == "DEC":
            ast.append(tokens[pointer].typ)
            pointer += 1
        elif tokens[pointer].typ == "AS":
            ast.append(tokens[pointer].typ)
            pointer += 1
        else:
            ast.append(tokens[pointer].text)
            pointer += 1
            

    return ast

## Stiallan Parser

class Node:
    def __init__(self, token, prev, left=None, right=None):
        self.token = token
        self.left = left
        self.right = right
        self.prev = prev

def start_parser(sc_tokens):
    """
    start_parser
    
    Creates an AST - abstract syntax tree.

    Args:
        sc_tokens (list): A list of tokens from the lexer.

    Returns:
        Node: Returns the head node of the AST
    """
    head_node = None
    current_node = None
    
    # After adding a nested statement, the program needs to move back up the AST to add 
    # the rest of the statement
    nested_statements = False
    end_count = 0
    
    for token in sc_tokens:
        if token.typ == "END":
            end_count += 1
    
    if end_count > 1:
        nested_statements = True
    
    # Create AST
    for token in sc_tokens:
        if head_node is None:
            head_node = Node(token, None)
            current_node = head_node
        else:
            if token.typ == "START":
                current_node.right = Node(token, current_node)
                current_node = current_node.right
            elif token.typ == "END" and nested_statements:
                current_node.left = Node(token, current_node)
                while current_node.prev is not None and current_node.right is None:
                    current_node = current_node.prev
                
                if current_node.left is not None:
                    current_node = current_node.left
            else:
                current_node.left = Node(token, current_node)
                current_node = current_node.left                              
                    
    return head_node
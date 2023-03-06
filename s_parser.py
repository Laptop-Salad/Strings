## Stiallan Parser
from lexer import Token

class Node:
    def __init__(self, token, left=None, right=None):
        self.token = token
        self.left = left
        self.right = right

def start_parser(sc_tokens):
    head_node = None
    current_node = None
    
    # Create AST
    for token in sc_tokens:
        if head_node is None:
            head_node = Node(token)
            current_node = head_node
        else:
            if token.typ == "START":
                current_node.right = Node(token)
                current_node = current_node.right
            else:
                current_node.left = Node(token)
                current_node = current_node.left                
                    
    return head_node
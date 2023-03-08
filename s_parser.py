## Stiallan Parser

class Node:
    def __init__(self, token, prev, left=None, right=None):
        self.token = token
        self.left = left
        self.right = right
        self.prev = prev

def traverse_left(current_node, prefix=None):
    while current_node is not None:
        if prefix is not None:
            print(prefix, "LEFT:", current_node.token.typ, current_node.token.txt)
        else:
            print("LEFT:", current_node.token.typ, current_node.token.txt)
        
        if current_node.right is not None:
            current_node = traverse_right(current_node.right, "LEFT")
            
            if current_node is None:
                return
            
            current_node = current_node.left
            
        current_node = current_node.left
        
    return current_node

def traverse_right(current_node, prefix=None):
    while current_node is not None:
        if prefix is not None:
            print(prefix, "RIGHT:", current_node.token.typ, current_node.token.txt)
        else:
            print("RIGHT:", current_node.token.typ, current_node.token.txt)
        
        if current_node.left is not None:
            current_node = traverse_left(current_node.left, "RIGHT")
            
            if current_node is None:
                return
            
            current_node = current_node.right
            
        current_node = current_node.right
    
    return current_node
        
def traverse_ast(head_node):
    if head_node is None:
        return
    
    current_node = head_node
    
    traverse_left(current_node)

def start_parser(sc_tokens):
    head_node = None
    current_node = None
    
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
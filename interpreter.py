## Interpreter for Stiallan
from lexer import Token
from s_parser import Node

def handle_operation(current_node):
    """
    handle_operation

    Args:
        current_node (Node): A node that contains a token with type "OP", start of an operation

    Returns:
        Result of operation
    """
    result = None
    operation = current_node.token.typ.split(":")[1]
    current_node = current_node.left
    
    while current_node is not None or current_node != ")":
        if current_node is None:
            break
        
        if current_node.right is not None:
            if current_node.right.token.typ == "START":
                new_statement = current_node.right
                inner_result = handle_operation(new_statement.left)
                
                current_node.right = None
                holder = current_node.left
                
                current_node.left = Node(
                    Token("INT", inner_result),
                    current_node,
                    holder
                )
        
        if current_node.token.typ == "INT":
            if result == None:
                result = int(current_node.token.txt)
            else:
                match operation:
                    case "PLUS":
                        result += int(current_node.token.txt)
                    case "MINUS":
                        result -= int(current_node.token.txt)
                    case "MULT":
                        result *= int(current_node.token.txt)
                    case "DIV":
                        result /= int(current_node.token.txt)
                    case "MOD":
                        result %= int(current_node.token.txt)
        
        current_node = current_node.left
    
    return result

def find_start(head_node):
    """
    find_start
    
    Finds the start of an operation, by locating token beginning with 'OP'. It then passes this
    token to handle_operation, and returns the result.

    Args:
        head_node (Node): the first node in the AST (linked list)

    Returns:
        the result on an operation.
    """
    if head_node is None:
        return 1
    
    if head_node.token.typ != "START":
        return "ERROR: Illegal start of statement. Must start with \"("
    
    current_node = head_node
    
    if current_node.right is not None:
        return "ERROR: Illegal start of sub-statement"
    
    current_node = current_node.left

    if current_node.token.typ.startswith("OP"):
        return handle_operation(current_node)

def start_interpreter(head_node):
    """
    start_interpreter
    
    Starts the process of interpreting line of code, is called by outside functions.

    Args:
        head_node (Node): the first node in the AST (linked list)

    Returns:
        result of line of code
    """
    
    res = find_start(head_node)
    
    return res

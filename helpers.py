### Stiallan helper
# These fuctions/variables are used by multiple files

operators = ["+", "-", "*", "/", "%"]

def error(error_code, pos):
    errors = ["Unexpected EOF"]

    print("ERROR at position", pos, errors[error_code])

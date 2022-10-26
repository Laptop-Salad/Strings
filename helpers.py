### Stiallan helper

def error(error_code, pos):
    errors = ["Unexpected EOF"]

    print("ERROR at position", pos, errors[error_code])

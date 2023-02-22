### Stiallan helper

def error(error_code, pos):
    """
    error

    This function prints out an error message based on the given error code."

    # Arguments:
    - `error_code`: An integer that identifies the type of error.
    - `pos`: An integer showing the position in the code where the error occured.

    # Returns:
    - String `error_message`
    """

    errors = {
        0 : "Unexpected end of line",
    }
    
    error_message = "ERROR at position {position} : {error}".format(position=pos,error=errors[error_code])
    return error_message

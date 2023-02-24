def raise_error(error_message):
    print(error_message)
    return error_message


def expected_error(pos, expected, actual, hint=None,):          
    if hint != None:
        error_message =  "ERROR at position {}: Expected {} but got {}. Did you mean {}?".format(pos, expected, actual, hint)
    else:
        error_message = "ERROR at position {}: Expected {} but got {}.".format(pos, expected, actual)   
    
    raise_error(error_message)
    return error_message


def invalid_error(expected, actual):
    error_message = "ERROR: Expected {} but got {}".format(expected, actual)
    raise_error(error_message)
    return error_message

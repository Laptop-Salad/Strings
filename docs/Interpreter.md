# Interpreter
The third phase of the interpreter. It takes the AST created in the second phase and interprets its meaning.

## The Source Code
### `variables`
Holds variables that are created. Is passed from `Stiallan.py`. `Interpreter.py` can add new variables and use it as a reference and `Stiallan.py` grabs it from `Interpreter.py` after interpreter is done.

###  `lookup_vars(ast)`
Takes one argument `ast`. Searches through `ast` and replaces any variables with its value from the `variables` array.

### `interpret(ast)`
Takes one argument `ast`. Interprets the meaning of a single operation. A single operation is defined as one set of brackets with no nested brackets.

It will either return the result of the operation or print an error.

### `start_interpreter(ast, dict_vars)`
Takes two arguments:
- `ast`
- `dict_vars`: Passed from `Stiallan.py`. Is short for "dictionary of variables".

Takes the AST created in the previous phase and passes each set of brackets starting from the inner most one to `interpret`. Returns `res`, the result.

# Parser
The second phase of an interpreter, creating an abstract syntax tree (ast).  Defines the hierarchical structure of the code.

## The Source Code
### `inner_bracket(pos, tokens, ast)`
Takes in three arguments:
- `pos` : Current position in tokens array.
- `tokens` : Tokens array.
- `ast` :  Abstract syntax tree.

Is called if there are any brackets inside another bracket. 
Returns:
- `pos` : Current position in the tokens array.
- `holder`: Acts a mini AST to be appended into `ast` later.

### `bracket(pos, tokens)`
Creates and builds AST. Calls `inner_bracket` to handle any potential nested brackets.

Takes in two arguments:
- `pos`:  Position in the tokens array
- `tokens`: An array of Tokens from `lexer.py`.

Returns an AST.

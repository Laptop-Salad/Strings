# Lexical Analyser
The first phase of an interpreter. The lexer or lexical analyser takes a line of code and translates it into tokens. .

## Tokens

|  Example Text | Example Position  |  Token |
| ------------ | ------------ | ------------ |
| +  | 3  | ["PLUS", "+", 3]  |
| -  | 4  | ["MINUS", "+", 4]   |
| *  | 2  | ["MULTIPLY", "+", 2]  |
| /  | 9 | ["DIVIDE", "+", 9]   |
| %  | 1  | ["MODULO", "+", 1]   |
| (  | 0  | ["LBRACKET", "+", 0]   |
| )  | 5  | ["RBRACKET", "+", 5]   |
| declare  | 1  | ["DEC", "+", 1]   |
| as  | 3  | ["AS", "+", 3]   |
| num_count  | 2  | ["ALPHA", "+", 2]   |
| 24  | 2 | ["NUMBER", "+", 2]  |
| "hello world" | 13 | ["STRING", "hello world", 13] |
| $ | 1 | ["unknown", "+", 1]  |

## Data Types
Currently Stiallan only has one two types, integer and string.

Declare integers
```
> (declare x as 5)
> 5
```

Declare strings
```
> (declare message as "Hello World")
> Hello World
```

## The Source Code

### `Token`
Takes in three arguments:
- `typ` : The name of the Token.
- `text` : The original section of code/text.
- `start_pos`: The starting position of the Token.

Used to instantiate a Token. Is used in the `tokenize` function.

### `types`
Holds some token types that require a specific character, e.g. a plus symbol. 
###  `tokenize(code)`
Takes in a single argument`code`, a single line of code entered by the user. This function is called from the main file`Stiallan.py`. It takes a single line of code and returns an array of`Token`.
### `sc_tokens`
Is an array and is short for "source code tokens". Is the array of Tokens returned by the tokenize function.

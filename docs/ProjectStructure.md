#Project Structure

## Files
1. `stiallan.py`: The main file, takes a line of code and takes it through the whole process of interpreting it. Read the [Documentation](Stiallan.md).
2. `lexer.py`: The first phase, tokenizing the code. Read the [Documentation](Lexer.md).
3. `parser.py`: The second phase, creating an abstract syntax tree. Read the [Documentation](Parser.md).
3. `interpreter.py`: The third phase, understanding the meaning of the code and producing a result. Read the [Documentation](Interpreter.md).
4. `helpers.py`: Contains functions/variables that two or more files require. Read the [Documentation](Helpers.md).

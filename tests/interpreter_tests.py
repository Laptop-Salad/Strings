import unittest
import sys

sys.path.append('../')
from interpreter import start_interpreter, lookup_vars
from s_parser import bracket
from lexer import tokenize

def run_code(code, variables={}):
    sc_tokens = tokenize(code)
    ast = bracket(0, sc_tokens)
    result = start_interpreter(ast, variables)
    return result

class TestMath(unittest.TestCase):
    # Addition 
    def test_addition(self):
        result = run_code("(+ 5 5)")
        expected = 10
        self.assertEqual(result, expected)

    # Subtraction
    def test_subtraction(self):
        result = run_code("(- 5 5)")
        expected = 0
        self.assertEqual(result, expected)

    # Multiplication
    def test_multiplication(self):
        result = run_code("(* 5 5)")
        expected = 25
        self.assertEqual(result, expected)

    # Division
    def test_division(self):
        result = run_code("(/ 100 2)")
        expected = 50
        self.assertEqual(result, expected)

    # Nested calculations
    def test_nested(self):
        result = run_code("(+ 10 (- 10 5) 8)")
        expected = 23
        self.assertEqual(result, expected)

    # Declaring variables
    def test_declare_variable(self):
        result = run_code("(declare x as 6)")
        expected = 6
        self.assertEqual(result, expected)

    # Calculation using variable
    def test_addition_variable(self):
        result = run_code("(+ x x)", {"x": 5})
        expected = 10
        self.assertEqual(result, expected)


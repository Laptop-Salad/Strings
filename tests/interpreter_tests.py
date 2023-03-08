import unittest
import sys

sys.path.append('../')
from interpreter import start_interpreter
from s_parser import start_parser
from lexer import tokenize

def run_code(code, variables={}):
    sc_tokens = tokenize(code)
    ast = start_parser(sc_tokens)
    result = start_interpreter(ast)
    return result

class TestMath(unittest.TestCase):       
    def test_addition(self):
        self.assertEqual(run_code("(+ 5 5)"), 10)
        self.assertEqual(run_code("(+ 10 5 4 3)"), 22)

    def test_subtraction(self):
        self.assertEqual(run_code("(- 5 5)"), 0)
        self.assertEqual(run_code("(- 20 10 5 6)"), -1)

    def test_multiplication(self):
        self.assertEqual(run_code("(* 5 5)"), 25)

    def test_division(self):
        self.assertEqual(run_code("(/ 100 2)"), 50)

    def test_nested(self):
        self.assertEqual(run_code("(+ 10 (- 10 5) 8)"), 23)

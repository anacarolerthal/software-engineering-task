import unittest
from unittest import mock
import sys

sys.path.append("../src")
from prompt import Prompt

class PromptTests(unittest.TestCase):
    
    def test_talkReturnsCorrectInput(self):
        self.prompt = Prompt("Digite um CPF: ")
        cpf = "141.325.157-96"
        with unittest.mock.patch('builtins.input', return_value=cpf):
            input_cpf = self.prompt.talk()
        self.assertEqual(input_cpf, cpf)

if __name__ == '__main__':
    unittest.main()



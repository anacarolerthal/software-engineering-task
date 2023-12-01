import unittest
import sys

sys.path.append("../src")
from cpf import Cpf
from custom_exceptions import TodosDigitosIguaisException, DigitoVerificadorInvalidoException, NumeroDigitosInvalidoException

class CpfTests(unittest.TestCase):

    def test_deveCalcularDigitoVerificadorComSucessoAoReceberCpfValido(self):
        # arrange
        CPF_VALIDO = "151.834.230-24"
        DIGITO_VERIFICADOR_ESPERADO = 2
        self.cpf = Cpf(CPF_VALIDO)

        # act
        digito = Cpf.calculaDigitoVerificador(self.cpf)

        # assert
        self.assertEqual(digito, DIGITO_VERIFICADOR_ESPERADO)

    def test_deveRetornarErroAoReceberCpfComDigitoVerificadorInvalido(self):
        # arrange
        CPF_COM_DIGITO_VERIFICADOR_INVALIDO = "151.834.230-24"
        self.cpf = Cpf(CPF_COM_DIGITO_VERIFICADOR_INVALIDO)
        DIGITO_INVALIDO_1 = 3
        DIGITO_INVALIDO_2 = 5

        # act
        with self.assertRaises(DigitoVerificadorInvalidoException) as context:
            self.cpf.validaDigitos(DIGITO_INVALIDO_1, DIGITO_INVALIDO_2)

        # assert
        self.assertEqual("Digito verificador inválido", str(context.exception))

    def test_deveRetornarErroAoReceberCpfComDiferenteDe11Digitos(self):
        # arrange
        CPF_COM_MAIS_DE_11_DIGITOS = "141.325.157.123"
        self.cpf = Cpf(CPF_COM_MAIS_DE_11_DIGITOS)

        # act
        with self.assertRaises(NumeroDigitosInvalidoException) as context:
            self.cpf.validaCpf()

        # assert
        self.assertEqual("CPF deve ter 11 dígitos", str(context.exception))

    def test_deveRetornarErroAoReceberCpfComTodosOsDigitosIguais(self):
        # arrange
        CPF_DIGITOS_IGUAIS = "111.111.111-11"
        self.cpf = Cpf(CPF_DIGITOS_IGUAIS)

        # act
        with self.assertRaises(TodosDigitosIguaisException) as context:
            self.cpf.validaCpf()

        # assert
        self.assertEqual("Todos os dígitos são iguais", str(context.exception))

if __name__ == '__main__':
    unittest.main()
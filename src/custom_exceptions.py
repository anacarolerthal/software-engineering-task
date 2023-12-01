class TodosDigitosIguaisException(Exception):
    def __init__(self):
        super().__init__("Todos os dígitos são iguais")

class DigitoVerificadorInvalidoException(Exception):
    def __init__(self):
        super().__init__("Digito verificador inválido")

class NumeroDigitosInvalidoException(Exception):
    def __init__(self):
        super().__init__("CPF deve ter 11 dígitos")





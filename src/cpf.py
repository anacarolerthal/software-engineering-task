import re
import custom_exceptions

class Cpf():

    #Constructor
    def __init__(self, cpf):
        self._value = re.sub(r"[^0-9]", "", cpf)
        self._reconstructed_value = re.sub(r"[^0-9]", "", cpf[:-2])
        self._n_digitos = 9
        self._digito_verificador_1 = cpf[-2]
        self._digito_verificador_2 = cpf[-1]

    #Getters and Setters
    def getCpfValue(self):
        return self._value

    def getReconstructedCpfValue(self):
        return self._reconstructed_value

    def setReconstructedCpfValue(self, cpf):
        self._reconstructed_value = cpf

    def getNDigitos(self):
        return self._n_digitos

    def setNDigitos(self, n):
        self._n_digitos = n

    def getDigitoVerificador1(self):
        return self._digito_verificador_1

    def getDigitoVerificador2(self):
        return self._digito_verificador_2

    def validaDigitos(self, digito1, digito2):
        if (int(self.getDigitoVerificador1()) == digito1) and (int(self.getDigitoVerificador2()) == digito2):
            return True
        else:
            raise custom_exceptions.DigitoVerificadorInvalidoException()

    def checaQuantidadeDigitos(self):
        """
        Funcao que checa se a quantidade de digitos é 11
        """
        if len(self.getCpfValue()) != 11:
            return True
        else:
            return False

    def checaDigitosIguais(self):
        """
        Funcao que checa se todos os digitos sao iguais
        """
        if self.getCpfValue() == self.getCpfValue()[0] * len(self.getCpfValue()):
            return True
        else:
            return False

    def validaCpf(self):
        """
        Funcao que valida o cpf
        """
        if self.checaQuantidadeDigitos():
            raise custom_exceptions.NumeroDigitosInvalidoException()
        elif self.checaDigitosIguais():
            raise custom_exceptions.TodosDigitosIguaisException()
        else:
            return True

    #Functional method
    def calculaDigitoVerificador(cpf):
        digito = 0
        # variavel que guarda a posicao do digito que esta sendo calculado no momento
        pos_atual_digito = cpf.getNDigitos() + 1

        for cada_digito in cpf.getReconstructedCpfValue():
            digito += int(cada_digito) * pos_atual_digito
            pos_atual_digito -= 1

        digito = (digito * 10) % 11
        if digito == 10:
            digito = 0

        return digito


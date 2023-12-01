from src.prompt import Prompt
from src.cpf import Cpf
from src.custom_exceptions import TodosDigitosIguaisException, DigitoVerificadorInvalidoException

MESSAGE = "Formato para inserir CPF - XXX.XXX.XXX-XX: "

terminal = Prompt(MESSAGE)
answer = terminal.talk()
cpf = Cpf(answer)

if cpf.validaCpf():
    digito1 = Cpf.calculaDigitoVerificador(cpf)
    cpf.setReconstructedCpfValue(cpf.getReconstructedCpfValue() + str(digito1))
    cpf.setNDigitos(10)

    digito2 = Cpf.calculaDigitoVerificador(cpf)
    cpf.setReconstructedCpfValue(cpf.getReconstructedCpfValue() + str(digito2))
    cpf.setNDigitos(11)


    if cpf.validaDigitos(digito1, digito2):
        print("CPF é válido")
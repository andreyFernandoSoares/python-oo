from conta import Conta

def teste_conta():
    conta = Conta("555", "Diddy", 45.5, 1000.0)
    print(conta.extrato())

if (__name__ == "__main__"):
    teste_conta()

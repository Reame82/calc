def soma(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def divisao(a, b):
    if b == 0:
        print("nao divida por zero, burro")
    else:
        print("a / b")


def exp(a, b):
    return a ** b


while True:
    print("1) soma")
    print("2) subtração")
    print("3) sair")
    print("4) divisao")
    print(("5) exponenciação"))

    entrada = int(input("selecione uma opção: "))

    if entrada == 1:
        a = int(input("digita:"))
        b = int(input("digita:"))

        print(soma(a, b))

    if entrada == 2:
        a = int(input("digita:"))
        b = int(input("digita:"))
        print(subtrair(a, b))

    if entrada == 4:
        a = float(input("digita:"))
        b = float(input("digita:"))
        print(divisao(a, b))

    if entrada == 5:
        a = float(input("digite o valor :"))
        b = float(input("digite o expoente:"))
        print(exp(a, b))

    if entrada == 3:
        break

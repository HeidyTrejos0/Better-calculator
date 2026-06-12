def addmultiplenumbers(numeros):
    total = 0

    for numero in numeros:
        total = total + numero

    return total


def multiplymultiplenumbers(numeros):
    resultado = 1

    for numero in numeros:
        resultado = resultado * numero

    return resultado


def isiteven(num):
    if type(num) == int and num % 2 == 0:
        return True
    else:
        return False


def isitaninteger(num):
    if type(num) == int:
        return True
    else:
        return False


def main():
    print("Hello learners!")


if __name__ == "__main__":
    main()
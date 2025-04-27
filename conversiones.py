DIGITOS_BINARIOS = "01"
DIGITOS_OCTALES = "01234567"
DIGITOS_HEXADECIMALES = "0123456789ABCDEF"
HEX_A_DEC = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15,
}


def decimal_a_binario(numero):
    binario = ""
    while numero >= 2:
        resto = numero % 2
        binario = DIGITOS_BINARIOS[resto] + binario
        numero = numero // 2
    binario = DIGITOS_BINARIOS[numero] + binario
    return binario


def decimal_a_octal(numero):
    octal = ""
    while numero >= 8:
        resto = numero % 8
        octal = DIGITOS_OCTALES[resto] + octal
        numero = numero // 2
    octal = DIGITOS_OCTALES[numero] + octal
    return octal


def decimal_a_hexa(numero):
    hexa = ""
    while numero >= 16:
        resto = numero % 16
        digito = DIGITOS_HEXADECIMALES[resto]
        hexa = digito + hexa
        numero = numero // 16
    hexa = DIGITOS_HEXADECIMALES[numero] + hexa
    return hexa


def binario_a_decimal(binario):
    decimal = 0
    for i in range(len(binario)):
        digito = int(binario[-1 - i])
        decimal = decimal + digito * 2**i
    return decimal


def octal_a_decimal(octal):
    decimal = 0
    for i in range(len(octal)):
        digito = int(octal[-1 - i])
        decimal = decimal + digito * 8**i
    return decimal


def hexa_a_decimal(hexa):
    decimal = 0
    for i in range(len(hexa)):
        digito = HEX_A_DEC[hexa[-1 - i].upper()]
        decimal = decimal + digito * 16**i
    return decimal


def validar_octal(numero):
    for digito in numero:
        if not (digito in DIGITOS_OCTALES):
            return False
    return True


def validar_binario(numero):
    for digito in numero:
        if not (digito in DIGITOS_BINARIOS):
            return False
    return True


def validar_hexa(numero):
    for digito in numero:
        if not (digito in DIGITOS_HEXADECIMALES):
            return False
    return True

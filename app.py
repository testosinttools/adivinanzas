import random
from conversiones import *

conversiones = [
    "decimal_a_binario",
    "decimal_a_octal",
    "decimal_a_hexa",
    "binario_a_decimal",
    "octal_a_decimal",
    "hexa_a_decimal",
]


def generar_par_pregunta_respuesta(conversion, numero):

    pregunta = ""
    resultado_esperado = ""

    if conversion == "decimal_a_binario":
        resultado_esperado = decimal_a_binario(numero)
        pregunta = f"Cual es el valor binario que corresponde al decimal {numero}?: "

    elif conversion == "decimal_a_octal":
        resultado_esperado = decimal_a_octal(numero)
        pregunta = f"Cual es el valor octal que corresponde al decimal {numero}?: "

    elif conversion == "decimal_a_hexa":
        resultado_esperado = decimal_a_hexa(numero)
        pregunta = (
            f"Cual es el valor hexadecimal que corresponde al decimal {numero}?: "
        )

    elif conversion == "binario_a_decimal":
        resultado_esperado = binario_a_decimal(str(numero))
        pregunta = f"Cual es el valor decimal que corresponde al binario {numero}?: "

    elif conversion == "octal_a_decimal":
        resultado_esperado = octal_a_decimal(str(numero))
        pregunta = f"Cual es el valor decimal que corresponde al octal {numero}?: "

    elif conversion == "hexa_a_decimal":
        resultado_esperado = hexa_a_decimal(str(numero))
        pregunta = (
            f"Cual es el valor decimal que corresponde al hexadecimal {numero}?: "
        )

    return (pregunta, resultado_esperado)


def jugar():

    numero = random.randint(1, 100)

    conversion = random.choice(conversiones)

    (pregunta, resultado_esperado) = generar_par_pregunta_respuesta(conversion, numero)

    respuesta_usuario = input(pregunta).strip().lower()

    if respuesta_usuario == resultado_esperado:
        print("¡Correcto!")
    else:
        print(f"Incorrecto. El valor correcto era {resultado_esperado}.")


BIENVENIDA = """
***************************
Juego de Adivinanzas 
***************************
"""


def main():

    print(BIENVENIDA)

    jugando = True
    while jugando:

        jugar()

        continuar = input("\n¿Quieres jugar otra vez? (s/n): ").strip().lower()
        if continuar != "s":
            jugando = False

    print("¡Gracias por jugar! Hasta luego.")


main()

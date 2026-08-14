def dividir_numeros():

    try:

        numero1 = input("Escriba el primer numero:")
        numero2 = input("Escriba el segundo numero:")

        numero1 = int(numero1)
        numero2 = int(numero2)

        resultado = numero1 / numero2

        return resultado

    except ValueError:
        print("Error:El numero introducido no es valido")

    except ZeroDivisionError:
        print("Error:No se puede dividir entre cero")

    finally:
        print("Fin del programa")

dividir_numeros()
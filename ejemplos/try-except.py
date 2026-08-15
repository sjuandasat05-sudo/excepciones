# Sección 1 - Try-except
# Replica los ejemplos del material sobre la estructura try-except

# ---- Ejemplo básico: dividir dos números ----
try:
    numero1 = 10
    numero2 = 0
    resultado = numero1 / numero2
    print(f"El resultado es: {resultado}")
except:
    print("¡Ups! No se puede dividir entre cero.")


# ---- Capturando excepciones específicas ----
print("\n--- Capturando excepciones específicas ---")
try:
    numero = int(input("Introduce un número: "))
    resultado = 100 / numero
    print(f"100 dividido por {numero} es {resultado}")
except ZeroDivisionError:
    print("No puedes dividir entre cero.")
except ValueError:
    print("Debes introducir un número válido.")


# ---- Accediendo a la información de la excepción (con 'as error') ----
print("\n--- Accediendo a la información de la excepción ---")
try:
    with open("archivo_inexistente.txt", "r") as archivo:
        contenido = archivo.read()
except FileNotFoundError as error:
    print(f"Error: {error}")
    print("Creando un archivo nuevo...")
    with open("archivo_inexistente.txt", "w") as archivo:
        archivo.write("Este es un archivo nuevo")


# ---- Combinando múltiples excepciones en una tupla ----
print("\n--- Combinando múltiples excepciones ---")
try:
    archivo = open("archivo_inexistente.txt", "r")
    valor = int(archivo.readline().strip())
    resultado = 100 / valor
except (FileNotFoundError, ValueError, ZeroDivisionError) as e:
    print(f"Ocurrió un error: {type(e).__name__}")
    print(f"Descripción: {e}")


# ---- Uso práctico: pedir la edad hasta que sea válida ----
print("\n--- Uso práctico: obtener_edad() ---")

def obtener_edad():
    while True:
        try:
            edad = int(input("¿Cuál es tu edad? "))
            if edad < 0:
                print("La edad no puede ser negativa.")
                continue
            return edad
        except ValueError:
            print("Por favor, introduce un número entero.")

edad_usuario = obtener_edad()
print(f"Tu edad es: {edad_usuario}")

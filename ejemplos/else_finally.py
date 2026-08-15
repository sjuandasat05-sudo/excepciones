# Sección 3 - Else y finally
# Replica los ejemplos del material sobre estas dos cláusulas

# ---- else: se ejecuta solo si NO hubo ninguna excepción ----
print("--- Ejemplo de else ---")
try:
    numero = int(input("Introduce un número: "))
    resultado = 100 / numero
except ValueError:
    print("Debes introducir un número válido.")
except ZeroDivisionError:
    print("No puedes dividir entre cero.")
else:
    print(f"El resultado es: {resultado}")


# ---- else con archivos: solo cerramos si se abrió con éxito ----
print("\n--- else con manejo de archivos ---")
try:
    archivo = open("archivo_inexistente.txt", "r")
    contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe.")
    contenido = ""
else:
    print("Archivo leído correctamente.")
    archivo.close()


# ---- finally: se ejecuta SIEMPRE, haya error o no ----
print("\n--- Ejemplo de finally ---")
try:
    numero = int(input("Introduce un número para dividir 10: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")
except ZeroDivisionError:
    print("Error: División por cero")
except ValueError:
    print("Error: Valor no válido")
finally:
    print("Operación finalizada")


# ---- Combinando else y finally juntos ----
print("\n--- Combinando else y finally ---")
try:
    archivo = open("archivo_inexistente.txt", "r")
    contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe, se creará uno nuevo.")
    archivo = open("archivo_inexistente.txt", "w")
    archivo.write("Archivo creado automáticamente")
else:
    print(f"Contenido leído: {contenido}")
finally:
    print("Operación de archivo completada.")
    archivo.close()


# ---- Orden de ejecución: try -> except/else -> finally ----
print("\n--- Orden de ejecución ---")

def demostrar_orden():
    try:
        print("1. Ejecutando bloque try")
        # x = 1 / 0  # descomentar para ver cómo cambia el orden
    except ZeroDivisionError:
        print("2. Ejecutando bloque except")
    else:
        print("3. Ejecutando bloque else")
    finally:
        print("4. Ejecutando bloque finally")

    print("5. Continuando después del bloque try")

demostrar_orden()


# ---- finally se ejecuta ANTES de que el return entregue el valor ----
print("\n--- finally con return ---")

def dividir(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        print("Error: División por cero")
        return None
    finally:
        print("División finalizada")

print(dividir(10, 2))  # imprime "División finalizada" y luego 5.0
print(dividir(10, 0))  # imprime "Error...", "División finalizada" y luego None

# Sección 2 - Tipos comunes de excepciones
# Replica los ejemplos del material sobre las excepciones más frecuentes

# ---- Operaciones matemáticas ----
print("--- Excepciones matemáticas ---")

try:
    resultado = 5 / 0
except ZeroDivisionError:
    print("ZeroDivisionError: no es posible dividir entre cero")

try:
    resultado = 10.0 ** 1_000_000  # un número demasiado grande para representar
except OverflowError:
    print("OverflowError: el número es demasiado grande para ser representado")


# ---- Tipos de datos ----
print("\n--- Excepciones de tipos de datos ---")

try:
    resultado = "42" + 10
except TypeError:
    print("TypeError: no se pueden sumar tipos diferentes")

try:
    numero = int("abc")
except ValueError:
    print("ValueError: la cadena no representa un número válido")


# ---- Índices y claves ----
print("\n--- Excepciones de índices y claves ---")

try:
    lista = [1, 2, 3]
    elemento = lista[10]
except IndexError:
    print("IndexError: el índice está fuera del rango de la lista")

try:
    diccionario = {"nombre": "Ana", "edad": 25}
    valor = diccionario["telefono"]
except KeyError:
    print("KeyError: la clave 'telefono' no existe en el diccionario")


# ---- Archivos ----
print("\n--- Excepciones de archivos ---")

try:
    with open("archivo_que_no_existe.txt", "r") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("FileNotFoundError: el archivo no existe")

# PermissionError: ocurre al intentar escribir sin permisos suficientes.
# Se deja documentado en vez de ejecutarlo, porque el resultado depende
# de los permisos del sistema donde se corra (en algunos entornos no falla).
# try:
#     with open("/etc/passwd", "w") as archivo:
#         archivo.write("datos")
# except PermissionError:
#     print("PermissionError: no tienes permisos para modificar este archivo")


# ---- Atributos y nombres ----
print("\n--- Excepciones de atributos y nombres ---")

try:
    texto = "Hola"
    longitud = texto.size  # el correcto sería len(texto)
except AttributeError:
    print("AttributeError: el objeto string no tiene el atributo 'size'")

try:
    print(variable_no_definida)
except NameError:
    print("NameError: la variable no está definida")


# ---- Importaciones ----
print("\n--- Excepciones de importación ---")

try:
    import biblioteca_inexistente
except ImportError:
    print("ImportError: no se pudo importar el módulo")

try:
    import modulo_que_no_existe
except ModuleNotFoundError:
    print("ModuleNotFoundError: el módulo no existe")


# ---- Jerarquía de excepciones ----
print("\n--- Jerarquía de excepciones (capturando con Exception) ---")

try:
    resultado = int("abc") / 0
except Exception as e:
    print(f"Se produjo un error: {type(e).__name__}")
    print(f"Descripción: {e}")


# ---- Identificando el tipo de excepción dinámicamente ----
print("\n--- Identificando una excepción con type(e).__name__ ---")

try:
    lista = [1, 2, 3]
    print(lista[5])
except Exception as e:
    print(f"Error de tipo: {type(e).__name__}")
    print(f"Descripción: {e}")

# Nota: las excepciones de bibliotecas externas (como 'requests') se definen
# igual, heredando de Exception, pero no se ejecutan aquí porque requieren
# conexión a internet y una librería adicional instalada.

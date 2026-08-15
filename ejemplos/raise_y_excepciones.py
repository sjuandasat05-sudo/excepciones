# Sección 4 - Lanzar excepciones
# Replica los ejemplos del material sobre raise y excepciones personalizadas

# ---- raise básico ----
print("--- raise básico ---")

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")
    return a / b

try:
    resultado = dividir(10, 0)
except ZeroDivisionError as e:
    print(f"Error: {e}")


# ---- Validación de parámetros ----
print("\n--- Validación de parámetros ---")

def calcular_raiz_cuadrada(numero):
    if numero < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
    return numero ** 0.5

try:
    print(calcular_raiz_cuadrada(-9))
except ValueError as e:
    print(f"Error: {e}")


# ---- Precondiciones no cumplidas (simulando una cuenta simple) ----
print("\n--- Precondiciones no cumplidas ---")

class Cuenta:
    def __init__(self, saldo, activa=True):
        self.saldo = saldo
        self.esta_activa = activa

def retirar_dinero(cuenta, cantidad):
    if not cuenta.esta_activa:
        raise ValueError("La cuenta no está activa")
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser positiva")
    if cantidad > cuenta.saldo:
        raise ValueError("Saldo insuficiente")
    cuenta.saldo -= cantidad
    return cuenta.saldo

cuenta_prueba = Cuenta(saldo=1000)
try:
    retirar_dinero(cuenta_prueba, 5000)
except ValueError as e:
    print(f"Error: {e}")


# ---- Relanzar una excepción con raise (sin argumentos) ----
print("\n--- Relanzar una excepción ---")

def procesar_archivo(ruta):
    try:
        with open(ruta, "r") as archivo:
            return archivo.read()
    except FileNotFoundError as e:
        print(f"Registrando error: {e}")
        raise  # relanza la misma excepción para que la maneje quien llamó

try:
    procesar_archivo("no_existe.txt")
except FileNotFoundError:
    print("El error también fue manejado en el nivel de arriba")


# ---- raise ... from e (mantener el contexto original) ----
print("\n--- raise ... from e ---")

class ConfigurationError(Exception):
    pass

def obtener_configuracion(archivo):
    try:
        with open(archivo, "r") as f:
            return f.read()
    except FileNotFoundError as e:
        raise ConfigurationError(f"Archivo de configuración no encontrado: {archivo}") from e

try:
    obtener_configuracion("config.ini")
except ConfigurationError as e:
    print(f"Error: {e}")


# ---- Excepciones personalizadas ----
print("\n--- Excepciones personalizadas ---")

class SaldoInsuficienteError(Exception):
    """Se lanza cuando se intenta retirar más dinero del disponible."""

    def __init__(self, saldo, cantidad):
        self.saldo = saldo
        self.cantidad = cantidad
        self.deficit = cantidad - saldo
        mensaje = f"No hay suficiente saldo. Saldo: {saldo}, Cantidad solicitada: {cantidad}"
        super().__init__(mensaje)


def retirar(cuenta, cantidad):
    if cantidad > cuenta.saldo:
        raise SaldoInsuficienteError(cuenta.saldo, cantidad)
    cuenta.saldo -= cantidad
    return cuenta.saldo

try:
    retirar(cuenta_prueba, 5000)
except SaldoInsuficienteError as e:
    print(f"Error: {e}")
    print(f"Déficit: {e.deficit}")


# ---- Ejemplo práctico completo: validación de entrada de usuario ----
print("\n--- Ejemplo práctico: obtener_edad() con validación completa ---")

def obtener_edad():
    while True:
        try:
            entrada = input("Introduce tu edad: ")

            if not entrada.strip():
                raise ValueError("La entrada no puede estar vacía")

            edad = int(entrada)

            if edad < 0:
                raise ValueError("La edad no puede ser negativa")
            if edad > 120:
                raise ValueError("La edad parece demasiado alta")

            return edad

        except ValueError as e:
            print(f"Error: {e}")

edad_usuario = obtener_edad()
print(f"Tu edad es: {edad_usuario}")

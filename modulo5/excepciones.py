import math

# 1. Qué tipos de excepciones podríamos tratar en este código

x = int(input("Ingresa un numero: "))
y = 1 / x

try:
    x = int(input("Ingresa un numero: "))
    y = 1 / x
except ValueError:
    print("Oh cielos, algo salio mal...")
except ZeroDivisionError:
    print("No se puede dividir por 0")
except:
    print("Error desconocido")

print("FIN.")

# 2. Comportamiento de ZeroDivisionError vs Arithmeticerror

try:
    y = 1 / 0
except ZeroDivisionError:
    print("Uuuppsss...")

print("FIN.")

try:
    y = 1 / 0
except ArithmeticError as ae:
    print(ae)

print("FIN.")

# Qué pasa con esto??

try:
    y = 1 / 0
except ArithmeticError:
    print("¡Problema aritmético!")
except ZeroDivisionError:
    print("¡División entre Cero!")


print("FIN.")

# Excepciones dentro de funciones


def badFun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("¡Problema aritmético!")
    return None


badFun(0)

print("FIN.")


def badFun(n):
    return 1 / n


try:
    badFun(0)
except ArithmeticError:
    print("¿Que pasó? ¡Se lanzo una excepción!")

print("FIN.")

# raise y assert
# 1. raise en el cuerpo de una función


def badFun(n):
    raise ZeroDivisionError


try:
    badFun(0)
except ArithmeticError:
    print("¿Que pasó? ¿Un error?")

print("FIN.")

# 2. raise en el bloque except


def badFun(n):
    try:
        return n / 0
    except:
        print("¡Lo hice otra vez!")
        # podríamos usar este bloque, por ejemplo, para guardar el timestamp del
        # momento del error y poder hacer una visualización de él
        raise


try:
    badFun(0)
except ArithmeticError:
    print("¡Ya veo!")

print("FIN.")

# 3. assert


x = float(input("Ingresa un numero: "))
assert x >= 0.0

x = math.sqrt(x)

print(x)













# 1. Solucion
try:
    x = int(input("Ingresa un numero: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("No puedes dividir entre cero, lo siento.")
except ValueError:
    print("Debes ingresar un valor entero.")
except:
    print("Oh cielos, algo salio mal...")

print("THE END.")

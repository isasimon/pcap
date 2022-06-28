def readint(prompt, min, max):
    try:
        number = int(input(prompt))
        assert min < number < max
    except ValueError:
        print("Error: entrada incorrecta")
        number = readint(prompt, min, max)
    except AssertionError:
        print(f"Error: el valor no está dentro del rango permitido ({min} y {max})")
        number = readint(prompt, min, max)
    return number


v = readint("Ingrese un número del -10 al 10: ", -10, 10)
print("El numero es: ", v)


# Validar que el minimo es menor que el máximo

class InvertedRangeException(AssertionError):
    pass


def readint(prompt, min, max):
    try:
        if min > max:
            raise InvertedRangeException
        number = int(input(prompt))
        assert min < number < max
        return number
    except ValueError:
        print("Error: entrada incorrecta")
        readint(prompt, min, max)
    except InvertedRangeException:
        raise InvertedRangeException("El valor minimo del rango es mayor que el máximo")
    except AssertionError:
        print(f"Error: el valor no está dentro del rango permitido ({min} y {max})")
        readint(prompt, min, max)

v = readint("Ingrese un número del -10 al 10: ", 15, 10)
print("El numero es: ", v)










lst = [1, 2]

lst.insert(1, 6)

print(lst[-1])

for v in range(2):
    print(v)
    print(lst[v])
    lst.insert(-1, lst[v])

print(lst)



l = [0, 1, 4, 9, 16]

del l[4]

l

x = 1
y = 2

x, y, z = x, x, y
z, y, z = x, y, z



a = 1
b = 1
1 ^ 1



nums = [1, 2, 3]
vals = nums
del vals[:]

1 / 5



def fun(a, b, c=0):
    pass

fun(b=0)


tup = (1, 2, 4, 8)
tup = tup[-2:-1]



lst = [[x for x in range(3)] for i in range(3)]

for r in range(3):
    for c in range(3):
        print(f"Numerador: {lst[r][c]}, denominador: 2")
        if lst[r][c] % 2 != 0:

            print("#")


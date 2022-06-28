from math import ceil, floor, trunc, \
    e, exp, pow, log, \
    pi, radians, degrees, sin, cos, tan, asin
import os
from random import *

# Using math
print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))

x = 1.4
y = 2.6

print(floor(x), floor(y))
print(floor(-x), floor(-y))
print(ceil(x), ceil(y))
print(ceil(-x), ceil(-y))
print(trunc(x), trunc(y))
print(trunc(-x), trunc(-y))

ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)


# Using os
dir(os)


print(os.environ['PATH'])


# Using random
seed(1)  # Con la misma semilla obtenemos el mismo resultado de random (no hay aleatoriedad real)
print(random())


print(randrange(4), end=' ')  # Numero entero de 1 a 4
print(randrange(2, 5), end=' ')  # Numero entero entre 2 y 5 (no incluye 5)
print(randrange(0, 2, 6), end=' ')  # Numero entero entre 0 y 6 teniendo en cuenta solo los pares (incluye 6)
print(randint(0, 5))  # Devuelve integer incluyendo 5


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


print(f"Longitud de lst {len(lst)}")
print(choice(lst))  # Devuelve elemento aleatorio de una lista
print(sample(lst, 5))  # Devuelve otra lista con 5 elementos aleatoriamente escogidos de lst
print(sample(lst, 10))





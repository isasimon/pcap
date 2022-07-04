callable("Cualquier cadena")
callable(lambda x1, x2, x3: x1 + x2 + x3)

(lambda p1, p2, p3: print(p1, p2, p3))(1, 2, 3)

g = lambda p1, p2, p3: print(p1, p2, p3)
g(1, 2, 3)

def a(a1, a2):
    return a1 + a2


(lambda x, y, z: a(x, y) - z)(9, 8, 7)

(lambda n: (n ** 2, n ** 3))(4)

f = lambda y: y - 3

f(1)
f(2)

(lambda y: y - 3)(3)
(lambda y: y - 3)(2)


def accumulator(iter, acc, f):
    for i in iter:
        acc = f(acc, i)
    return acc


def resta(a, b):
    return a - b


result = accumulator([7, 5, 2], 10, resta)


acc_sum = lambda iter, acc: accumulator(iter, acc, lambda x, y: x + y)


acc_sum([7, 5, 2], 10)




import pandas as pd

df = pd.DataFrame([])









# Ejercicio fold / reduce


def fold(iter, acc, f):
    if acc is None:
        return acc
    else:
        for i in iter:
            acc = f(i, acc)
        return acc


fold([1, 2], 0, lambda x, y: x + y)
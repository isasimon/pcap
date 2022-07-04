def iteratodo(*args, **kwargs):
    for i in args:
        print(i)
    print("Sigo iterando xd")
    for key, value in kwargs.items():
        print(f"Clave {key}, valor {value}")
    return


iteratodo(1, 3, 'ertyu', key1="el", key2="último", key3="verano")
iteratodo(key2="último", key3="verano")
iteratodo(1, 3, 'ertyu')
iteratodo()


"""Usando funciones como objetos"""


def shout(text):
    return text.upper()


print(shout('Hello'))

yell = shout

print(yell('Hello'))


"""Pasando una función como argumento"""


def shout(text):
    return text.upper()


def whisper(text):
    return text.lower()


def greet(func):
    # storing the function in a variable
    greeting = func("""Hi, I am created by a function passed as an argument.""")
    print(greeting)


greet(shout)
greet(whisper)

"""Devolviendo una función desde otra"""


def create_adder(x):
    def adder(y):
        return x + y

    return adder


add_15 = create_adder(15)

print(add_15(10))

# Aaaalso:
print(create_adder(1)(2))


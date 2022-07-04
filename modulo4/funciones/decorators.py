"""Decoradores"""


# defining a decorator
def hello_decorator(func):
    # inner1 is a Wrapper function in
    # which the argument is called

    # inner function can access the outer local
    # functions like in this case "func"
    def inner1(*args):
        print("Hello, this is before function execution")

        # calling the actual function now
        # inside the wrapper function.
        value = func(*args)
        print("This is after function execution")
        return value

    return inner1


# defining a function, to be called inside wrapper
def function_to_be_used():
    print("This is inside the function !!")


def estoy_sumando_un_segundo(a, b):
    print("Empiezo a sumar")
    sum = a + b
    print(sum)
    return sum


# passing 'function_to_be_used' inside the
# decorator to control its behaviour
function_to_be_used = hello_decorator(function_to_be_used)


estoy_sumando_un_segundo = hello_decorator(estoy_sumando_un_segundo)





# calling the function
function_to_be_used()


@hello_decorator
def another_function_to_be_used():
    print("This is another function inside the function !!")


another_function_to_be_used()







##Ejercico

# importing libraries
import time
import math


# decorator to calculate duration
# taken by any function.
def calculate_time(func):
    # added arguments inside the inner1,
    # if function takes any arguments,
    # can be added like this.
    def inner1(*args, **kwargs):
        # storing time before function execution
        begin = time.time()

        func(*args, **kwargs)

        # storing time after function execution
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)

    return inner1


# this can be added to any function present,
# in this case to calculate a factorial
@calculate_time
def factorial(num):
    # sleep 2 seconds because it takes very less time
    # so that you can see the actual difference
    time.sleep(2)
    print(math.factorial(num))


# calling the function.
factorial(10)















def cuenta_regresiva(n):
    if n > 0:
        print(n)
        n -= 1
        cuenta_regresiva(n)
    else:
        print("Booom!")




def factorial(n, res=1):
    if n > 0:
        res = res * n
        n -= 1
        return factorial(n, res)
    else:
        return res


print(factorial(3))
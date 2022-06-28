# module.py

#!/usr/bin/env python3

""" module.py - an example of Python module """

__counter = 0


def custom_sum(my_list):
    global __counter
    __counter += 1
    sum = 0
    for el in my_list:
        sum += el
    return sum


def custom_prod(my_list):
    global __counter
    __counter += 1
    prod = 1
    for el in my_list:
        prod *= el
    return prod


if __name__ == "__main__":
    print("I prefer to be a module, but I can do some tests for you")
    my_list = [i+1 for i in range(5)]
    print(custom_sum(my_list) == 15)
    print(custom_prod(my_list) == 120)
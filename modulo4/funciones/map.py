animals = ['dog', 'cat', 'mouse']


def reverse(iterable):
    return iterable[::-1]


def upper(iterable):
    return iterable.upper()


a = map(upper, map(reverse, animals))


list(a)

# Cómo sería con una función lambda

stuffs = ('chair', 64.33, 'Cher')
reversed_stuffs = map(reverse, stuffs) # Qué pasara????

list(reversed_stuffs)

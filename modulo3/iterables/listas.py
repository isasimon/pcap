"""
OPERACIONES BÁSICAS DE UNA LISTA
"""

vocales = ['a', 'e']
vocales.insert(1, 'i')

print(vocales)

del vocales[0]

print(vocales)

# Diferencia entre pop y remove

l = list([1, 5, 3, 5, 10])

print(f"Initial list {l}")
my_remove = l.remove(5)
print(f"Removed elemente {my_remove}")
print(f"List after removing element 2 {l}")
my_pop = l.pop()
print(f"Poped element {my_pop}")
print(f"List after poping {l}")
my_pop_2 = l.pop(1)
print(f"List after poping index 1 {l}")


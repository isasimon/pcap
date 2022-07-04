""" Esto es un doc-string, que indica brevemente el propósito del módulo """

from sys import path  # path contiene las rutas donde python busca módulos

print(path)

path.append('C:\\Users\\User\\PycharmProjects\\pcap\\modulo5\\modules_examples')

# print(path)

from modules import module

prod = module.custom_prod([1, 2, 3, 4])
print(prod)


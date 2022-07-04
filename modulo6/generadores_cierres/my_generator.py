def potencias_de_2(n):
    potencia = 1
    for i in range(n):
        yield potencia
        potencia *= 2


for v in potencias_de_2(8):
    print(v)

# Se puede crear una lista comprimida
x = [x for x in potencias_de_2(5)]
print(x)

# Se puede castear a una lista
y = list(potencias_de_2(3))
print(y)
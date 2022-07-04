# constructor
class conClase:
    def __init__(self, valor=None):
        self.var = valor


obj1 = conClase("objeto")
obj2 = conClase()

print(obj1.var)
print(obj2.var)


# métodos privados
class conClase:
    def visible(self):
        print("visible")

    def __oculto(self):
        print("oculto")


obj = conClase()
obj.visible()

try:
    obj.__oculto()
except AttributeError:
    print("fallido")

obj._conClase__oculto()
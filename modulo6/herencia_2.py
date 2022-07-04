class Super:
    def __init__(self, nombre):
        self.nombre = nombre
        self.supVar = 2

    def __str__(self):
        return "Mi nombre es " + self.nombre + "."


class Sub(Super):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.subVar = 3


class Sub2(Sub):
    def __init__(self, nombre):
        Super.__init__(self, nombre)
        self.supVar = 9
        self.subVar = 10


obj = Sub("Andy")
obj2 = Sub2("Peter")

print(obj)
print(obj2)

print(obj.supVar)
print(obj.subVar)

# Las propiedades las busca primero en el objeto y luego en las superclases

print(obj2.supVar)
print(obj2.subVar)
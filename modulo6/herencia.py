# Sobrescribir propiedad __str__(self)
class Estrella:
    def __init__(self, nombre, galaxia):
        self.nombre = nombre
        self.galaxia = galaxia

    def __str__(self):
        return self.nombre + ' en la ' + self.galaxia


sol = Estrella("Sol", "Vía Láctea")
print(sol)


# Evaluamos los niveles de herencia con el método issubclass
class Vehiculo:
    pass


class VehiculoTerrestre(Vehiculo):
    pass


class VehiculoOruga(VehiculoTerrestre):
    pass


for cls1 in [Vehiculo, VehiculoTerrestre, VehiculoOruga]:
    for cls2 in [Vehiculo, VehiculoTerrestre, VehiculoOruga]:
        print(issubclass(cls1, cls2), end="\t")
    print()


# Evaluamos que clase instancian los objectos
class Vehiculo:
    pass


class VehiculoTerrestre(Vehiculo):
    pass


class VehiculoOruga(VehiculoTerrestre):
    pass


miVehiculo = Vehiculo()
miVehiculoTerrestre = VehiculoTerrestre()
miVehiculoOruga = VehiculoOruga()

for obj in [miVehiculo, miVehiculoTerrestre, miVehiculoOruga]:
    for cls in [Vehiculo, VehiculoTerrestre, VehiculoOruga]:
        print(isinstance(obj, cls), end="\t")
    print()
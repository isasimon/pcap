import time

"""
En este caso, el polimorfismo nos permite tener 
un único método girar cuya funcionalidad está 
centralizada en un solo punto. Si camiamos la implementación
de girar, todos girarán diferente y cada uno puede
tener su propia definición de cambiar dirección.
Permite mantener un código limpio y consistente
"""


class Vehiculo:
    # Método abstracto que será implementado en subclases
    def cambiardireccion(self, izquierda, on):
        pass

    def girar(self, izquierda):
        self.cambiardireccion(izquierda, True)
        time.sleep(0.25)
        self.cambiardireccion(izquierda, False)


class VehiculoOruga(Vehiculo):
    def control_de_pista(self, izquierda, alto):
        pass

    def cambiardireccion(self, izquierda, on):
        self.control_de_pista(izquierda, on)


class VehiculoTerrestre(Vehiculo):
    def girar_ruedas_delanteras(self, izquierda, on):
        pass

    def cambiardireccion(self, izquierda, on):
        self.girar_ruedas_delanteras(izquierda, on)
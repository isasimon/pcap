"""
La clase Vehículo puede ser instanciada
con diferentes controladores capaces de mover
el vehículo de diferente manera.
A diferencia de con la herencia, no llamamos
varias subclases con diferente funcionalidad
sino siempre a la clase Vehículo pasandole como
argumento diferente controlador
"""

import time


class Pistas:
    def cambiardireccion(self, izquierda, on):
        print("pistas: ", izquierda, on)


class Ruedas:
    def cambiardireccion(self, izquierda, on):
        print("ruedas: ", izquierda, on)


class Vehiculo:
    def __init__(self, controlador):
        self.controlador = controlador

    def girar(self, izquierda):
        self.controlador.cambiardireccion(izquierda, True)
        time.sleep(0.25)
        self.controlador.cambiardireccion(izquierda, False)


conRuedas = Vehiculo(Ruedas())
conPistas = Vehiculo(Pistas())

conRuedas.girar(True)
conPistas.girar(False)
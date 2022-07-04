from abstract_factory.fabrica import Fabrica
from abstract_factory.mesa.mesa import Mesa
from abstract_factory.silla.silla import Silla
from abstract_factory.fabrica_barroca import FabricaBarroca
from abstract_factory.fabrica_gotica import FabricaGotica


def client(abstract: Fabrica):
    mesa: Mesa = abstract.crearMesa()
    print(mesa.comer())

    silla: Silla = abstract.crearSilla()
    print(silla.sentarse())

    precio = silla.get_precio() + mesa.get_precio()

    print("El precio total de la estancia es ", str(precio))


if __name__ == '__main__':
    client(FabricaBarroca())

    client(FabricaGotica())
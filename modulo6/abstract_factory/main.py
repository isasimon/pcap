from abstract_factory.fabrica import Fabrica
from abstract_factory.fabrica_barroca import FabricaBarroca
from abstract_factory.fabrica_moderna import FabricaModerna


def client(abstract: Fabrica):
    mesa = abstract.crearMesa()
    print(mesa.comer())

    silla = abstract.crearSilla()
    print(silla.sentarse())

    precio = silla.get_precio() + mesa.get_precio()

    print("El precio total de la estancia es ", str(precio))


if __name__ == '__main__':
    client(FabricaBarroca())

    client(FabricaModerna())
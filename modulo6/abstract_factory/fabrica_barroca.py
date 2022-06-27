from abstract_factory.fabrica import Fabrica
from abstract_factory.silla.silla_barroca import SillaBarroca
from abstract_factory.mesa.mesa_barroca import MesaBarroca


class FabricaBarroca(Fabrica):
    def crearSilla(self) -> SillaBarroca:
        return SillaBarroca()

    def crearMesa(self) -> MesaBarroca:
        return MesaBarroca()
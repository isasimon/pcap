from abstract_factory.fabrica import Fabrica
from abstract_factory.silla.silla_gotica import SillaGotica
from abstract_factory.mesa.mesa_gotica import MesaGotica


class FabricaGotica(Fabrica):
    def crearMesa(self) -> MesaGotica:
        return MesaGotica()

    def crearSilla(self) -> SillaGotica:
        return SillaGotica()
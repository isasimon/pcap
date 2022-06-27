from abstract_factory.fabrica import Fabrica
from abstract_factory.mesa.mesa_moderna import MesaModerna
from abstract_factory.silla.silla_moderna import SillaModerna


class FabricaModerna(Fabrica):
    def crearSilla(self) -> SillaModerna:
        return SillaModerna()

    def crearMesa(self) -> MesaModerna:
        return MesaModerna()
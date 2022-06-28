from abc import ABC, abstractmethod
from abstract_factory.mesa.mesa import Mesa
from abstract_factory.silla.silla import Silla


class Fabrica(ABC):
    @abstractmethod
    def crearSilla(self) -> Silla:
        pass

    @abstractmethod
    def crearMesa(self) -> Mesa:
        pass
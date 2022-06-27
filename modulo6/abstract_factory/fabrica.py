from abc import ABC, abstractmethod


class Fabrica(ABC):
    @abstractmethod
    def crearSilla(self):
        pass

    @abstractmethod
    def crearMesa(self):
        pass
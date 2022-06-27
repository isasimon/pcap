from abc import ABC, abstractmethod


class Silla(ABC):
    @abstractmethod
    def sentarse(self):
        pass
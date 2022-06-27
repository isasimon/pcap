from abc import ABC, abstractmethod


class Silla(ABC):
    @abstractmethod
    def sentarse(self) -> str:
        pass

    @abstractmethod
    def get_precio(self) -> int:
        pass
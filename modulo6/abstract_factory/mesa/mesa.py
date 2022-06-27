from abc import ABC, abstractmethod


class Mesa(ABC):
    @abstractmethod
    def comer(self) -> str:
        pass

    @abstractmethod
    def get_precio(self) -> int:
        pass
from abstract_factory.silla.silla import Silla


class SillaBarroca(Silla):
    def sentarse(self) -> str:
        return "Me siento en mi silla barroca"

    def get_precio(self) -> int:
        return 20
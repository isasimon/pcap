from abstract_factory.silla.silla import Silla


class SillaGotica(Silla):
    def sentarse(self) -> str:
        return "Me siento en una silla gótica"

    def get_precio(self) -> int:
        return 7
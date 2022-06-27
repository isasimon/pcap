from abstract_factory.silla.silla import Silla


class SillaModerna(Silla):
    def sentarse(self) -> str:
        return "Me siento en mi silla moderna"

    def get_precio(self) -> int:
        return 5

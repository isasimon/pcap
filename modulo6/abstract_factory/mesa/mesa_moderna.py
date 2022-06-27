from abstract_factory.mesa.mesa import Mesa


class MesaModerna(Mesa):
    def comer(self) -> str:
        return "Como en mi mesilla moderna :O"

    def get_precio(self) -> int:
        return 10
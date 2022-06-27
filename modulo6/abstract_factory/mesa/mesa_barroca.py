from abstract_factory.mesa.mesa import Mesa


class MesaBarroca(Mesa):
    def comer(self) -> str:
        return "Como en mi mesa barroca :)"

    def get_precio(self) -> int:
        return 25
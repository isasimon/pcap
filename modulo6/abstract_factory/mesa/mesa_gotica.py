from abstract_factory.mesa.mesa import Mesa


class MesaGotica(Mesa):
    def comer(self) -> str:
        return "Estoy comiendo en una mesaa gótica"

    def get_precio(self) -> int:
        return 13


if __name__ == '__main__':
    mesa = MesaGotica()
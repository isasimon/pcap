class Pila:
    def __init__(self):
        self.__listaPila = []

    def push(self, val):
        self.__listaPila.append(val)

    def pop(self):
        val = self.__listaPila[-1]
        del self.__listaPila[-1]
        return val


class SumaPila(Pila):
    def __init__(self):
        Pila.__init__(self)
        # Variable privada. Solo accesible mediante un get
        self.__sum = 0

    # push  de la superclase queda anulado
    def push(self, val):
        Pila.push(self, val)
        self.__sum += val

    def pop(self):
        val = Pila.pop(self)
        self.__sum -= val
        return val


if __name__ == '__main__':
    suma_pila = SumaPila()
    suma_pila.push(3)
    suma_pila.push(2)
    suma_pila.push(1)
    print(suma_pila._Pila__listaPila)
    suma_pila.__otra_lista = []



class PizzaError(Exception):
    def __init__(self, pizza, mensaje):
        Exception.__init__(self, mensaje)
        self.pizza = pizza


class NoPizzaError(PizzaError):
    def __init__(self, pizza, mensaje):
        PizzaError.__init__(self, pizza, mensaje)
        self.pizza = pizza

    def __str__(self):
        return "La pizza " + self.pizza + " no está en el menú"


class DemasiadoQuesoError(PizzaError):
    def __init__(self, pizza, queso, mensaje):
        PizzaError.__init__(self, pizza, mensaje)
        self.queso = queso

    def __str__(self):
        return "La cantidad de queso " + str(self.queso) + " es demasiado."


def makePizza(pizza, queso):
    if pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise NoPizzaError(pizza, "no esta en el menu")
    if queso > 100:
        raise DemasiadoQuesoError(pizza, queso, "demasiado queso")
    print("¡Pizza lista!")


for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
    try:
        makePizza(pz, ch)
    except DemasiadoQuesoError as tmce:
        print(tmce)
    except NoPizzaError as pe:
        print(pe)
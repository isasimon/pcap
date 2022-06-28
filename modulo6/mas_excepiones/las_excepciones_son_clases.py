# Las excepciones son clases
try:
    i = int("Hola!")
except Exception as e:
    print(e)
    print(e.__str__())


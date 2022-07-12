# Ejemplo erroneo
def exterior(par):
    loc = par


var = 1
exterior(var)

print(var)
print(loc) # No hay forma de acceder a loc


# Hacemos loc accesible desde fuera
def exterior(par):
    loc = par

    def interior():
        return loc
    return interior


var = 1
fun = exterior(var) # Almacenas la función en fun
print(type(fun))
print(fun()) # Invocas fun


# Par qué podemos usar esto??
def crearcierre(par):
    loc = par

    def potencia(p):
        return p ** loc
    return potencia


sqr = crearcierre(2)
cube = crearcierre(3)

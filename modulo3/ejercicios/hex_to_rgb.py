codigo_hex = input("Ingrese un color en código hexadecimal con el formato #XXXXXX")

#09FFBF
#000009
#0000FF

# Eliminamos el caracter # del principio de la cadena y lo transformamos
# a int16
codigo_hex = codigo_hex.lstrip('#')
print(type(codigo_hex))

codigo_integer = int(codigo_hex, 16)
print(codigo_integer)

# Calculamos el rojo desplazando 16 bits a la derecha
rojo = codigo_integer >> 16
print(rojo)
# Calculamos el verde deslazando 8 bits a la derecha
# y aplicando una máscara para quedarnos con los 8 últimos bits
verde = codigo_integer >> 8
print(verde)
verde_mascara = 0x00FF
verde &= verde_mascara
print(verde)





# Aplicamos una máscara para quedarlos los 8 últimos bits
azul_mascara = 0x0000FF


azul = codigo_integer & azul_mascara
print(f"rgb({rojo}, {verde}, {azul})")


"""
Tu tarea aquí es: ¡Debes diseñar un devorador de vocales usando:

Un ciclo for.
El concepto de ejecución condicional (if-elif-else ).
La declaración continue.
Tu programa debe:

Pedir al usuario que ingrese una palabra en la variable useWord.
Utilizar userWord = userWord.upper() para convertir la palabra ingresada por el usuario a mayúsculas.
Usa la ejecución condicional y la instrucción continue para "comer" las siguientes vocales A , E , I , O , U
de la palabra ingresada.
Asigne las letras no consumidas a la variable palabrasinVocal e imprime la variable en la pantalla.
Analiza el código en el editor. Hemos creado palabrasinVocal y le hemos asignado una cadena vacía.
Utiliza la operación de concatenación para pedirle a Python que combine las letras seleccionadas en una cadena
más larga durante los siguientes giros de ciclo, y asignarlo a la variable palabrasinVocal.

Prueba tu programa con los datos que le proporcionamos.

Entrada: Gregory
Salida: GRGRY


Entrada: abstemious
Salida: BSTMS
"""
















userWord = input("Ingrese una palabra.")
userWord = userWord.upper()

palabraSinVocal = ""

for letra in userWord:
    if letra == 'A':
        continue
    elif letra == 'E':
        continue
    elif letra == 'I':
        continue
    elif letra == 'O':
        continue
    elif letra == 'U':
        continue
    else:
        palabraSinVocal = palabraSinVocal + letra

print(palabraSinVocal)


# Forma alternativa comprimida
userWord = input("Ingrese una palabra.")
userWord = userWord.upper()
listaVocales = ['A', 'E', 'I', 'O', 'U']
palabraSinVocal = ""

for letra in userWord:
    if letra in listaVocales:
        continue
    else:
        palabraSinVocal = palabraSinVocal + letra

print(palabraSinVocal)

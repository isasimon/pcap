"""
Un niño y su padre están construyendo una pirámide.

Su pirámide es un poco rara, ya que en realidad es una pared en forma de pirámide, es plana.
La pirámide se apila de acuerdo con un principio simple: cada capa inferior contiene un bloque más que la capa superior.
Como se ilustra aquí
      ______
      |    |
    __________
   |    |    |
 _______________
|    |    |    |
________________

Tu tarea es escribir un programa que lea la cantidad de bloques que tienen los constructores,
y generar la altura de la pirámide que se puede construir utilizando estos bloques.

Nota: La altura se mide por el número de capas completas: si los constructores no tienen la
cantidad suficiente de bloques y no pueden completar la siguiente capa, terminan su trabajo inmediatamente.


Datos de prueba:

Número de bloques: 6
Altura: 3


Número de bloques:20
Altura: 6


Número de bloques: 1000
Altura: 44


Número de bloques: 2
Altura: 1
"""












bloques = int(input("Ingrese el número de bloques: "))
altura = 0

while bloques > altura:
    altura += 1
    bloques -= altura
else:
    print("La altura de la pirámide:", altura)

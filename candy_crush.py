import os
from funciones import *
# Hacer el bucle del juego principal !!
print("Bienvenido Al Candy Crush!!! Estas listo para arrancar!?????")
lista_candy = generar_lista(4,7)
imprimir_piezas(lista_candy)
cordenadas = ingresar_posicion()
resultado = verificar_vertical(lista_candy, cordenadas)
print(resultado[0])
generar_csv("Candycrush\JugadoresCandy1.csv",[resultado[1], resultado[2]])

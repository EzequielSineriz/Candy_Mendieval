import random
import pygame
ancho_celda = 55
alto_celda =  65
lista_piezas = {
    1: pygame.transform.scale(pygame.image.load("Candycrush/imagenes/cabeza_mago.jpg"), (ancho_celda, alto_celda)),
    2: pygame.transform.scale(pygame.image.load("Candycrush/imagenes/Candy_Hechizo.jpg"), (ancho_celda, alto_celda)),
    3: pygame.transform.scale(pygame.image.load("Candycrush/imagenes/Candy_poder.jpg"), (ancho_celda, alto_celda)),
}



def generar_lista(filas, columnas)->list:
    """Me Genera una lista de diccionarios con numeros random(1-3) en las filas y columnas"""
    lista = []
    for i in range(filas):
        piezas = []
        for j in range(columnas):
            pieza_random = random.randint(1, 3)
            pieza = lista_piezas[pieza_random]
            piezas.append(pieza) 
        diccionario = {"piezas": piezas}
        lista.append(diccionario)
    return lista


def ingresar_posicion()->list:
    """Ingresa fila y columna verifica que sea de 0-3(fila), y de 0-6(columna) retorna [fila,columna] """
    fila = pedir_numero_en_rango("ingrese la fila desde " , 0, 3)
    columna = pedir_numero_en_rango("Ingrese la fila desde " , 0, 6)
    return [fila, columna]



def verificar_vertical(lista_diccionarios, fila, columna):
    """Funcion principal de la logica del juego, verifica si hay coincidencia si gano o perdio el jugador
        Devuelve como parametro una lista[], con 2 booleanos de ganador, perdedor
    """
    
    numero = lista_diccionarios[fila]["piezas"][columna]
    conteo= contar_en_direccion(lista_diccionarios, fila, len(lista_diccionarios), 1, columna, numero)#+1 para que itere de arriba para abajo
    ganador = False
    
    if (conteo) >= 3:
        ganador = True
        perdedor = False
    else:
        ganador = False
        perdedor = True    
    
    return ganador, perdedor

def pedir_numero_en_rango(mensaje:str,desde:int, hasta:int):
    numero = int(input(mensaje + str(desde) + " y " + str(hasta) + ": "))
    while numero < desde or numero > hasta:
        print("El número ingresado no está en el rango " + str(desde) + "-" + str(hasta) + ".")
        numero = int(input("Ingrese un número entre " + str(desde) + " y " + str(hasta) + ": "))
    return numero

def imprimir_piezas(lista:list):
    "Verificacion de las piezas para comprobar valores"
    for i in range(len(lista)):
        piezas = lista[i]["piezas"]
        for j in range(len(piezas)):
            print(piezas[j], end=" ")
        print("")



def generar_csv(nombre_archivo: str, jugador: list):
    """Genera un csv, y me retorna la linea del nombre del jugador(str), y el puntaje(int)"""
    with open(nombre_archivo, "a") as archivo:
        linea = "Jugador: {0}, Puntaje: {1}\n"
        linea = linea.format(jugador[0], jugador[1])
        archivo.write(linea)
    return linea



def contar_en_direccion(lista_diccionarios, fila_inicio, fila_fin, paso, columna, numero):
    """le paso una lista de diccionaros y me hace un for con las piezas verificando si el {numero}, que le paso
        por parametro llega o no llega a ser cont = 3, para retornas despues el valor y verificar"""
    conteo = 0
    
    for i in range(fila_inicio, fila_fin, paso):
        if lista_diccionarios[i]["piezas"][columna] == numero:
            conteo += 1
        else:
            break  #deja de contar si el numero no coincide

    # contar hacia arriba
    for i in range(fila_inicio - 1, -1, -1): 
        if lista_diccionarios[i]["piezas"][columna] == numero:
            conteo += 1
        else:
            break  

    return conteo


def dibujar_menu(ventana, imagen_fondo, posicion_imagen, texto, 
                 boton_jugar, posicion_boton_jugar, 
                 boton_sonido_on, posicion_boton_on, 
                 boton_sonido_off, posicion_boton_off, 
                 boton_config, posicion_boton_config, color_fondo):
    """
    DIBUJA EL MENU EN LA VENTANA
    Parametros:
    - ventana: Imagen de pygame donde se dibuja el menu
    - imagen_fondo: Imagen de fondo del menu
    - posicion_imagen: Cordenadas de la imagen de fondo
    - texto: Texto a mostrar
    - boton_jugar: Imagen del boton de jugar
    - posicion_boton_jugar: Coordenadas del boton de jugar
    - boton_sonido_on: Imagen del boton de sonido activado
    - posicion_boton_on: Coordenadas del boton de sonido
    - boton_sonido_off: Imagen del boton de sonido
    - posicion_boton_off: Coordenadas del botón de sonido desactivado
    - boton_config: Imagen del boton de configuración
    - posicion_boton_config: Coordenadas del botón de configuracion
    - color_fondo: Color de fondo de la ventana
    """
    ventana.fill(color_fondo)
    ventana.blit(imagen_fondo, posicion_imagen)
    ventana.blit(texto, (150, 380))  # Coordenadas del texto
    ventana.blit(boton_jugar, posicion_boton_jugar)
    ventana.blit(boton_sonido_on, posicion_boton_on)
    ventana.blit(boton_sonido_off, posicion_boton_off)
    ventana.blit(boton_config, posicion_boton_config)
    # if conteo >= 3

def dibujar_tablero(ventana, tablero, ancho_celda, alto_celda):

    """Dibuja, blitea, y crea los rect con el ancho_celda, y alto_celda, le paso un parametro
        el tablero lo recorro con un for y creo una lista rect que me va a tener los rect creados para 
        las piezas bliteadas """
    lista_rects = []
    pix_der_x = 81 # me da la proporcion de pixeles a la derecha que me va a aparecer de la pantalla
    pix_der_y = 150 # me da la proporcion de pixeles del indice y para abajo 
    fila_indice = 0  # contador para las filas
    for fila in tablero:  # Recorrer las filas del tablero
        columna_indice = 0 
        fila_rects = []
        for pieza in fila["piezas"]:  # Recorrer las piezas de la fila
            x = pix_der_x + columna_indice * ancho_celda    # Coordenada X #columna indice arranca en 0 que va a ser la 1 posicion va a guardar la primer imagen
            y = pix_der_y + fila_indice * alto_celda  # Coordenada Y                        #
            ventana.blit(pieza, (x, y)) 
            # Crear y almacenar el Rect
            rect = pygame.Rect(x, y, ancho_celda, alto_celda)
            fila_rects.append((rect, fila_indice, columna_indice))  # Guardar también el índice #para verificar retorno si estoy tocando un rect
            columna_indice += 1 
        lista_rects.append(fila_rects) 
        fila_indice += 1  #
    return lista_rects



def mostrar_resultado(ventana, resultado, posicion_imagen_victoria, posicion_imagen_derrota, imagen_victoria, imagen_derrota):
    
    if resultado:
        ventana.blit(imagen_victoria, posicion_imagen_victoria)
    else:
        ventana.blit(imagen_derrota, posicion_imagen_derrota)





             
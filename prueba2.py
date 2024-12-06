import pygame
import constantes
from funciones import *




pygame.init() # Iniciamos la libreria pygames
ventana = pygame.display.set_mode((constantes.ANCHO, constantes.ALTO)) # le pasamos los parametros
pygame.display.set_caption("Candy Medieval") # Le cambio el nombre de la ventana de mi juego

# Defino un Timer
timer_segundos = pygame.USEREVENT
pygame.time.set_timer(timer_segundos, 1000)  # Cada 1000 ms (1 segundo)
posicion_imagen_timer = [477, 105]
segundos = 30  # Tiempo inicial en segundos
fin_tiempo = False

# cargar una fuente personalizada (archivo TTF)
fuente_medieval = pygame.font.Font("Candycrush/MedievalSharp.ttf", 65)


#Defino texto
fuente = pygame.font.SysFont("Candycrush/MedievalSharp.ttf", 70)
ingreso = ""
ingreso_rect = pygame.Rect(200,270,200,35)
#el rect para que accione al nombre
font_input = pygame.font.SysFont("Arial", 20)

#Cargamos y Montamos el primer fondo de Pantalla
imagen_fondo = pygame.image.load("Candycrush/fondomed.jpg")
imagen_fondo = pygame.transform.scale(imagen_fondo,(800,600))
posicion_imagen =[0,0]
#Cargamos el fondo de pantalla_juego
fondo_pantalla_juego = pygame.image.load("Candycrush/imagenes/Fondo.png")
fondo_pantalla_juego = pygame.transform.scale(fondo_pantalla_juego,(800,600))
posicion_imagen =[0,0]


# cargamos y montamos el boton jugar
boton_jugar = pygame.image.load("Candycrush/imagenes/botonjugara.jpg")
boton_jugar = pygame.transform.scale(boton_jugar,(85,80))
posicion_imagen_boton_jugar = [340,500]
rect_boton_jugar = pygame.Rect(posicion_imagen_boton_jugar[0], posicion_imagen_boton_jugar[1], 85, 80)#LE PONGO EL MISMO PARAMETRO PARA QUE TOQUE CUALQUIER SUPE
                                                                                                      #RFICIE DEL BOTON Y ME DEVUELVA EL TRUE                                                             
# cargamos y montamos el sonido On le ponemos un rect para que reacione al eventpos
boton_sonido_on = pygame.image.load("Candycrush/imagenes/sonido_on.png")
boton_sonido_on = pygame.transform.scale(boton_sonido_on,(35,35))
posicion_boton_on = [750, 70]
rect_boton_on = pygame.Rect(posicion_boton_on[0],posicion_boton_on[1], 35, 35)
#Boton OFF
boton_sonido_off = pygame.image.load("Candycrush/imagenes/sonido_off.png")
boton_sonido_off = pygame.transform.scale(boton_sonido_off,(35,35))
posicion_boton_off = [750, 20]
rect_boton_off = pygame.Rect(posicion_boton_off[0],posicion_boton_off[1], 35, 35)
#Boton Configuracion De Vista
boton_config = pygame.image.load("Candycrush/imagenes/boton_config.png")
boton_config = pygame.transform.scale(boton_config,(35,35))
posicion_boton_config = [750, 120]
#creo el  nick del personaje
nick = pygame.image.load("Candycrush/imagenes/rect_nombre.png")
nick = pygame.transform.scale(nick,(200,35))
posicion_nick = [200, 270]



texto = fuente_medieval.render("Candy Medieval", True, (255, 146, 8))  # 

#defino musica
pygame.mixer.init()
sonido_fondo = pygame.mixer.Sound("Candycrush/sonidos/5.mp3")
volumen = 0.09
sonido_fondo.set_volume(volumen)
#Cargo musica winner
sonido_win = pygame.mixer.Sound("Candycrush/sonidos/44.wav")
sonido_win.set_volume(volumen)
#Cargo musica loser
sonido_loser = pygame.mixer.Sound("Candycrush/sonidos/45.wav")
sonido_loser.set_volume(volumen)

posicion_grilla = [150, 150]
fin_tiempo = False

en_menu= True
run = True
musica_encendida = True
sonido_fondo.play()
ancho_celda = 65 #55
alto_celda = 75 #65

filas = 4
columnas = 7
#Generar tablero
tablero = generar_lista(filas, columnas)

lista_piezas = {
    1: pygame.transform.scale(pygame.image.load("Candycrush/imagenes/cabeza_mago.jpg"), (ancho_celda, alto_celda)),
    2: pygame.transform.scale(pygame.image.load("Candycrush/imagenes/Candy_Hechizo.jpg"), (ancho_celda, alto_celda)),
    3: pygame.transform.scale(pygame.image.load("Candycrush/imagenes/Candy_poder.jpg"), (ancho_celda, alto_celda)),
}
lista_rects = dibujar_tablero(ventana,tablero,ancho_celda,alto_celda)
print(lista_rects)
pos= []


#Cargamos el cuadro de victoria
victoria_cuadro = pygame.image.load("Candycrush/imagenes/Victoria.png")
victoria_cuadro = pygame.transform.scale(victoria_cuadro,(450,200))
posicion_victoria_cuadro = [70,-18]
#Imagen de derrota cuadro
derrota_cuadro = pygame.image.load("Candycrush/imagenes/imagen_derrota.png")
derrota_cuadro = pygame.transform.scale(derrota_cuadro,(400,200))
posicion_derrota_cuadro = [100, -15]

#Cargamos imagen nick del personaje
nombre_personaje = pygame.image.load("Candycrush/imagenes/Personaje.png")
nombre_personaje = pygame.transform.scale(nombre_personaje,(300,450))
posicion_nombre_personaje = [155,150]

#Cargamos el goblin de oro
goblin_oro = pygame.image.load("Candycrush/imagenes/goblin_oro.png")
goblin_oro = pygame.transform.scale(goblin_oro,(100,100))
posicion_goblin_oro = [0,0]

#Cargamos monedas de oro
monedas_oro = pygame.image.load("Candycrush/imagenes/coin.png")
monedas_oro = pygame.transform.scale(monedas_oro,(30,30))
posicion_monedas_oro = [50,115]

#Cargamos moneda de oro x100
oro_cien = pygame.image.load("Candycrush/imagenes/100.png")
oro_cien = pygame.transform.scale(oro_cien,(45,45))
posicion_oro_cien = [80,107]

# cargamos moneda 0 oro
cero_moneda = pygame.image.load("Candycrush/imagenes/cero.png")
cero_moneda = pygame.transform.scale(cero_moneda,(20,30))
posicion_cero_moneda = [85,110]

#Crear el rect de siguiente
#siguiente_cuadro = pygame.image.load("Candycrush/imagenes/rect_nombre.png")
#siguiente_cuadro = pygame.transform.scale(siguiente_cuadro,(100,25))
posicion_siguiente_cuadro = [313,545] ###############

#creamos las flags para los sonidos reproducidos de ganador o perdedor
sonido_win_reproducido = False
sonido_loser_reproducido = False




resultado = bool
flag_perdedor = False
while run == True:
    # lo llenamos de un color de fondo para que cuando renueva se renueve la pantalla
    ventana.fill(constantes.COLOR_BG) 
    
    for event in pygame.event.get():# me entrega todos los eventos que ocurren en el juego
        if event.type == pygame.QUIT:# tipo de evento que realizo, apreto la x cambio el valor del run
            run = False
        
        if en_menu:
            dibujar_menu(
            ventana = ventana,
            imagen_fondo = imagen_fondo,
            posicion_imagen = posicion_imagen,
            texto = texto,
            boton_jugar = boton_jugar,
            posicion_boton_jugar = posicion_imagen_boton_jugar,
            boton_sonido_on = boton_sonido_on,
            posicion_boton_on = posicion_boton_on,
            boton_sonido_off = boton_sonido_off,
            posicion_boton_off = posicion_boton_off,
            boton_config = boton_config,
            posicion_boton_config = posicion_boton_config,
            color_fondo = constantes.COLOR_BG)
        

            if event.type == pygame.MOUSEBUTTONDOWN:  #detectar clics
                if rect_boton_jugar.collidepoint(event.pos) and en_menu:
                    en_menu = False  # cambia a la pantalla del juego
                if rect_boton_on.collidepoint(event.pos) and musica_encendida == False:
                    sonido_fondo.play()
                    musica_encendida = True 
                #Poner bandera para identificar si esta prendido o apagado alguno.
                if rect_boton_off.collidepoint(event.pos) and musica_encendida == True:
                    sonido_fondo.stop()
                    musica_encendida = False
                conteo = 0
        if en_menu == False:  
            fila_index = 0  # Inicializamos el índice de la fila
            for fila_rects in lista_rects:  # Recorremos las filas
                col_index = 0  # Inicializamos el índice de la columna para cada fila
                for celda in fila_rects:  # Recorremos las celdas dentro de cada fila
                    rect = celda[0]  # Obtenemos solo el rect de la celda
                    if rect.collidepoint(event.pos):  # Verificamos colisión con el clic
                        print("Hiciste clic en un rect.")
                            # Pasamos los índices a verificar_vertical
                        conteo, flag_perdedor = verificar_vertical(tablero, fila_index, col_index)
                        col_index += 1  # Incrementamos el índice de la columna
                    fila_index += 1  # Incrementamos el índice de la fila
            if event.type == pygame.USEREVENT :
                    if event.type == timer_segundos:
                        if fin_tiempo == False:
                            segundos = int(segundos) - 1
                        if int(segundos) == 0:
                            fin_tiempo = True
                            segundos = "0"

        if event.type == pygame.KEYDOWN and en_menu == False:
                if event.key == pygame.K_BACKSPACE:
                    ingreso = ingreso[0:-1]
                else:
                    ingreso += event.unicode

    if en_menu:
        dibujar_menu(
            ventana = ventana,
            imagen_fondo = imagen_fondo,
            posicion_imagen = posicion_imagen,
            texto = texto,
            boton_jugar = boton_jugar,
            posicion_boton_jugar = posicion_imagen_boton_jugar,
            boton_sonido_on = boton_sonido_on,
            posicion_boton_on = posicion_boton_on,
            boton_sonido_off = boton_sonido_off,
            posicion_boton_off = posicion_boton_off,
            boton_config = boton_config,
            posicion_boton_config = posicion_boton_config,
            color_fondo = constantes.COLOR_BG)
        

    else:
        posicion_boton_on = [675, 555]
        rect_boton_on = pygame.Rect(posicion_boton_on[0],posicion_boton_on[1], 35, 35)#Preguntar
        posicion_boton_off = [720, 555]
        rect_boton_off = pygame.Rect(posicion_boton_off[0],posicion_boton_off[1], 35, 35)#Preguntar si esta bien
        posicion_boton_config = [630, 555]
        ventana.fill((constantes.COLOR_BG))  
        ventana.blit(fondo_pantalla_juego,posicion_imagen)
        ventana.blit(boton_sonido_on, posicion_boton_on)
        ventana.blit(boton_sonido_off, posicion_boton_off)
        ventana.blit(boton_config, posicion_boton_config)
        segundos_texto = fuente.render(str(segundos), True, constantes.RED2 )
        ventana.blit(segundos_texto, [280, 110])
        dibujar_tablero(ventana, tablero, ancho_celda, alto_celda)
        if conteo == True:
            ventana.blit(victoria_cuadro, posicion_victoria_cuadro)
            sonido_fondo.stop()
            if sonido_win_reproducido == False:
                sonido_win.play()
                sonido_win_reproducido = True
            ventana.blit(nombre_personaje,posicion_nombre_personaje)
            ventana.blit(goblin_oro, posicion_goblin_oro)
            ventana.blit(monedas_oro,posicion_monedas_oro)
            ventana.blit(oro_cien, posicion_oro_cien)
            ventana.blit(nick,posicion_nick)
            
            pygame.draw.rect(ventana, constantes.BLACK, ingreso_rect , 2)
            #MUESTRO LA CAJA DE TEXTO PARA QUE INGRESE UN TEXTO
            font_input_surface = font_input.render(ingreso, True, constantes.TURQUOISEBLUE) 
            ventana.blit(font_input_surface, ( ingreso_rect.x+5 , ingreso_rect.y + 5 )) 
            #ventana.blit(siguiente_cuadro,posicion_siguiente_cuadro)
            rect_boton_siguiente = pygame.Rect(posicion_siguiente_cuadro[0],posicion_siguiente_cuadro[1], 100, 25)
            
        if flag_perdedor == True:
            ventana.blit(derrota_cuadro, posicion_derrota_cuadro)
            sonido_fondo.stop()
            if sonido_loser_reproducido == False:
                sonido_loser.play()
                sonido_loser_reproducido = True
            ventana.blit(nombre_personaje,posicion_nombre_personaje)
            ventana.blit(goblin_oro, posicion_goblin_oro)
            ventana.blit(monedas_oro,posicion_monedas_oro)
            ventana.blit(cero_moneda, posicion_cero_moneda)
            ventana.blit(nick,posicion_nick)
            pygame.draw.rect(ventana, constantes.BLACK, ingreso_rect , 2)
            #MUESTRO LA CAJA DE TEXTO PARA QUE INGRESE UN TEXTO
            font_input_surface = font_input.render(ingreso, True, constantes.TURQUOISEBLUE) 
            ventana.blit(font_input_surface, ( ingreso_rect.x+5 , ingreso_rect.y + 5 )) 
            #ventana.blit(siguiente_cuadro,posicion_siguiente_cuadro)
            rect_boton_siguiente = pygame.Rect(posicion_siguiente_cuadro[0],posicion_siguiente_cuadro[1], 200, 35)
            
     

    pygame.display.flip()

pygame.quit

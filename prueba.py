import pygame
import constantes
from funciones import *

# Inicializamos pygame
pygame.init()

# Configuración de la ventana
ventana = pygame.display.set_mode((constantes.ANCHO, constantes.ALTO))
pygame.display.set_caption("Candy Medieval")

# Definición de Timer
timer_segundos = pygame.USEREVENT
pygame.time.set_timer(timer_segundos, 1000)  # Cada 1000 ms (1 segundo)
posicion_imagen_timer = [477, 105]
segundos = 30
fin_tiempo = False

# Fuente personalizada
fuente_medieval = pygame.font.Font("Candycrush/MedievalSharp.ttf", 65)

# Texto y caja de ingreso
fuente = pygame.font.SysFont("Candycrush/MedievalSharp.ttf", 70)
ingreso = ""
ingreso_rect = pygame.Rect(200, 270, 200, 35)
font_input = pygame.font.SysFont("Arial", 20)

# Fondos de pantalla
imagen_fondo = pygame.image.load("Candycrush/fondomed.jpg")
imagen_fondo = pygame.transform.scale(imagen_fondo, (800, 600))
fondo_pantalla_juego = pygame.image.load("Candycrush/imagenes/Fondo.png")
fondo_pantalla_juego = pygame.transform.scale(fondo_pantalla_juego, (800, 600))

# Botones
boton_jugar = pygame.image.load("Candycrush/imagenes/botonjugara.jpg")
boton_jugar = pygame.transform.scale(boton_jugar, (85, 80))
posicion_imagen_boton_jugar = [340, 500]
rect_boton_jugar = pygame.Rect(*posicion_imagen_boton_jugar, 85, 80)

boton_sonido_on = pygame.image.load("Candycrush/imagenes/sonido_on.png")
boton_sonido_on = pygame.transform.scale(boton_sonido_on, (35, 35))
posicion_boton_on = [750, 70]
rect_boton_on = pygame.Rect(*posicion_boton_on, 35, 35)

boton_sonido_off = pygame.image.load("Candycrush/imagenes/sonido_off.png")
boton_sonido_off = pygame.transform.scale(boton_sonido_off, (35, 35))
posicion_boton_off = [750, 20]
rect_boton_off = pygame.Rect(*posicion_boton_off, 35, 35)

boton_config = pygame.image.load("Candycrush/imagenes/boton_config.png")
boton_config = pygame.transform.scale(boton_config, (35, 35))
posicion_boton_config = [750, 120]

# Nick del personaje
nick = pygame.image.load("Candycrush/imagenes/rect_nombre.png")
nick = pygame.transform.scale(nick, (200, 35))
posicion_nick = [200, 270]

# Textos y sonidos
texto = fuente_medieval.render("Candy Medieval", True, (255, 146, 8))
pygame.mixer.init()
sonido_fondo = pygame.mixer.Sound("Candycrush/sonidos/5.mp3")
volumen = 0.09
sonido_fondo.set_volume(volumen)
sonido_win = pygame.mixer.Sound("Candycrush/sonidos/44.wav")
sonido_win.set_volume(volumen)
sonido_loser = pygame.mixer.Sound("Candycrush/sonidos/45.wav")
sonido_loser.set_volume(volumen)

# Configuración del tablero
ancho_celda = 65
alto_celda = 75
filas = 4
columnas = 7
tablero = generar_lista(filas, columnas)
lista_piezas = {
    1: pygame.transform.scale(pygame.image.load("Candycrush/imagenes/cabeza_mago.jpg"), (ancho_celda, alto_celda)),
    2: pygame.transform.scale(pygame.image.load("Candycrush/imagenes/Candy_Hechizo.jpg"), (ancho_celda, alto_celda)),
    3: pygame.transform.scale(pygame.image.load("Candycrush/imagenes/Candy_poder.jpg"), (ancho_celda, alto_celda)),
}
lista_rects = dibujar_tablero(ventana, tablero, ancho_celda, alto_celda)

# Cuadros de victoria y derrota
victoria_cuadro = pygame.image.load("Candycrush/imagenes/Victoria.png")
victoria_cuadro = pygame.transform.scale(victoria_cuadro, (450, 200))
derrota_cuadro = pygame.image.load("Candycrush/imagenes/imagen_derrota.png")
derrota_cuadro = pygame.transform.scale(derrota_cuadro, (400, 200))

# Variables de estado
en_menu = True
run = True
musica_encendida = True
sonido_win_reproducido = False
sonido_loser_reproducido = False
sonido_fondo.play()

# Bucle principal
while run:
    ventana.fill(constantes.COLOR_BG)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect_boton_jugar.collidepoint(event.pos) and en_menu:
                en_menu = False
            if rect_boton_on.collidepoint(event.pos) and not musica_encendida:
                sonido_fondo.play()
                musica_encendida = True
            if rect_boton_off.collidepoint(event.pos) and musica_encendida:
                sonido_fondo.stop()
                musica_encendida = False

        if event.type == timer_segundos and not fin_tiempo:
            segundos -= 1
            if segundos <= 0:
                fin_tiempo = True
                segundos = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                ingreso = ingreso[:-1]
            else:
                ingreso += event.unicode

    if en_menu:
        dibujar_menu(
            ventana=ventana,
            imagen_fondo=imagen_fondo,
            posicion_imagen=[0, 0],
            texto=texto,
            boton_jugar=boton_jugar,
            posicion_boton_jugar=posicion_imagen_boton_jugar,
            boton_sonido_on=boton_sonido_on,
            posicion_boton_on=posicion_boton_on,
            boton_sonido_off=boton_sonido_off,
            posicion_boton_off=posicion_boton_off,
            boton_config=boton_config,
            posicion_boton_config=posicion_boton_config,
            color_fondo=constantes.COLOR_BG
        )
    else:
        ventana.fill(constantes.COLOR_BG)
        ventana.blit(fondo_pantalla_juego, [0, 0])
        ventana.blit(boton_sonido_on, posicion_boton_on)
        ventana.blit(boton_sonido_off, posicion_boton_off)
        ventana.blit(boton_config, posicion_boton_config)
        segundos_texto = fuente.render(str(segundos), True, constantes.RED2)
        ventana.blit(segundos_texto, [280, 110])
        dibujar_tablero(ventana, tablero, ancho_celda, alto_celda)

    pygame.display.flip()

pygame.quit()


import pygame
import sys
import random
import math
import time

pygame.init()

anchura = 1000
altura = 700

blanco = (255,255,255)
negro = (0,0,0)

posicion_pelota = [anchura/2, altura/2]
tamaño_pelota = 10
velocidad = 10
incremento_de_velocidad = 0
a = 0
tiempo_desde_rebote = 0

tamaño_jugadores = [20,100]
posicion_J1 = [50,0]
posicion_J2 = [anchura-(50+tamaño_jugadores[0]),0]
v = 75

Puntos_J1 = 0
Puntos_J2 = 0

screen = pygame.display.set_mode((anchura, altura))
pygame.display.set_caption("Pong")

clock = pygame.time.Clock()

fuente = pygame.font.SysFont("monospace", 50)

def generar_direccion(a):
	if random.random() < 0.5:
		a = random.randint(-50,-15)
	else:
		a = random.randint(15,50)
	if random.random() < 0.5:
		a += 180
	return a
	
a = generar_direccion(a)

while Puntos_J1 < 10 and Puntos_J2 < 10:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			y1 = posicion_J1[1]
			y2 = posicion_J2[1]
			if event.key == pygame.K_w and posicion_J1[1] >= v:
				y1 -= v
			if event.key == pygame.K_s and posicion_J1[1] <= altura - (tamaño_jugadores[1] + v):
				y1 += v
			posicion_J1 = [posicion_J1[0], y1]
			if event.key == pygame.K_UP and posicion_J2[1] >= v:
				y2 -= v
			if event.key == pygame.K_DOWN and posicion_J2[1] <= altura - (tamaño_jugadores[1] + v):
				y2 += v
			posicion_J1 = [posicion_J1[0], y1]
			posicion_J2 = [posicion_J2[0], y2]

	screen.fill(negro)

	if posicion_pelota[1] < tamaño_pelota or posicion_pelota[1] > altura - tamaño_pelota: #comprobar altura vertical y rebotar si es necesario
		a -= 2 * a
		pygame.mixer.music.load("reboteP.wav")
		pygame.mixer.music.play()

	if posicion_pelota[0] < posicion_J1[0] + tamaño_jugadores[0] + tamaño_pelota and posicion_pelota[0] > posicion_J1[0]- 1:
		if posicion_pelota[1] > posicion_J1[1] - tamaño_pelota and posicion_pelota[1] < posicion_J1[1] + tamaño_jugadores[1] + tamaño_pelota and tiempo_desde_rebote == 0:
			a = a + (2 * (90 - a))
			incremento_de_velocidad += 1
			pygame.mixer.music.load("reboteJ.wav")
			pygame.mixer.music.play()
			tiempo_desde_rebote = 10

	if posicion_pelota[0] > posicion_J2[0] - tamaño_jugadores[0] + tamaño_pelota and posicion_pelota[0] < posicion_J2[0] + 1:
		if posicion_pelota[1] > posicion_J2[1] - tamaño_pelota and posicion_pelota[1] < posicion_J2[1] + tamaño_jugadores[1] + tamaño_pelota and tiempo_desde_rebote == 0:
			a = a + (2 * (90 - a))
			incremento_de_velocidad += 1
			pygame.mixer.music.load("reboteJ.wav")
			pygame.mixer.music.play()
			tiempo_desde_rebote = 10

	if posicion_pelota[0] > 0 - tamaño_pelota and posicion_pelota[0] < anchura + tamaño_pelota:
		posicion_pelota = [posicion_pelota[0] + velocidad * math.cos(math.radians(a)), posicion_pelota[1] + velocidad * math.sin(math.radians(a))]
	else:
		if posicion_pelota[0] > anchura/2:
			Puntos_J1 += 1
		else:
			Puntos_J2 += 1
		pygame.mixer.music.load("punto.wav")
		pygame.mixer.music.play()
		posicion_pelota = [anchura/2, altura/2]
		velocidad = 5
		incremento_de_velocidad = 0
		a = generar_direccion(a)

	pygame.draw.circle(screen, blanco,(posicion_pelota[0], posicion_pelota[1]), tamaño_pelota)

	pygame.draw.rect(screen, blanco, (posicion_J1[0], posicion_J1[1], tamaño_jugadores[0], tamaño_jugadores[1]))
	pygame.draw.rect(screen, blanco, (posicion_J2[0], posicion_J2[1], tamaño_jugadores[0], tamaño_jugadores[1]))

	if tiempo_desde_rebote > 0:
		tiempo_desde_rebote -= 1

	texto = str(Puntos_J1) + ":" + str(Puntos_J2)
	label = fuente.render(texto, 1, blanco)
	screen.blit(label, (anchura/2 - 57, 20))

	velocidad = 5 + incremento_de_velocidad

	clock.tick(60)

	pygame.display.update()

if Puntos_J1 > Puntos_J2:
	texto_final = "Jugador de la izquierda gana!"
	ñaña = 67
else:
	texto_final = "Jugador de la derecha gana!"
	ñaña = 100
texto_final = fuente.render(texto_final, 1, blanco)
screen.blit(texto_final, (ñaña, 150))
pygame.display.update()
time.sleep(3)
sys.exit()
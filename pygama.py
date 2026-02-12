#Napiši snake-game v pygamu
#koda od prej ti lahko sliži za inspiracijo (npr dolzina kace s kvadratki -> to pride prav)

#za projekt naredite github repozitorij, in spremembe sproti comitatje addajte in pushajte
#na koncu morajo biti v repozitoriju vsaj 3 vecji commiti

#okiren plan

#I. Naredi ogrodje -> while zanka, canvas, eventi za exit itd


#II. Naredi kvadrat -> ta kvadrat bo v prihodnisti ratala kača, zaenkrat naj bo samo kvadrat
#	naredi logiko da ta kvadrat lahko zavija levo desno z kliki na gumne na tipkovnici
#	naredi logiko, da se nakej izpiše, ko se ta kvadrat dotakne stene
#	naredi logiko, da se ta kvadrat premika po nekem "gridu" -> hint nastavi clock.tick na nekaj malega,
#		vsak frame premakni kaco za nekaj pixlov, ta premik predstavlja sirino vsake celice


#III. Kvdrat spremeni v seznam kvadratov, ki predstavljajo kaco


#IV. Naredi logiko, da se nekaj izpiše, ce se kace zabije sama vase


#V. Naredi nek nov kvadrat ki predstavlja hrano
#	-> naredi da se vsakic ko ga kaca poje z glavo prestavi na nakljucno mesto in kaca zrasta


#od tu naprej je treba samo še štet score, kej izpiovat na ekrat, dt kk gumb za game over pa restart itd... neke olepšave




#1. dodatna naloga:
#naredi branch "izgled"
#v tem brancu naredi logiko, da ko igra tece, lahko pritisnes gumb "space" kar celotni kaci nastavi nakljucno barvo

#2. dodatna naloga:
#naredi branch "multiplayer"
#v tem branchu naredi logiko, da sta na zacetku igre 2 kaci, ena se upravlja z wasd, druga z gumbi s puscicami
#ce se aca zabije vase, v drugo kaco ali v steno, izgubi

#3. dodatna naloga
#naredi megre obeh branchov

import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake - II")

clock = pygame.time.Clock()
FPS = 10   # manjši FPS = premikanje po gridu

x = WIDTH // 2
y = HEIGHT // 2

direction = (CELL_SIZE, 0)

font = pygame.font.SysFont(None, 40)
hit_wall = False

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = (-CELL_SIZE, 0)
            if event.key == pygame.K_RIGHT:
                direction = (CELL_SIZE, 0)
            if event.key == pygame.K_UP:
                direction = (0, -CELL_SIZE)
            if event.key == pygame.K_DOWN:
                direction = (0, CELL_SIZE)

    x += direction[0]
    y += direction[1]

    if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
        hit_wall = True

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (0, 200, 0), (x, y, CELL_SIZE, CELL_SIZE))

    if hit_wall:
        text = font.render("Zadel si steno!", True, (255, 0, 0))
        screen.blit(text, (200, 280))

    pygame.display.flip()

pygame.quit()
sys.exit()



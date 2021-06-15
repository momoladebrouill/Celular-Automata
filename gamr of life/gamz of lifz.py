import pygame as pg
import noise
from random import randrange,seed,randint
from colorsys import hsv_to_rgb 
# Constantes :
FPS = 60  # les fps tabernak
WIND = 750 # dimentions de la fentere
SIZE = 50 #les dimentions des cellules

print("W pour tout effacer, cliquer pour créer, S pour simuler et R pour shuffle")
pg.init()
f = pg.display.set_mode(size=(WIND, WIND))
pg.display.set_caption("Jeu de la vie de Conway")
fpsClock = pg.time.Clock() #Horloge qui va s'occuper des FPS
#Groupe qui va être parcouru
o = pg.sprite.Group()

def carr(x, y, teh=10, c=(255, 0, 0)):  # Tracer un carré à partir d'un point en haut à gauche
    carr = pg.Surface((teh, teh))  # piqué sur stackoverflow pour avoir un fond avec un alpha
    carr.set_alpha(255)
    carr.fill(c)
    f.blit(carr, (x, y))

class lutin(pg.sprite.Sprite):  # Les cellules
    def __init__(self):
        super().__init__()
        self.alive=False
        self.next_alive=self.alive
        self.x = randrange(WIND)  # X d'origine
        self.y = randrange(WIND)  # Y d'origine
        self.c = hsv_to_rgb(abs(noise.pnoise2(self.x/WIND*0.1,self.y/WIND*0.1,base=randint(0,10))), 1, 255)  # Couleur principale
    def draw(self): # Dessine le carré avec sa position sur la grille
        carr(self.x*SIZE, self.y*SIZE, c=self.c,teh=SIZE)
    def check(self): # Appplique les règles de Conway
        self.total=src((self.x+1,self.y+1))+\
                    src((self.x+1,self.y-1))+\
                    src((self.x+1,self.y))+\
                    src((self.x,self.y-1))+\
                    src((self.x,self.y+1))+\
                    src((self.x-1,self.y))+\
                    src((self.x-1,self.y+1))+\
                    src((self.x-1,self.y-1))
        self.next_alive=self.alive
        if self.alive:
            if self.total<2 or self.total>3:
                self.next_alive=False
            else:
                self.next_alive=True
        else:
            if self.total==3:
                self.next_alive=True
        
def src(tup:tuple): #recherche si la cellule est vivante au duplet
    if tup not in page:
        return int(page[(tup[0]%(WIND/SIZE),tup[1]%(WIND/SIZE))].alive)
    else:
        return int(page[tup].alive)
    
page={}
for y in range(int(WIND/SIZE)):
    for x in range(int(WIND/SIZE)):
        m=lutin()
        m.x=x
        m.y=y
        o.add(m)
        
        page[(x,y)]=m
b = True
try:
    while b:
        pg.display.flip()
        s = pg.Surface((WIND, WIND))  # piqué sur stackoverflow pour avoir un fond avec un alpha
        s.set_alpha(200)
        s.fill((0, 0, 0))
        f.blit(s, (0, 0))
        souris=pg.mouse
        p = pg.key.get_pressed()  # SI la touche est appuyée
        if p[pg.K_a]:
            carr(0, 0, WIND, c=(255, 255, 255))
        for event in pg.event.get():  # QUAND la touche est appuyée
            if event.type == pg.QUIT:
                b = False
                print(" Fin du jeu  babe")
            elif event.type == pg.MOUSEBUTTONUP:
                if event.button==1:
                    x,y=event.pos
                    x,y=int(x/SIZE),int(y/SIZE)
                    m=page[(x,y)]
                    m.next_alive= not m.alive
        for bubu in o:
            if p[pg.K_w]:
                bubu.next_alive=True
            if p[pg.K_r]:
                bubu.next_alive=randrange(2)
            if p[pg.K_s]:
                bubu.check()
        for bubu in o :
            bubu.alive=bubu.next_alive
            if bubu.alive:
                bubu.draw()
        fpsClock.tick(FPS)
except:
    pg.quit()
    raise
pg.quit()

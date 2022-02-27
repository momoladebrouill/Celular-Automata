import pygame as pg
import noise
import random
from colorsys import hsv_to_rgb
# Constantes :
FPS = 60  # les fps tabernak
WIND = 750 # dimentions de la fentere
nbs=100
SIZE = 750/nbs #les dimentions des cellules
quadri=range(int(WIND/SIZE))
fps = pg.time.Clock()

lieux={}
for i in quadri:
    for j in quadri:
        if random.choice((1,0)):
            lieux[(i,j)]=1   

def find(x,y):
    if x<0 or y<0  or x>nbs:
        return 1
    else:
        return lieux.get((x,y),-1)
b = True
try:
    pg.init()
    f = pg.display.set_mode(size=(WIND, WIND))
    pg.display.set_caption("Toom's rule")
    while b:
        pg.display.flip()
        s = pg.Surface((WIND, WIND))
        s.set_alpha(50)
        s.fill((200, 100, 0))
        
        
        si = pg.key.get_pressed()  # SI la touche est appuyée
        if si[pg.K_SPACE]:
            nex={}
            for i in quadri:
                for j in quadri:
                    if i==nbs-1 or j-1<0:
                        nex[(i,j)]= lieux.get((i,j),-1)
                    elif find(i,j-1) + find(i+1,j) + find(i,j) > 0:
                        nex[(i,j)]=1
            lieux={}
            lieux.update(nex)

        for event in pg.event.get():  # QUAND la touche est appuyée
            if event.type == pg.QUIT:
                b = False
            if event.type == pg.KEYDOWN:
                touche= event.dict['key']
                if touche == pg.K_a:
                    
                    nbs=WIND/SIZE
                    SIZE = 750/nbs #les dimentions des cellules
                    quadri=range(int(WIND/SIZE))
                    lieux={}
                    for i in quadri:
                        for j in quadri:
                            if random.choice((1,0)):
                                lieux[(i,j)]=1  
                    
            
            elif event.type == pg.MOUSEBUTTONUP:
                
                s.set_alpha(360)
                if event.button==4:
                    SIZE+=1
                if event.button==5:
                    SIZE-=1
        f.blit(s, (0, 0))
        for i in quadri:
            for j in quadri:
                if lieux.get((i,j),0):
                    pg.draw.rect(f,(255,255,0),((i*SIZE,j*SIZE),(SIZE,SIZE)))
        fps.tick(FPS)
except:
    pg.quit()
    raise
pg.quit()

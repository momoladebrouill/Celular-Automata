import pygame as pg
import random
from colorsys import hsv_to_rgb
# Constantes :
FPS = 60  # les fps tabernak
WIND = 750 # dimentions de la fentere
nbs=100
SIZE = 750/nbs #les dimentions des cellules
quadri=range(int(WIND/SIZE))
fps = pg.time.Clock()

def find(x,y):
    if x>0 and x<nbs and y>0 and y<nbs:
        return not bool(lieux.get((x,y),0))

def pick():
    if random.random()>0.9:
        return hsv_to_rgb(random.random(),1,255)
    else:
        return (255,255,255)

def neigbourg(i,j):
    ls=((i-1,j-1),(i,j-1),(i+1,j-1),
        (i-1,j),        (i+1,j),
        (i-1,j+1),(i,j+1),(i+1,j+1))
    for pos in ls:
        if pos[0]>0 and pos[0]<nbs and pos[1]<nbs and pos[1]>0:
            yield pos

lieux={}
b = True
mode=''

try:
    pg.init()
    f = pg.display.set_mode(size=(WIND, WIND))
    pg.display.set_caption("Toom's rule")
    while b:
        pg.display.flip()
        s = pg.Surface((WIND, WIND))
        f.set_alpha(360)
        f.fill((0, 0, 0))
        si = pg.key.get_pressed()  # SI la touche est appuyée
        if not si[pg.K_SPACE]:
            nex={}
            for partic in lieux:
                
                if find(partic[0],partic[1]+1): nex[(partic[0],partic[1]+1)]=1
                elif find(partic[0]-1,partic[1]+1):   nex[(partic[0]-1,partic[1]+1)]=1
                elif find(partic[0]+1,partic[1]+1): nex[(partic[0]+1,partic[1]+1)]=1
##                elif find(partic[0]-1,partic[1]): nex[(partic[0]-1,partic[1])]=1
##                elif find(partic[0]+1,partic[1]): nex[(partic[0]+1,partic[1])]=1
                else: nex[(partic[0],partic[1])]=1
            lieux={}
            lieux.update(nex)
        for event in pg.event.get():  # QUAND la touche est appuyée
            if event.type == pg.QUIT:
                b = False
                print(" Il y avait {0} cellules".format(len(lieux)))
            if event.type == pg.KEYDOWN:
                touche= event.dict['key']
                if touche == pg.K_a:
                    nbs=WIND/SIZE
                    SIZE = 750/nbs #les dimentions des cellules
                    quadri=range(int(WIND/SIZE))
                    lieux={}
            elif event.type ==pg.MOUSEBUTTONDOWN:
                if event.button==1:
                    mode='c'
                if event.button==3:
                    mode='e'
            elif event.type == pg.MOUSEBUTTONUP:
                mode=''
                s.set_alpha(360)
                if event.button==4:
                    SIZE+=1
                elif event.button==5:
                    SIZE-=1
                nbs=WIND/SIZE
                SIZE = 750/nbs #les dimentions des cellules
                quadri=range(int(WIND/SIZE))
        x,y=pg.mouse.get_pos()
        x=int(x/SIZE)
        y=int(y/SIZE)
        if mode=='c':
            lieux[(x,y)]=1
            if SIZE<5:
                for lieu in neigbourg(x,y):
                    lieux[lieu]=1
        elif mode=='e':
            lieux[(x,y)]=0
        for i,j in lieux:
            pg.draw.rect(f,0xffffff,((i*SIZE,j*SIZE),(SIZE,SIZE)))
        fps.tick(FPS)
except:
    pg.quit()
    raise
pg.quit()

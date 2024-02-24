import pygame as pg
import random
from colorsys import hsv_to_rgb
# Constantes :
FPS = 60  # les fps tabernak
WIND = 750 # dimentions de la fentere
nbs=50
SIZE = 750/nbs #les dimentions des cellules
quadri=range(int(WIND/SIZE))
fps = pg.time.Clock()



def find(xpos,ypos):
    if ypos>nbs:
        return 1
    else:
        return (xpos,ypos) in lieux

def tous():
    for azr in range(int(nbs)):
        for zpeifj in range(int(nbs)):
            yield int(nbs)-azr,int(nbs)-zpeifj

lieux={}
b = 1
mode=''
try:
    pg.init()
    f = pg.display.set_mode(size=(WIND, WIND))
    pg.display.set_caption("Toom's rule")
    while b:
        b+=1
        pg.display.flip()
        f.fill(0)
        si = pg.key.get_pressed()  # SI la touche est appuyée
        if not si[pg.K_SPACE]:
            nex={}
            for partic in tous():
                if find(partic[0],partic[1]):
                    if find(partic[0],partic[1]+1)==0:
                        nex[(partic[0],partic[1]+1)]=1
                    elif find(partic[0]-1,partic[1]+1)==0:
                        nex[(partic[0]-1,partic[1]+1)]=1
                    elif find(partic[0]+1,partic[1]+1)==0:
                        nex[(partic[0]+1,partic[1]+1)]=1
    ##                elif find(partic[0]+1,partic[1])==0:
    ##                    nex[(partic[0]+1,partic[1])]=1
    ##                elif find(partic[0]-1,partic[1])==0:
    ##                    nex[(partic[0]-1,partic[1])]=1
                    else:
                        nex[(partic[0],partic[1])]=1
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
                if event.button==4:
                    SIZE+=1
                elif event.button==5:
                    SIZE-=1
                    if SIZE<=0:SIZE=1
                nbs=WIND/SIZE
                SIZE = 750/nbs #les dimentions des cellules
                quadri=range(int(WIND/SIZE))
        mx,my=pg.mouse.get_pos()
        mx=int(mx/SIZE)
        my=int(my/SIZE)
        if b>1:
            b=1
            if mode=='c':
                lieux[(mx,my)]=1
        elif mode=='e':
            lieux[(mx,my)]=0
        for i,j in lieux:
            pg.draw.rect(f,0xffffff,((i*SIZE,j*SIZE),(SIZE,SIZE)))
        fps.tick(FPS)
except:
    pg.quit()
    raise
pg.quit()

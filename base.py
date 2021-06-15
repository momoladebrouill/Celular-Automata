import pygame as pg
import noise
import random
from colorsys import hsv_to_rgb
# Constantes :
FPS = 60  # les fps tabernak
WIND = 750 # dimentions de la fentere
nbs=50
SIZE = 750/nbs #les dimentions des cellules
quadri=range(int(WIND/SIZE))
fps = pg.time.Clock()



def find(x,y):
    return bool(lieux.get((x,y),0))

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
        if  not si[pg.K_SPACE]:
            nex={}
            for a,b in lieux:
                for i,j in neigbourg(a,b):
                    som=sum((find(i-1,j-1),find(i,j-1),find(i+1,j-1),
                                find(i-1,j),                find(i+1,j),
                                find(i-1,j+1),find(i,j+1),find(i+1,j+1)))
                    if find(i,j):
                        if not (som<2 or som>3):
                            nex[(i,j)]=lieux[(i,j)]
                    else:
                        if som==3:
                            nex[(i,j)]=pick()
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
            lieux[(x,y)]=pick()
        elif mode=='e':
            lieux[(x,y)]=0
        #f.blit(s, (0, 0))
        for i in quadri:
            for j in quadri:
                if lieux.get((i,j),0):
                    c=lieux[(i,j)]
                    pg.draw.rect(f,c,((i*SIZE,j*SIZE),(SIZE,SIZE)))
        fps.tick(FPS)
except:
    pg.quit()
    raise
pg.quit()

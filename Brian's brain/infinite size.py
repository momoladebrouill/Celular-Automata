import pygame as pg
import noise
import random
import math
from colorsys import hsv_to_rgb
"""à alléger et clarifier"""
# Constantes :
FPS = 60  # les fps tabernak
WIND = 750 # dimentions de la fentere
nbs=10 #le nombre de celules sur la grid
SIZE = WIND/nbs #la taille des cellules
quadri=range(nbs)
fps = pg.time.Clock()

class dep:
    x=0
    y=0
    sped=-10
    __repr__=lambda self:str((self.x,self.y))

def find(x,y):return lieux.get((x,y),0)==1

def neigbourg(i,j):
    ls=((i-1,j-1),(i,j-1),(i+1,j-1),
        (i-1,j),        (i+1,j),
        (i-1,j+1),(i,j+1),(i+1,j+1))
    for pos in ls:
        yield pos[0],pos[1]
        
def grid(n):
    for abscisse in range(n):
        for ordonne in range(n):
            yield abscisse,ordonne
lieux={}
B = 1
mode=''
ct=0

try:
    pg.init()
    f = pg.display.set_mode(size=(WIND, WIND))
    pg.display.set_caption("Brian's Brain")
    font=pg.font.SysFont('consolas',25,1)
    while B:
        pg.display.flip()
        f.set_alpha(10)
        f.fill(0)
        B+=1
        si = pg.key.get_pressed()  # SI la touche est appuyée
        if si[pg.K_q]:dep.x-=dep.sped
        if si[pg.K_s]:dep.y+=dep.sped
        if si[pg.K_d]:dep.x+=dep.sped
        if si[pg.K_z]:dep.y-=dep.sped

        if not si[pg.K_SPACE] and not B%5:
            nex={}
            for a,b in lieux:
                if lieux[(a,b)]==1:
                    nex[(a,b)]=2
                for i,j in neigbourg(a,b):
                    if not find(i,j):
                        som=sum(find(X,Y) for X,Y in neigbourg(i,j))
                        if som==2 and lieux.get((i,j))!=2:
                            nex[(i,j)]=1
            lieux={}
            lieux.update(nex)
        
        for event in pg.event.get():  # QUAND la touche est appuyée
            if event.type == pg.QUIT:
                B = False
                pg.quit()
                print(" Il y avait {0} cellules".format(len(lieux)))
            if event.type == pg.KEYDOWN:
                touche=event.dict['key']
                if touche == pg.K_a:
                    nbs=int(WIND/SIZE)
                    for i in range(nbs):
                        for j in range(nbs):
                            lieux[(i,j)]=1
                elif touche == pg.K_e:
                    lieux={}
                    
            elif event.type ==pg.MOUSEBUTTONDOWN:
                if event.button==1:
                    mode='c'
                elif event.button==3:
                    mode='e'
            elif event.type == pg.MOUSEBUTTONUP:
                mode=''
                if event.button==4:
                    SIZE+=5
                    dep.x-=x*5
                    dep.y-=y*5
                elif event.button==5:
                    SIZE-=5
                    if SIZE<=0:
                        SIZE=1
                    else:
                        dep.x+=x*5
                        dep.y+=y*5
                
                
        x,y=pg.mouse.get_pos()
        x=round((x-dep.x)/SIZE)-0.5
        y=round((y-dep.y)/SIZE)-0.5
        
        if mode=='c':
            lieux[(x,y)]=1
        elif mode=='e':
            if (x,y) in lieux:
                lieux.pop((x,y))

        nex=dict()
        for i,j in lieux:
            if i>-dep.x/SIZE-1 and j>-dep.y/SIZE-1 and i<-dep.x/SIZE+nbs and j<-dep.y/SIZE+nbs: # si on a besoin de le dessiner
                # et bien alors on le dessine
                nex[(i,j)]=lieux[(i,j)]
                try:
                    coul=[(255,255,255),(200,200,0)][nex[(i,j)]-1]
                except IndexError:
                    coul=(255,0,0)
                pg.draw.rect(f,coul,((dep.x+i*SIZE,dep.y+j*SIZE),(SIZE,SIZE)))
                
        
        lieux.clear()
        lieux.update(nex)

        pg.draw.rect(f,0xff0000,((dep.x,dep.y),(SIZE,SIZE)))     
        pg.draw.rect(f,0xffffff,((x*SIZE+dep.x,y*SIZE+dep.y),(SIZE,SIZE)),width=3)        
        fps.tick(FPS)
except:
    pg.quit()
    raise
pg.quit()

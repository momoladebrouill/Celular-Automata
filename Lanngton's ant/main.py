import pygame as pg
import noise
import random
import math
from colorsys import hsv_to_rgb
# Constantes :
FPS = 60  # les fps tabernak
WIND = 750 # dimentions de la fentere
nbs=10
SIZE = 750/nbs #les dimentions des cellules
quadri=range(int(WIND/SIZE))
fps = pg.time.Clock()

class dep:
    x=0
    y=0
    sped=-10

def find(x,y):
    return bool(lieux.get((x,y),0))

def neigbourg(i,j):
    ls=((i-1,j-1),(i,j-1),(i+1,j-1),
        (i-1,j),        (i+1,j),
        (i-1,j+1),(i,j+1),(i+1,j+1))
    for pos in ls:
        yield pos
class frm:
    x=nbs/2
    y=nbs/2
    angle=0
    def draw():
        self=frm
        centre=(dep.x+self.x*SIZE+SIZE/2,
                dep.y+self.y*SIZE+SIZE/2)
        pg.draw.circle(f,0xffffff,centre,SIZE/2)
        pg.draw.line(f,0xffff00,centre,(centre[0]+SIZE/2*math.cos(self.angle),centre[1]+SIZE/2*math.sin(self.angle)),int(SIZE/2))
    def fd():
        global lieux
        self=frm
        if find(self.x,self.y)==1:
            self.angle+=math.pi/2
            lieux.pop((self.x,self.y))
        else:
            self.angle-=math.pi/2
            lieux[(self.x,self.y)]=1
        self.angle=self.angle%math.tau
        self.x+=int(math.cos(self.angle))
        self.y+=int(math.sin(self.angle))
lieux={}
b = True
mode=''

ct=0
try:
    pg.init()
    f = pg.display.set_mode(size=(WIND, WIND))
    pg.display.set_caption("La fourmi de langton")
    font=pg.font.SysFont('consolas',25,1)
    while b:
        pg.display.flip()
        s = pg.Surface((WIND, WIND))
        s.set_alpha(360)
        s.fill((0, 0, 0))
        si = pg.key.get_pressed()  # SI la touche est appuyée
        if not si[pg.K_SPACE]:
            frm.fd()
            ct+=1
        if si[pg.K_q]:dep.x-=dep.sped
        if si[pg.K_s]:dep.y+=dep.sped
        if si[pg.K_d]:dep.x+=dep.sped
        if si[pg.K_z]:dep.y-=dep.sped
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
                    dep.x+=1
                    dep.y+=1
                elif event.button==5:
                    SIZE-=1
                    dep.x-=1
                    dep.y-=WIND/SIZE/2
                nbs=WIND/SIZE
                SIZE = 750/nbs #les dimentions des cellules
                quadri=range(int(WIND/SIZE))
        x,y=pg.mouse.get_pos()
        x=int(x/SIZE+dep.x*SIZE)
        y=int(y/SIZE+dep.y*SIZE)
        if mode=='c':
            lieux[(x,y)]=1
        elif mode=='e':
            if lieux.get((x,y)):
                lieux.pop((x,y))
        f.blit(s, (0, 0))
        for i,j in lieux: 
            pg.draw.rect(f,0xff0025,((dep.x+i*SIZE,dep.y+j*SIZE),(SIZE,SIZE)))
        t=font.render(str(ct),False,(255,255,255))
        f.blit(t,(0,0))
        frm.draw()
        fps.tick(FPS)
except:
    pg.quit()
    raise
pg.quit()

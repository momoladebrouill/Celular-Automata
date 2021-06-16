#!/usr/bin/env python
import pygame as pg


from colorsys import hsv_to_rgb
# Constantes :
FPS = 60  # les fps tabernak
WIND = 750 # dimentions de la fentere
nbs=75
SIZE = 750/(nbs-1) #les dimentions des cellules
quadri=range(int(WIND/SIZE))
fps = pg.time.Clock()



def find(x,y):
    if lieux.get((x,y),0)==1:
        return 1
    else:
        return 0

def neigbourg(i,j):
    ls=((i-1,j-1),(i,j-1),(i+1,j-1),
        (i-1,j),        (i+1,j),
        (i-1,j+1),(i,j+1),(i+1,j+1))
    for pos in ls:
        if pos[0]>0 and pos[0]<nbs and pos[1]>0 and pos[1]<nbs:
            yield pos
        else:
            print('moriarty')
            yield 'hey'
        
lieux={}
b = 1
mode=''
mouse=(0,0)
try:
    pg.init()
    font=pg.font.SysFont("consolas",25)
    f = pg.display.set_mode((WIND, WIND),pg.RESIZABLE)
    pg.display.set_caption("Brian's brain")
    while b:
        b+=1
        pg.display.update()
        f.fill(0)
        si = pg.key.get_pressed()  # SI la touche est appuyée
        if  not si[pg.K_SPACE] and not b%5:
            nex={}
            for a,b in lieux:
                if lieux[(a,b)]==1:
                    nex[(a,b)]=2
            for i in quadri:
                for j in quadri:
                    if not find(i,j):
                        som=sum((find(i-1,j-1),find(i,j-1),find(i+1,j-1),
                                find(i-1,j),                find(i+1,j),
                                find(i-1,j+1),find(i,j+1),find(i+1,j+1)))
                        if som==2 and lieux.get((i,j))!=2:
                            nex[(i,j)]=1
                
                
            lieux={}
            lieux.update(nex)
        for event in pg.event.get():  # QUAND la touche est appuyée
            if event.type == pg.QUIT:
                b = False
                print(" Il y avait {0} cellules".format(len(lieux)))
            if event.type == pg.KEYDOWN:
                if event.dict['key'] == pg.K_a:
                    lieux={}
            elif event.type ==pg.MOUSEBUTTONDOWN:
                mouse=event.pos
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
                nbs=WIND/SIZE
                SIZE = 750/nbs #les dimentions des cellules
                quadri=range(int(WIND/SIZE))
        if mode:
            x,y=pg.mouse.get_pos()
            x=int(x/SIZE)
            y=int(y/SIZE)
            if mode=='c':
                lieux[(x,y)]=1
            elif mode=='e':
                if (x,y) in lieux:
                    lieux.pop((x,y))

        
        
        for i,j in lieux:
                c=lieux[(i,j)]
                if c==1:
                    c=(255,255,255)
                elif c==2:
                    c=(200,200,0)
                else:
                    c=(255,0,0)
                pg.draw.rect(f,c,((i*SIZE+1,j*SIZE+1),(SIZE-1,SIZE-1)))
        f.blit(font.render(str(int(fps.get_fps())),False,(0,255,0),(0,0,0)),(0,WIND/2))
        f.blit(font.render(str(int(len(lieux))),False,(0,255,0),(0,0,0)),(0,WIND/2+20))

        fps.tick(FPS)
except:
    pg.quit()
    raise
pg.quit()

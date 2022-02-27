import pygame as pg
from utis import*
from colorsys import hsv_to_rgb
pg.init()
f=pg.display.set_mode((500,500),pg.RESIZABLE)
fps=pg.time.Clock()
B=1
X,Y=250,250
mid=Pos(X,Y)
zoom=50
web=[(Pos(0,0),Vec(long=20,angle=i/4*math.tau),0.1) for i in range(4)]
lieux=[]
for fil in web:
    fil[1].x,fil[1].y=round(fil[1].x),round(fil[1].y)
    lieux.append(fil[0]+fil[1])
    
while B:
    pg.display.update()
    f.fill(0)
    for fil in web:
        if fil[1].long>0:
            fil[1].draw(pg,f,mid+fil[0],hsv_to_rgb(fil[2]%1,1,255))
    for pos in lieux:
         pg.draw.circle(f,0x0000ff,(mid+pos).pourpg(),5)
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            B=0
        elif event.type==pg.VIDEORESIZE:
            X=event.w//2
            Y=event.h//2
            mid=Pos(X,Y)
        elif event.type==pg.MOUSEBUTTONUP:
            if event.button==4:
                zoom-=1
            elif event.button==5:
                zoom+=1
        elif event.type==pg.KEYUP:
            if event.key==pg.K_SPACE:
                nv=[]
                lieux=[]
                for fil in web:
                    fil[1].x,fil[1].y=round(fil[1].x),round(fil[1].y)
                    lieux.append(fil[0]+fil[1])
                   
                for fil in web:
                    nv.append(fil)
                    a=Vec(long=fil[1].long,angle=fil[1].angle-math.pi/4)
                    a.x,a.y=round(a.x),round(a.y)
                    if not fil[0]+(fil[1]+a) in lieux:
                        nv.append((fil[0]+fil[1],a,fil[2]+0.1))
                        lieux.append(fil[0]+fil[1]+a)
                        
                    b=Vec(long=fil[1].long,angle=fil[1].angle+math.pi/4)
                    b.x,b.y=round(b.x),round(b.y)
                    if not fil[0]+(fil[1]+b) in lieux:
                        nv.append((fil[0]+fil[1],b,fil[2]+0.1))
                        lieux.append(fil[0]+fil[1]+b)
                web=nv[:]

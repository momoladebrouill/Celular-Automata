import pygame as pg
import utis

import random
import math
from colorsys import hsv_to_rgb

grav=utis.Vec(x=0,y=0.1)
class Confetti:
    def __init__(self,x=375,y=375):
        self.pos=utis.Pos(x,y)
        self.vec=utis.Vec(long=10,angle=3*math.pi/2+(random.random()-0.5)/2)
        self.size=10
        self.coul=random.random()
    def draw(self):
        self.pos+=self.vec
        self.vec+=grav
        self.size-=0.01
        pg.draw.circle(f,0x0000ff,self.pos.pourpg(),5)
if __name__=='__main__':
    pg.init()
    f= pg.display.set_mode(size=(750,750))
    fps=pg.time.Clock()
    boom=[Confetti() for i in range(10)]
    creer=0
    s=pg.Surface((750,750))
    s.set_alpha(10)
    while True:
        fps.tick(120)
        pg.display.flip()
        f.blit(s,(0,0))


        for event in pg.event.get():
            if event.type==pg.QUIT:
                pg.quit()
            if event.type==pg.MOUSEBUTTONDOWN:
                creer=1
            elif event.type==pg.MOUSEBUTTONUP:
                creer=0
        if creer:
            posu=pg.mouse.get_pos()
            boom.append(Confetti(posu[0],posu[1]+20))

        proch=[]
        for conf in boom:
            conf.draw()
            if conf.pos.x<750:
                proch.append(conf)
        conf=proch[:]

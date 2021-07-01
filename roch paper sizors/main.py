import pygame as pg
import random
from colorsys import hsv_to_rgb

tour=[
  [0,1],[0,-1],
  [1,0],[1,1],[1,-1],
  [-1,0],[-1,1],[-1,-1]]
size=5
class Cell:
  def __init__(self,mode,pos,val):
    self.mode=mode
    self.pos=pos
    self.val=val
  def is_weaker(self,other):
    if self.mode=='rock':
      return other.mode=='sci'
    elif self.mode=='sci':
      return other.mode=='paper'
    elif self.mode=='paper':
      return other.mode=='rock'
    
  def attack(self):
    todo=random.choice(tour)
    attack=self.pos[0]+todo[0],self.pos[1]+todo[1]
    if attack[0]>=0 and attack[1]>=0 and attack[0]<wind[0] and attack[1]<wind[1]:
      if type(pam[attack])==int:
        if self.val<=9:
          pam[attack]=Cell(self.mode,attack,self.val+1)
          draw(pam[attack],attack)
          
      elif pam[attack].is_weaker(self):
        pam[attack].val-=1
        draw(pam[attack],attack)
        if pam[attack].val<=0 and self.val<=9:
          pam[attack]=Cell(self.mode,attack,self.val+1)
          draw(pam[attack],attack)
          
def col(val,pos):
  if type(val)==int:
    TypeError
  c=int(val.val/10*255)
  if c<0:
   
    return 0
  else:
    cg=c
    
  if val.mode=='rock':
    return (0,0,cg)
  elif val.mode=='sci':
    return (0,cg,0)
  elif val.mode=='paper':
    return (cg,0,0)
pam={}
wind=(500//size,500//size)
for y in range(wind[0]):
      for x in range(wind[1]):
        pam[x,y]=0
          


pg.init()
f=pg.display.set_mode((500,500),pg.RESIZABLE)
fps=pg.time.Clock()

B=1
mode='rock'
create=False
remap=False
conf=[]
maxx,maxy=50,50
def draw(truc,pos):
  pg.draw.rect(f,col(truc,pos),((pos[0]*size,pos[1]*size),(size,size)))
while B:
  pg.display.update()
  if create:
    mouse=pg.mouse.get_pos()
    pam[(mouse[0]//size),(mouse[1]//size)]=Cell(mode,((mouse[0]//size),(mouse[1]//size)),0)

    
  for pos in pam:
    truc=pam[pos]
    if type(truc)!=int:
      truc.attack()
      

  for event in pg.event.get():
    if event.type==pg.QUIT:
      pg.quit()
      B=0
    elif event.type==pg.MOUSEBUTTONDOWN:
      if event.button==3:
        mode='sci'
      elif event.button==2:
        mode='paper'
      elif event.button==1:
        mode='rock'
      if not event.button==5 and not event.button==4:
        create=True
    elif event.type==pg.MOUSEBUTTONUP:
      if event.button==5:
        size+=1
        remap=True
        
      elif event.button==4:
        size-=1
        if not size:size=1
        remap=True
        
      else:
        create=False
    elif event.type==pg.KEYUP:
      if event.key==pg.K_c:
        breakpoint()
      elif event.key==pg.K_e:
        f.fill(0)
        for y in range(wind[1]):
          for x in range(wind[0]):
            pam[x,y]=0
        
    if event.type==pg.VIDEORESIZE:
      wind=event.w//size,event.h//size
      remap=True
  if remap:
    f.fill(0)
    nmaxx,nmaxy=0,0
    for y in range(wind[1]):
      for x in range(wind[0]):
        if x>maxx or maxy<y:
          pam[(x,y)]=0
          if maxx>nmaxx:
            nmaxx=maxx
          if maxy>nmaxy:
            nmaxy=maxy
    maxx,maxy=nmaxx,nmaxy
    remap=False

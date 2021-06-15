import pygame as pg
dic={}
size=10
# dic rempli de zeros
smode=''
border=750/size
def find(x,y):
    global dic
    
    if x>=border or y>=border:
        return 1

    
    try:
        return dic[(x,y)]
    except:
        pg.draw.rect(f,0xff0000,((x*size,y*size),(size,size)))
        dic[(x,y)]=0
        return 0
try:
    pg.init()
    f=pg.display.set_mode((750,750))
    fps=pg.time.Clock()
    s=pg.Surface((750,750))
    s.set_alpha(360)
    B=1
    while B:
        B+=1
        fps.tick(60)
        pg.display.flip()
        f.blit(s,(0,0))
        if not B%1:
            dummy={}
            dummy.update(dic)
            for x,y in dummy:
                if find(x+1,y+1)==0 and find(x,y):
                    dic[(x,y)]=0
                    dic[(x+1,y+1)]=1
                elif find(x,y+1)==0 and find(x,y):
                    dic[(x,y)]=0
                    dic[(x,y+1)]=1
                elif find(x-1,y+1)==0 and find(x,y):
                    dic[(x,y)]=0
                    dic[(x-1,y+1)]=1
                
        for a,b in dic:
            if dic[(a,b)]==1:
                pg.draw.rect(f,0xffffff,((a*size,b*size),(size,size)))
        
        for event in pg.event.get():
            if event.type==pg.QUIT:
                B=0
            if event.type==pg.KEYUP:
                dic.clear()
            if event.type==pg.MOUSEBUTTONDOWN:
                smode='draw'
            elif event.type==pg.MOUSEBUTTONUP:
                smode=''
        if smode=='draw':
            sox,soy=pg.mouse.get_pos()
            dic[(int(sox/size),int(soy/size))]=1
except:
    pg.quit()
    raise
pg.quit()

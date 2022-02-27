import pygame 
class w:
	l=500
	h=500
	tup=lambda :(w.h,w.l)
pygame.init()
f=pygame.display.set_mode((500,500),pygame.RESIZABLE)
font=pygame.font.SysFont("consolas",25)
fps=pygame.time.Clock()
q=1
pos={}
clicking=False
while q:
	pygame.display.flip()
	fps.tick(60)
	f.fill(0)
	if clicking:
		pis=(int(pygame.mouse.get_pos()[0]/10),int(pygame.mouse.get_pos()[1]/10))
		if not pos.get(pis,0):
			pos[pis]=True
	nepos={}
	for x,y in pos:
		if pos[x,y]==True:
			pygame.draw.rect(f,0xffffff,(x*10,y*10,10,10))
			if pos.get((x,y+1),0)==True: # Si on peut s'étaler
				if pos.get((x-1,y),0)==False and x-1>0:
					pos[x,y]=False
					nepos[x,y]=False
					nepos[x-1,y]=True
				elif pos.get((x+1,y),0)==False and x+1<w.l:
					pos[x,y]=False
					nepos[x,y]=False
					nepos[x+1,y]=True
				else:
					nepos[x,y]=True
					pos[x,y]=True
			if pos.get((x,y+1),0)==False and y<w.h: #Si on peut descendre
				nepos[(x,y+1)]=True
				nepos[(x,y)]=False
				pos[x,y]=False
			elif pos.get((x-1,y+1),0)==False and y+1<w.h:
				nepos[(x-1,y+1)]=True
				nepos[(x,y)]=False
				pos[x,y]=False
			elif pos.get((x+1,y+1),0)==False and y+1<w.h:
				nepos[(x+1,y+1)]=True
				nepos[(x,y)]=False
				pos[x,y]=False
			else:
				nepos[(x,y)]=True

	pos={}
	pos.update(nepos)
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
			q=0
		if event.type==pygame.VIDEORESIZE:
			w.h=event.h
			w.l=event.w

		if event.type==pygame.MOUSEBUTTONDOWN:
			clicking=True
		elif event.type==pygame.MOUSEBUTTONUP:
			clicking=False
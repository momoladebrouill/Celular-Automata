import tkinter as tk
import random

class Tabl():
    def __init__(self):
        self.val=0
        self.w=10
        self.h=10
    def __setitem__(self,pos,val):
        if val:
            self.val+=2**(pos[1]*self.w+pos[0])
        else:
            if self[pos]:
                self.val-=2**(pos[1]*self.w+pos[0])

    def __getitem__(self,pos):
        return self.val&2**(pos[1]*self.w+pos[0])
    def __iter__(self):
        self.x,self.y=0,1
        self.part=1
        self.bi=False
        return self
    def __next__(self):
        goodtogo=lambda self:(self.part//2)&self.val
        while goodtogo(self) and self.bi:
            self.x+=1
            self.part*=2
            if self.x >self.w:
                self.x=1
                self.y+=1
            if self.y>self.h:
                raise StopIteration
            if goodtogo(self):
                self.bi= not self.bi
                return self.x-1,self.y-1
    def __repr__(self):
        traceur=1
        s=""
        for y in range(self.h):
            for x in range(self.w):
                s+="1" if self.val&traceur else "0"
                traceur*=2
            s+="\n"
        return s
t=Tabl()
rules={"alive":5}
class Fen(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.can=tk.Canvas(self,width=500,height=500)
        self.title("Cellular Automata")
        self.can.pack(expand=tk.YES)
        self.can["bg"]="black"
        self.isrunning=tk.BooleanVar(self,False)
        self.cases={}
        tk.Checkbutton(self,text="run the simulation",
                       variable=self.isrunning).pack()
    def eachframe(self):
        if self.isrunning.get():
            """
            for pos in self.cases:
                # Récuperer la valeur de l'objet
                Id=self.cases[pos]
                tag=self.can.itemcget(Id,"tags")
                # Paramétrer la valeur de l'objet
                #self.can.itemconfigure(Id,{'fill':random.choice(('red','blue','yellow'))})
                # Supprimer l'objet
                #self.can.delete(tag)
                pos=tuple(tag)
            """
            for x,y,val in t:
                ...
                
                
            
                
                
    
        self.after(20,self.eachframe)
    def truc(self,event):
        pos=event.x//10*10,event.y//10*10
        t[pos]=1
        self.cases[pos]=self.can.create_rectangle(pos[0],pos[1],pos[0]+10,pos[1]+10,
                                  fill="white",tag=f"{pos}")
        
        

f"""=Fen()
f.can.bind("<Button>",f.truc)
f.eachframe()
tk.mainloop()"""

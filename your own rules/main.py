import tkinter as tk
import random

tour=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

class Tabl():
    def __init__(self,width=50,height=50):
        self.val=0
        self.w=50
        self.h=50
        self.max=2**(self.w*self.h)

    def switch(self,pos):
        self.val^=1<<(pos[1]*self.w+pos[0])

    def __setitem__(self,pos,val):
        if val:
            self.val|=1<<(pos[1]*self.w+pos[0])
        elif self[pos]:
            self.val-=1<<(pos[1]*self.w+pos[0])

    def __getitem__(self,pos):
        if 0<=pos[0]<=self.w and 0<=pos[1]<=self.h:
            return bool(self.val & 1<<(pos[1]*self.w+pos[0]))
        return 0

    def __iter__(self):
        self.x,self.y=0,1
        self.part=1
        return self

    def __next__(self):
        self.x+=1
        self.part*=2
        if self.x >self.w:
            self.x=1
            self.y+=1
        if self.y>self.h:
            raise StopIteration
        return self.x-1,self.y-1,self[self.x-1,self.y-1]

    def __repr__(self):
        traceur=1
        s=""
        for y in range(self.h):
            for x in range(self.w):
                s+="1" if self.val&traceur else "0"
                traceur<<=1
            s+="\n"
        return s


class Fen(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Cellular Automata")
        self.t=Tabl()
        self.cases={}
        self.gen=0
        self.can=tk.Canvas(self,width=500,height=500)
        self.can["bg"]="black"
        self.can.grid(row=0,column=0)

        param=tk.Frame(self)
        param.grid(row=0,column=1)

        self.isrunning=tk.BooleanVar(self,False)

        tk.Checkbutton(param,text="run the simulation",
                       variable=self.isrunning).pack()

        tk.Button(param,text="clear",command=self.empty).pack()
        self.s=[(tk.Scale(param,
                         from_=1,
                         to=8,
                         orient=tk.HORIZONTAL,
                         command=self.newrules),tex) for tex in ["Min born","Max born","Min death","Max death"]]
        for s,tex in self.s:
            tk.Label(param,text=tex).pack()
            s.pack()
        self.rpz=tk.StringVar(self,value="Not running")
        tk.Label(param,textvariable=self.rpz).pack()
        self.s=[i[0] for i in self.s]
        self.newrules()

    def empty(self):
        self.t=Tabl()
        for pos in self.cases:
            Id=self.cases[pos]
            self.can.delete(Id)
        self.cases={}
        self.gen=0

    def newrules(self,x=None):
        self.rules={
                "born":[self.s[0].get(),self.s[1].get()],
                "die":[self.s[2].get(),self.s[3].get()]
                }

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
            todell,toadd=set(),set()
            for x,y,val in self.t:
                somme=sum(self.t[x+mx,y+my] for mx,my in tour)
                if val:
                    if self.rules["die"][0]<=somme<=self.rules["die"][1]:
                        todell.add((x,y))
                else:
                    if self.rules["born"][0]<=somme<=self.rules["born"][1]:
                        toadd.add((x,y))
            for elem in todell:
                self.deleteat(elem)
            for elem in toadd:
                self.addat(elem)
            self.rpz.set("Generation n°"+ str(self.gen))
            self.gen+=1
        self.after(20,self.eachframe)

    def deleteat(self,pos):
        self.t[pos]=0
        for p in self.cases:
            if p==pos:
                Id=self.cases[pos]
                self.can.delete(Id)
                del self.cases[pos]
                break

    def addat(self,pos):
        if not self.t[pos]:
            self.t.switch(pos)
            self.cases[pos]=self.can.create_rectangle(pos[0]*10,pos[1]*10,pos[0]*10+10,pos[1]*10+10,
                                      fill="white",tag=f"{pos}")

    def useradd(self,event):
        pos=event.x//10,event.y//10
        self.addat(pos)
        
    def userdel(self,event):
        pos=event.x//10,event.y//10
        self.deleteat(pos)


f=Fen()
f.can.bind("<Button-1>",f.useradd)
f.can.bind("<Button-3>",f.userdel)
f.eachframe()
tk.mainloop()

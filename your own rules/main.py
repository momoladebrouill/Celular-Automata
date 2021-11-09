import tkinter as tk

class Fen(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.can=tk.Canvas(self,width=500,height=500)
        self.title("JEan")
        self.can.pack(expand=tk.YES)
        self.can["bg"]="black"
        self.isrunning=tk.BooleanVar(self,False)
        tk.Checkbutton(self,text="run the simulation",
                       variable=self.isrunning).pack()
    def eachframe(self):
        if self.isrunning.get():
            for elem in self.can.find_all():
                print(self.can.itemcget(elem,"x"))
        else:
            print(self.can.find_withtag("(0, 0)"))
        self.after(20,self.eachframe)
    def truc(self,event):
        pos=event.x//10*10,event.y//10*10
        self.can.create_rectangle(pos[0],pos[1],pos[0]+10,pos[1]+10,
                                  fill="white",tag=f"{pos}")
        
        

f=Fen()
f.can.bind("<Button>",f.truc)
f.eachframe()

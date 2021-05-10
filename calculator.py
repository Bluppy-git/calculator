from tkinter import *
from math import *

#calculating method
def calculate(event):
    gleichung = t.get()
    t.delete(0,END)
    try:
            t.insert(0, eval(gleichung))
    except:
            t.insert(0, "invalid syntax")


top = Tk()
top.title("calculator")
t = Entry(top)
t.grid(row=0,columnspan=5)

#where the button is and the symbol on top of the button
b1 = Button(top,text=" 1 ")
b1.grid(row=1,column=0)

b2 = Button(top,text=" 2 ")
b2.grid(row=1,column=1)

b3 = Button(top,text=" 3 ")
b3.grid(row=1,column=2)                     

b4 = Button(top,text=" 4 ")
b4.grid(row=2,column=0)

b5 = Button(top,text=" 5 ")
b5.grid(row=2,column=1)

b6 = Button(top,text=" 6 ")
b6.grid(row=2,column=2)

b7 = Button(top,text=" 7 ")
b7.grid(row=3,column=0)

b8 = Button(top,text=" 8 ")
b8.grid(row=3,column=1)

b9 = Button(top,text=" 9 ")
b9.grid(row=3,column=2)

b0 = Button(top,text=" 0 ")
b0.grid(row=4,column=1)

bp =Button(top,text=" + ")
bp.grid(row=3,column=3)

bm =Button(top,text="  - ")
bm.grid(row=3,column=4)                     

bmu =Button(top,text="  x ")
bmu.grid(row=2,column=3)

bd =Button(top,text=" ÷ ")
bd.grid(row=2,column=4)

be =Button(top,text=" = ")
be.grid(row=4,column=3)

bdel =Button(top,text=" DEL ")
bdel.grid(row=4,column=2)

bwur =Button(top,text=" √ ")
bwur.grid(row=2,column=5)

bkla =Button(top,text="  (  ")
bkla.grid(row=1,column=3)

bklz =Button(top,text="  ) ")
bklz.grid(row=1,column=4)

bkom =Button(top,text="  ,  ")
bkom.grid(row=4,column=4)

bh2 =Button(top,text="  ² ")
bh2.grid(row=3,column=5)

bh3 =Button(top,text="  ³ ")
bh3.grid(row=4,column=5)

bclr =Button(top,text=" CLR ")
bclr.grid(row=4,column=0)

bπ =Button(top,text=" π ")
bπ.grid(row=1,column=5)


#what the button does
b1.bind("<Button-1>", lambda x:t.insert(END,"1"))
b2.bind("<Button-1>", lambda x:t.insert(END,"2"))
b3.bind("<Button-1>", lambda x:t.insert(END,"3"))
b4.bind("<Button-1>", lambda x:t.insert(END,"4"))
b5.bind("<Button-1>", lambda x:t.insert(END,"5"))
b6.bind("<Button-1>", lambda x:t.insert(END,"6"))
b7.bind("<Button-1>", lambda x:t.insert(END,"7"))
b8.bind("<Button-1>", lambda x:t.insert(END,"8"))
b9.bind("<Button-1>", lambda x:t.insert(END,"9"))
b0.bind("<Button-1>", lambda x:t.insert(END,"0"))
bp.bind("<Button-1>", lambda x:t.insert(END,"+"))
bm.bind("<Button-1>", lambda x:t.insert(END,"-"))
bmu.bind("<Button-1>", lambda x:t.insert(END,"*"))
bd.bind("<Button-1>", lambda x:t.insert(END,"÷"))
bwur.bind("<Button-1>", lambda x:t.insert(END,"sqrt("))
be.bind("<Button-1>", calculate)              
bdel.bind("<Button-1>",lambda x:t.delete(len(t.get())-1),END)
bkla.bind("<Button-1>", lambda x:t.insert(END,"("))
bklz.bind("<Button-1>", lambda x:t.insert(END,")"))
bkom.bind("<Button-1>", lambda x:t.insert(END,"."))
bh2.bind("<Button-1>", lambda x:t.insert(END,"**"))
bh3.bind("<Button-1>", lambda x:t.insert(END,"***"))
bclr.bind("<Button-1>", lambda x: t.delete(0,END))
bπ.bind("<Button-1>", lambda x: t.insert(END,"3,141592654"))

top.mainloop()
from Tkinter import *
 
a=1
def oval_func(event):
    global a    
    if a==1:
        cv.create_oval(30,10,100,80,fill='orange')
        a=-1
    else:
        cv.create_oval(30,10,100,80,fill='black')    
        a=1
cv = Canvas(width=150,height=100,bg='grey80')
cv.create_oval(30,10,100,80,fill='black')
cv.pack(side=LEFT)
 
but=Button()
but['text'] ='Taster'
but.pack(side=LEFT)
 
but.bind('<Button-1>',oval_func)
mainloop()
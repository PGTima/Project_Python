import pyowm
from tkinter import *


main_window=Tk()
main_window.title('Погода в твоем городе')
 
text1=Text(main_window,height=1,width=13,font='Arial 14',wrap=WORD)


button1=Button(main_window,
	text='Введите город',
	width=13,
	height=1,
	bg='white',
	fg='black',
	font='arial 14')
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()

check1=Checkbutton(main_window,text='Ветер',variable=var1,onvalue=1,offvalue=0)
check2=Checkbutton(main_window,text='Давление',variable=var2,onvalue=1,offvalue=0)
check3=Checkbutton(main_window,text='Влажность',variable=var3,onvalue=1,offvalue=0)
check4=Checkbutton(main_window,text='Давление',variable=var4,onvalue=1,offvalue=0)

text1.pack()
button1.pack()
check1.pack()
check2.pack()
check3.pack()
check4.pack()

main_window.mainloop()



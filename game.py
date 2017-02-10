from  tkinter import *
from  random import *
import os


prev=None # None  -ничто

def cmd():
	pass

def hide_all(buttons):
	'''Прячет текст на кнопках
	'''
	for i in range(SIDE):
		for j in xrange(SIDE):
			buttons[i][j].configure(text='?')
		


def hide_both(buttons,i1,j1,j1,j2):
	buttons[i1][j1].configure(text='?')
	buttons[i2][j2].configure(text='?')
	

def change(buttons,i,j):
	global prev
	buttons[i][j].configure(text='{:>3}'.format(nums[i*SIDE+j])) #text=nums[i*SIDE+j])
	if prev is None:
		prev=(i.j)
	else:
		if nums[i*SIDE+j]!=nums[prev[0]*SIDE+prev[1]]:
			main_window.after(2000, hide_both(buttons,prev[0],prev[1],i,j), buttons)
				
		prev=None
		

main_window=Tk()
main_window.title('Запоминалка')
faq=PhotoImage(file'Faq.gif')

images=[PhotoImage(file'Faq.gif') for f in 
SIDE=6;
QSIDE=SIDE**2//2

#nums=[]
#for i in range(a,100):
#	nums.append(i)
#	print(nums)
#nums=[i**2 for i in range(1,100)]#список квадратов чисел
nums=list(range(1,100))
shuffle(nums)	
nums=nums[0:QSIDE] *2  # Срез  от 0 элемента до QSIDE и дублируем переменные
shuffle(nums)

files=[os.path.join('gif',f) for f in os.listdir('gif')]
shuffle(files)	
files=files[0:QSIDE] *2  # Срез  от 0 элемента до QSIDE и дублируем переменные
shuffle(files)
print('Memorizer')
buttons=[]

for i in range(SIDE):
	buttons.append([])
	for j in range(SIDE):
		button=tkinter.button(main_window
			            ,text='{:>3}'.format(nums[i*SIDE+j])
			           # ,text=nums[i*SIDE+j]
						,font=()
		                ,command=lambda ii=i,jj=j:change(buttons,ii,jj))
        #button.pack()
        button.grid(row=i,column=j)
		buttons[i].append(button)




main_window.after(2000, hide_all, buttons)
main_window.mainloop()

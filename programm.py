# import tkinter                # импорт (подключение библиотекиа)
import pyowm
from tkinter import *         # импортировать всё, что есть в tkinter
from random import shuffle
import os
# import time     # хочется использовать time.sleep(), но для GUI-интерфейса не пойдет
# import pdb      # <- родной питоновский отладчик (консольный)

SIDE = 6                        # Размерность квадратной таблицы кнопок
QSIDE = SIDE ** 2 // 2          # Количество уникальных значений в таблице

# --- Заполнение списка числами ---
# Вариант 1. Простой
# nums = []
# for i in range(1,100):
#     nums.append(i)

# Вариант 2. Генератор списка (функциональный подход)
# nums = [i**2 for i in range(1, 100)]      # <- список квадратов чисел от 1 до 99

# Вариант 3. Просто преобразуем генератор range к списку
nums = list(range(1, 100))

shuffle(nums)            # <- перемешиваем список
nums = nums[:QSIDE] * 2  # <- берем срез нужного размера и размножаем его
shuffle(nums)            # <- еще раз перемешиваем
print(nums)              # <- контрольный вывод

# По аналогии с числами сделаем список из имён файлов
files = [os.path.join('gif', f) for f in os.listdir('gif')]
# os.path.join('gif', f) - кроссплатформенное формирование пути к файлу
# os.listdir('gif') - список файлов в директории gif

shuffle(files)
files = files[:QSIDE] * 2
shuffle(files)
   

print('Memorizer')

# SublimeREPL   - плагин для запуска Python-кода прямо в Sublime

prev = None     # Для хранения координат предыдущей нажатой кнопки

def cmd():      # Функция в Питоне - без операторных скобок. Вся суть - в отступах
    ''' Документация для функции пишется в многострочной строке
        сразу после заголовка. Эта документация выводится функцией help()
    '''
    print('ПРИВЕТ')
    print('Я полезная функция')
                # Может что-то возвращать, тогда нужен return
                # Если ничего не возвращает, тогда можно без return'а


def hide_all(buttons):
    ''' Прячет текст на всех кнопках из списка
    '''
    pass        # nop - No Operation ;;
    for i in range(SIDE):
        for j in range(SIDE):
            # buttons[i][j].configure(text=' ? ')
            buttons[i][j].configure(image=faq)


def hide_both(buttons, i1, j1, i2, j2):
    ''' Прячет текст на кнопках с координатами (i1, j1) и (i2, j2)
    '''
    # buttons[i1][j1].configure(text=' ? ')
    # buttons[i2][j2].configure(text=' ? ')
    buttons[i1][j1].configure(image=faq)
    buttons[i2][j2].configure(image=faq)


opened = []         # Список координат уже открытых кнопок

def change(buttons, i, j):
    ''' Изменение текста/изображения на кнопках.
        Будет применяться как обработчик нажатия кнопок.
    '''
    if (i, j) in opened:    # Если кнопка уже открыта - выходим из функции   
        return

    global prev     # Используем глобальную переменную координат предыдущей кнопки

    # buttons[i][j].configure(text='{:>3}'.format(nums[i * SIDE + j]))
    buttons[i][j].configure(image=images[i * SIDE + j])

    if prev is None:        # Если до этого не была нажата никакая кнопка, то...
        prev = (i, j)       # ... запоминаем координаты текущей нажатой кнопки

    else:                   # Если же до этого была нажата какая-то кнопка...
                            # ... нужно ее проверить...
        # if nums[i * SIDE + j] != nums[prev[0] * SIDE + prev[1]]:
        if files[i * SIDE + j] != files[prev[0] * SIDE + prev[1]] \
            or prev == (i, j):       # Аналогия: prev[0] == i and prev[1] == j:

            # Метод after() позволяет запустить указанную функцию (hide_both)
            # через указанное количество милисекунд (1000)
            main_window.after(1000, hide_both, buttons, prev[0], prev[1], i, j)
        else:
            opened.extend([prev, (i, j)])    

        prev = None         # Забываем нажатую кнопку сразу после второго нажатия 


# def <lambda> (x, y): return x ** y        # <- так лямбда-функция могла бы быть записана 
                                            # в обычном виде объявления функций


main_window = Tk()                              # Создаём объект главного окна
main_window.title('Запоминалка')                # Устанавливаем заголовок

faq = PhotoImage(file='FAQ.gif')                # Создаём картинку со знаком вопроса

images = [PhotoImage(file=f) for f in files]    # Создаём список объектов-картинок
                                                # на основании сгенерированного выше списка файлов

# PEP-8 - рекомендации по оформлению кода

buttons = []                                    # <- список всех кнопок

for i in range(SIDE):                           # В Питоне есть 2 оператора циклов while и for
    buttons.append([])                          
    for j in range(SIDE):                       # Цикл for очень удобен для обхода последовательностей,
                                                # работает по принципу foreach - перебрать все элементы
                                                # т.е. j будет на каждом шаге цикла хранить новое значение из range

        # Создание объекта класса Button (кнопка)                                                
        button = Button(main_window,            
                                # text=' ? ',   # <- текст на кнопке
                                # text='{:>3}'.format(nums[i * SIDE + j]),
                                # text=nums[i * SIDE + j],
                                # font=('Courier New', 12, 'normal'),   # <- стиль шрифта (для картинок не нужен)
                                # image=faq,
                                image=images[i * SIDE + j],             # <- картинка на кнопке
                                relief=FLAT,                            # <- стиль кнопки - плоская
                                            # command - функция, которая будет выполнена при нажатии на кнопку
                                command=lambda ii=i, jj=j: change(buttons, ii, jj))

        buttons[i].append(button)           # <- формирование списка кнопок

        # button.pack()         # .pack() / .grid() - разные способы размещения объектов в окне tkinter
        button.grid(row=i, column=j)


main_window.after(2000, hide_all, buttons)  # <- метод after() позволяет запустить указанную функцию (hide_all)
                                            # через указанное количество милисекунд (2000)

main_window.mainloop()                      # <- запуск основного цикла обработки событий tkinter-окна
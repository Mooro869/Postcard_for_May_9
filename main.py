# coding: utf8
import pygame
import time
from tkinter import *
from PIL import ImageTk

root = Tk()
root.title('Открытка: "9 мая"')
root.resizable(width=False, height=False)
cWidth = 1280
cHeight = 720
c = Canvas(root, width=cWidth, height=cHeight, bg='#263A29')
c.pack()

# Звезда
star = ImageTk.PhotoImage(file='zvzda.png')
c.create_image(100, 100, image=star, anchor=NW)

# Танк
photo_tank = PhotoImage(file='skorpion-tank.gif')
tank = c.create_image(700, 1, image=photo_tank, anchor=NW)

# Самолет
photo_fly = PhotoImage(file='spitfire-fighter-aircraft.gif')
fly = c.create_image(900, -1, image=photo_fly, anchor=NW)

def move_all(): # Движение объектов
    while True:
        # Движение танка
        c.move(tank, -1, 0)
        c.update()

        # Движение самолета
        c.move(fly, -5, 5)
        c.update()
        time.sleep(0.05)

def createText():
    cText = ('''
С Победой! Этот день великий
Мы не забудем никогда.
За наш покой и счастье люди
Отдали жизни навсегда.  

Желаю жить и дальше в мире,
Чтоб не тревожила война,
Чтоб беды дом ваш обходили,
Чтоб на душе была весна.
    ''')
    c.create_text(cWidth * 2 / 3, cHeight / 2, text=cText, fill='red', font='Times 24 bold')

# Запуск музыки
pygame.mixer.init()
pygame.mixer.music.set_volume(0.1) # Громкость песни
pygame.mixer.music.load("Den_Pobedy.mp3") # Файл с музыкой
pygame.mixer.music.play() # Воспроизведение песни

createText()
move_all()

root.mainloop()
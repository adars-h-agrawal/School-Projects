import random
from tkinter import *
from random import randint

win = Tk()    #  Game Window creation for game
win.geometry('700x160')
win.title('Switch Game')
win.resizable(0, 0)
exit = True
chance = 12
c = 0
l = ['OFF.png', 'ON.png']
i = True
x = [20, 130, 240, 350, 460, 570]

values = [1, 1, 1, 1, 1, 1]

on1 = PhotoImage(file = l[i])
on2 = PhotoImage(file = l[i])
on3 = PhotoImage(file = l[i])
on4 = PhotoImage(file = l[i])
on5 = PhotoImage(file = l[i])
on6 = PhotoImage(file = l[i])

images = [on1, on2, on3, on4, on5, on6]

# Game Logic
def find(l, n):
                    # Checking for  switch which are Off
    index =[]
    i = 0
    while i < 6:
        if l[i] == 0 and i != n-1:
            index.append(i)

        i+=1

    return index

def switch(t ,e):  #  Randomly swichting off the button after user choice
    global images, btn
    on = PhotoImage(file = l[not(bool(t))])
    images[e] = on

    btn_c = Button(win, image = on, command = lambda:click(e+1))
    btn[e] = btn_c
    btn[e].place(x = x[e], y = 50)




def click (n): # Handling All Switch Buttons
    global images, values, on1, on2, on3, on4, on5, on6, i, c, exit, chance, txt, btn1, btn2, btn3, btn4, btn5, btn6
    if n == 1:
        btn1.destroy()
        if values[0]:
            values[0] = 0
        else:
            values[0] = 1
        on1 = PhotoImage(file = l[bool(values[0])])
        images[0] = on1
        btn1 = Button(win, image = images[0], command = lambda : click(1))
        btn1.place(x = x[n-1], y = 50)

    if n == 2:
        btn2.destroy()
        if values[1]:
            values[1] = 0
        else:
            values[1] = 1
        on2 = PhotoImage(file = l[bool(values[1])])
        images[1] = on2
        btn2 = Button(win, image = images[1], command = lambda : click(2))
        btn2.place(x = x[n-1], y = 50)

    if n == 3:
        btn3.destroy()
        if values[2]:
            values[2] = 0
        else:
            values[2] = 1
        on3 = PhotoImage(file=l[bool(values[2])])
        images[2] = on3
        btn2 = Button(win, image=images[2], command=lambda: click(3))
        btn2.place(x=x[n-1], y=50)

    if n == 4:
        btn4.destroy()
        if values[3]:
            values[3] = 0
        else:
            values[3] = 1
        on4 = PhotoImage(file=l[bool(values[3])])
        images[3] = on4
        btn4 = Button(win, image=images[3], command=lambda: click(4))
        btn4.place(x=x[n-1], y=50)

    if n == 5:
        btn5.destroy()
        if values[4]:
            values[4] = 0
        else:
            values[4] = 1
        on5 = PhotoImage(file=l[bool(values[4])])
        images[4] = on5
        btn5 = Button(win, image=images[4], command=lambda: click(5))
        btn5.place(x=x[n-1], y=50)

    if n == 6:
        btn6.destroy()
        if values[5]:
            values[5] = 0
        else:
            values[5] = 1
        on6 = PhotoImage(file=l[bool(values[5])])
        images[5] = on6
        btn6 = Button(win, image=images[5], command=lambda: click(6))
        btn6.place(x = x[n-1], y=50)
    avail = [1, 0]
    rand = random.choices(avail, weights=(60, 40))
    rand = int(rand[0])

    if bool(rand) and c >= 1:
        off  = find(values ,n)
        element = random.choice(off)
        t = values[element]
        if bool(values[element]):
            values[element] = 0
        else:
            values[element] = 1

        switch(t, element)
    c+=1
    chance-=1
    txt.destroy()
    txt = Label(win, text=f'Chances Left: {chance}', font='Helvetica 15 bold')
    txt.place(x=500, y=20)
    exit = True
    for j in values:
        if j == 1:
            exit = False
    if exit:
        win.destroy()
        print('You Win')
    elif chance == 0:
        win.destroy()
        print('You Lose')

# Placing Buttons On The Screen

btn1 = Button(win, image = images[0], command = lambda :click(1))
btn1.place(x = 20, y = 50)

btn2 = Button(win, image=images[1], command = lambda :click(2))
btn2.place(x = 130, y = 50)

btn3 = Button(win, image = images[2], command = lambda :click(3))
btn3.place(x = 240, y = 50)

btn4 = Button(win, image = images[3], command = lambda :click(4))
btn4.place(x = 350, y = 50)

btn5 = Button(win, image = images[4], command = lambda :click(5))
btn5.place(x = 460, y = 50)

btn6 = Button(win, image = images[5], command = lambda :click(6))
btn6.place(x = 570, y = 50)

txt = Label(win, text= f'Chances Left: {chance}', font = 'Helvetica 15 bold')
txt.place(x = 500, y = 20)

btn =[btn1, btn2, btn3, btn4, btn5, btn6]


win.mainloop()  #Main Game Loop Which updates all user Events
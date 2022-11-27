from tkinter import *
window = Tk()
window.minsize(700, 400)
window.title("Ball")

def rool ():
    global ball_x
    global dX
    global ball_y
    global dY
    ball_x = ball_x + dX
    ball_y = ball_y + dY
    canvas.coords(ball, ball_x+20, ball_y+20, ball_x+diametr, ball_y+diametr)

    if ball_x + diametr >= 700:
        dX = dX * -1
    if ball_y + diametr >= 400:
        dY = dY * -1
    if ball_y + diametr <= 30:
        dY = dY * -1
    if ball_x + diametr <= 30:
        dX = dX * -1

    window.after(25, rool)
    

canvas = Canvas(background="Orange")
canvas.pack(fill=BOTH, expand=YES)

ball_x = 100
ball_y = 100
diametr = 50

dX = 3
dY = 3
ball = canvas.create_oval(ball_x, ball_y, ball_x+diametr, ball_y+diametr)

window.after(25, rool)
window.mainloop()
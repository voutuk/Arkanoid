#   Імпорт
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Radiobutton
import sys
#   Конфіг лаунчера
launcher = Tk()
launcher.resizable(0,0)
launcher.title("Лаунчер Arkanoid")
w = 400
h = 500
sw = launcher.winfo_screenwidth()
sh = launcher.winfo_screenheight()
x = (sw - w) / 2
y = (sh - h) / 2
launcher.minsize(w, h)
launcher.geometry('%dx%d+%d+%d' % (w, h, x, y))
#   Місце для потеряшок
bals = 0
lv = 0
threme = 1
#   Налаштування кнопок теми
def pink():
    global threme
    btn.config(bg=("Pink"), fg=("Black"))
    threme = 1
def black():
    global threme
    btn.config(bg=("Black"), fg=("White"))
    threme = 2
def lop():
    global threme
    btn.config(bg=("Blue"), fg=("White"))
    threme = 3
#  Робота кнопки складності
def level():
    global lv
    global platform_width
    if lv == 0:
        testbtn.config(text="Нереально", bg=("#F85C50"), fg=("White"))
        lv = 1
    elif lv == 1:
        testbtn.config(text="Легко", bg=("#8CBA51"), fg=("White"))
        lv = 2
    elif lv == 2:
        testbtn.config(text="Нормально", bg=("#FED876"), fg=("Black"))
        lv = 0
#   Код арканоіда
def start():
    def close_window():
        window.destroy()
        launcher.destroy()
    #   Нове вікно
    window = Toplevel(launcher)
    #   Закрити старе вікно
    launcher.withdraw()
    #   Правильне закриття
    def on_close():
        if messagebox.askokcancel("Вихід з гри", "Повернутися в лаунчер?"):
            launcher.deiconify()
            window.destroy()
        else:
            sys.exit()
    window.protocol("WM_DELETE_WINDOW", on_close)
    #   Місце під глобали
    global threme
    global ball_x
    global ball_y
    global diametr
    global dX
    global dY
    global platform_height
    global platform_width
    global platform_y
    global platform_x
    global width
    global height
    global fast
    global balis
    global lv
    global bal
    #   Переключення тем
    if threme == 2:
        bg_col = "White"
        ov_col = "Black"
        pl_col = "Black"
    elif threme == 3:
        bg_col = "Blue"
        ov_col = "Black"
        pl_col = "Black"
    else:
        bg_col = "Pink"
        ov_col = "White"
        pl_col = "White"
    #   Переключення складності
    if lv == 0:
        dX = 4
        dY = 4
    elif lv == 1:
        dX = 6
        dY = 6
        platform_width = 50
    elif lv == 2:
        dX = 2
        dY = 2
    #   Рух платформи ліво
    def left(event):
        global platform_x
        platform_x = platform_x - 20
        canvas.coords(platform, platform_x, platform_y, platform_x + platform_width, platform_y + platform_height)
        if platform_x <= 20:
            platform_x = platform_x + 20
    #   Рух платформи право
    def right(event):
        global platform_x
        platform_x = platform_x + 20
        canvas.coords(platform, platform_x, platform_y, platform_x + platform_width, platform_y + platform_height)
        if platform_x >= 680 - platform_width:
            platform_x = platform_x - 20
    #   Кадри
    def roll():
        #   Глобали
        global ball_x
        global dX
        global ball_y
        global dY
        global width
        global height
        global bal
        global tecas
        #   Зчитування інформації про вікно
        width = window.winfo_width()
        height = window.winfo_height()
        #   Рух кола
        ball_x = ball_x + dX
        ball_y = ball_y + dY
        canvas.coords(ball, ball_x, ball_y, ball_x + diametr, ball_y + diametr)
        #   Відбивання кола від стінок по X
        if ball_x + diametr >= width or ball_x <= 0:
            dX = dX * -1
        #   Відбивання кола від стінок по Y
        if ball_y + diametr >= height or ball_y <= 0:
            dY = dY * -1
        #   Програш
        if ball_y + diametr >= 400:
            messagebox.showinfo("Лаунчер Arkanoid", "Нажаль ви програли! Продовжити гру?")
        #   Відбивання кола від платформи збоку
        if ball_y + diametr >= platform_y and ball_x + diametr >= platform_x and ball_x <= platform_x + platform_width:
            dX = dX * -1
        #   Відбивання кола від платформи зверху
        elif ball_y + diametr >= platform_y - dY and ball_x + diametr >= platform_x and ball_x <= platform_x + platform_width:
            dY = dY * -1
            global bals
            bals = bals + 1
            balis = "Coin: " + str(bals)
            coins.config(text=balis)
        #   Повтори
        window.after(10, roll)
    #   Налаштування вікна
    window.resizable(0, 0) 
    window.minsize(width, height)
    window.title("Arkanoid")
    #   Канвас
    canvas = Canvas(window, bg=bg_col, highlightthickness=0)
    canvas.pack(fill=BOTH, expand=YES)
    coins = Label(window, text="Coin: 0", justify=CENTER, font="Verdana 14", fg=(ov_col), bg=(bg_col))
    canvas_widget = canvas.create_window(640, 20, window=coins)
    #   Коло, платформа
    ball = canvas.create_oval(ball_x, ball_y, ball_x + diametr, ball_y + diametr, fill=ov_col)
    platform = canvas.create_rectangle(platform_x, platform_y, platform_x + platform_width, platform_y + platform_height, fill=pl_col)
    #   Бінд клавіш
    window.bind("<Left>", left)
    window.bind("<Right>", right)
    window.bind("<a>", left)
    window.bind("<d>", right)
    #   Запуск кола
    roll()
#   Інтерфейс
label678 = Label(launcher, text=" ").pack()
label5 = Label(launcher, text=" ").pack()
label1 = Label(launcher, text="Арканоід", font=("Lucida", 50)).pack()
label2 = Label(launcher, text="Налаштуй гру на свій смак!", font=("Arial Bold", 10)).pack()
label5 = Label(launcher, text=" ").pack()
label3 = Label(launcher, text="Вибери складність: ", font=("Arial Bold", 10)).pack()
testbtn = Button(launcher, bg=("#FED876"), fg=("Black"), text="Нормально", font=("Arial Bold", 11), command=level)
testbtn.pack()
label99 = Label(launcher, text=" ").pack()
label3 = Label(launcher, text="Вибери тему: ", font=("Arial Bold", 10)).pack()
rad1 = Radiobutton(launcher,text='Рожева', value=1, command=pink).pack()
rad2 = Radiobutton(launcher,text='Чорнобіла', value=2, command=black).pack()
rad3 = Radiobutton(launcher,text='Стара', value=3, command=lop).pack()
label56 = Label(launcher, text="         ").pack()
btn = Button(launcher, bg=("#DCE5E7"), fg=("Black"), text="Почати", font=("Arial Bold", 15), command=start)
btn.pack()
#   Данні
width = 700
height = 400
ball_x = 350
ball_y = 200
diametr = 50
dX = 4
dY = 4
platform_width = 150
platform_height = 30
platform_y = 350
platform_x = 400 - platform_width / 2
cube_width = 30
cube_height = 30
cube_y = 100
cube_x = width / 2 - platform_width / 2
#   Нарешті я закінчив цю програму
launcher.mainloop()
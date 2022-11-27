#   Імпорт (Не оптимізовано)
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Radiobutton
import sys
import time
#   Конфіг лаунчера (Оптимізовано)
launcher = Tk()
launcher.resizable(0,0)
launcher.title("Лаунчер Arkanoid")
x = (launcher.winfo_screenwidth() - 400) / 2
y = (launcher.winfo_screenheight() - 500) / 2
launcher.minsize(400, 500)
launcher.geometry('%dx%d+%d+%d' % (400, 500, x, y))
#  Робота кнопки складності (Оптимізовано)
def level():
    global data
    if data[13] == 0:
        testbtn.config(text="Нереально", bg=("#F85C50"), fg=("White"))
        data[13] = 1
    elif data[13] == 1:
        testbtn.config(text="Легко", bg=("#8CBA51"), fg=("White"))
        data[13] = 2
    elif data[13] == 2:
        testbtn.config(text="Нормально", bg=("#FED876"), fg=("Black"))
        data[13] = 0
#   Код арканоіда
def start():
    global data
    #   Нове вікно та закриття лаунчера
    window = Toplevel(launcher)
    launcher.withdraw()
    #   Правильне закриття  (Оптимізовано)
    def on_close():
        global data
        data[11] = 1
        if messagebox.askokcancel("Вихід з гри", "Повернутися в лаунчер?"):
            data = [700, 400, 350, 200, 50, 4, 4, 150, 30, 350, 125, 0, 0, 0, 0, "❤❤❤ "]
            launcher.deiconify()
            window.destroy()
        else:
            sys.exit()
    window.protocol("WM_DELETE_WINDOW", on_close)
    #   Переключення тем  (Оптимізовано)
    if selected.get() == 2:
        bg_col = "Pink"
        ov_col = "White"
        pl_col = "White"
    elif selected.get() == 3:
        bg_col = "#58595B"
        ov_col = "#939598"
        pl_col = "#939598"
    else:
        bg_col = "Blue"
        ov_col = "Black"
        pl_col = "Black"
    #   Переключення складності  (Оптимізовано)
    if data[13] == 0:
        data[5] = 4
        data[6] = 4
    elif data[13] == 1:
        data[5] = 6
        data[6] = 6
        data[7] = 50
    elif data[13] == 2:
        data[5] = 2
        data[6] = 2
    #   Рух платформи ліво (Не оптимізовано)
    def left(event):
        data[10] = data[10] - 20
        canvas.coords(platform, data[10], data[9], data[10] + data[7], data[9] + data[8])
        if data[10] <= 20:
            data[10] = data[10] + 20
    #   Рух платформи право  (Не оптимізовано)
    def right(event):
        data[10] = data[10] + 20
        canvas.coords(platform, data[10], data[9], data[10] + data[7], data[9] + data[8])
        if data[10] >= 680 - data[7]:
            data[10] = data[10] - 20

    #   Кадри
    def roll():
        global data
        #   Зчитування інформації про вікно
        data[0] = window.winfo_width()
        data[1] = window.winfo_height()
        #   Рух кола
        data[2] = data[2] + data[5]
        data[3] = data[3] + data[6]
        canvas.coords(ball, data[2], data[3], data[2] + data[4], data[3] + data[4])
        #   Відбивання кола від стінок по X
        if data[2] + data[4] >= data[0] or data[2] <= 0:
            data[5] = data[5] * -1
        #   Відбивання кола від стінок по Y
        if data[3] + data[4] >= data[1] or data[3] <= 0:
            data[6] = data[6] * -1
        #   Програш
        if data[3] + data[4] >= 400:
            if data[11] == 0:
                messagebox.showinfo("Лаунчер Arkanoid", "Нажаль ви програли! Продовжити гру?")
                data[14] += 1
        #   Відбивання кола від платформи збоку
        if data[3] + data[4] >= data[9] and data[2] + data[4] >= data[10] and data[2] <= data[10] + data[7]:
            data[5] = data[5] * -1
        #   Відбивання кола від платформи зверху
        elif data[3] + data[4] >= data[9] - data[6] and data[2] + data[4] >= data[10] and data[2] <= data[10] + data[7]:
            data[6] = data[6] * -1
            #   Рахунок coin
            if data[14] == 1:
                data[15] = "❤❤❤ "
            elif data[14] == 2:
                data[15] = "❤❤ "
            elif data[14] == 3:
                data[15] = "❤ "
            elif data[14] == 4:
                messagebox.showinfo("Лаунчер Arkanoid", "Ви повністю програли! Повернутися в лаунчер?")
                data = [700, 400, 350, 200, 50, 4, 4, 150, 30, 350, 125, 0, 0, 0, 0, "❤❤❤ "]
                launcher.deiconify()
                window.destroy()
            data[12] += 1
            cointext = str(data[15]) + "Coin: " + str(data[12])
            coins.config(text=cointext)
        #   Повтори
        #time.sleep(0.005)
        window.after(10, roll)
    #   Налаштування вікна
    window.resizable(0, 0)
    window.minsize(data[0], data[1])
    window.title("Arkanoid")
    #   Канвас
    canvas = Canvas(window, bg=bg_col, highlightthickness=0)
    canvas.pack(fill=BOTH, expand=YES)
    coins = Label(window, text="❤❤❤ Coin: 0", justify=CENTER, font="Verdana 14", fg=(ov_col), bg=(bg_col))
    canvas_widget = canvas.create_window(620, 20, window=coins)
    #   Коло, платформа
    ball = canvas.create_oval(data[2], data[3], data[2] + data[4], data[3] + data[4], fill=ov_col)
    platform = canvas.create_rectangle(data[10], data[9], data[10] + data[7], data[9] + data[8], fill=pl_col)
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
def retro():
    btn.config(bg=("Blue"), fg=("White"))
def pink():
    btn.config(bg=("Pink"), fg=("Black"))
def gray():
    btn.config(bg=("#58595B"), fg=("White"))
selected = IntVar()
rad1 = Radiobutton(launcher, text="Ретро", value=1, variable=selected, command=retro)
rad2 = Radiobutton(launcher, text="Рожева", value=2, variable=selected, command=pink)
rad3 = Radiobutton(launcher, text="Сіра", value=3, variable=selected, command=gray)
rad1.pack()
rad2.pack()
rad3.pack()
label56 = Label(launcher, text="         ").pack()
btn = Button(launcher, bg=("#DCE5E7"), fg=("Black"), text="Почати", font=("Arial Bold", 15), command=start)
btn.pack()
#   Данні
data = [700, 400, 350, 200, 50, 4, 4, 150, 30, 350, 125, 0, 0, 0, 0, "❤❤❤ "]
#   Нарешті я закінчив цю програму
launcher.mainloop()
from cgitb import text
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.animation as animation

import tkinter as tk
from tkinter import Label, messagebox

from funcs.math_funcs import funcs

window = tk.Tk()

window.title("GRAFICADOR DE ECUACION CON SU DERIVADA E INTEGRAL")
window.geometry("900x900")

fig, ax = plt.subplots()


label1 = Label(window, text="Ecuacion")
label1.pack(side=tk.TOP)

label2 = Label(window, text="Limites")
label2.pack(side=tk.TOP)

user_input = tk.Entry(window, width=100)
lims = tk.Entry(window, width=50)

user_input.pack(side=tk.TOP)
lims.pack(side=tk.TOP)

canvas = FigureCanvasTkAgg(fig, window)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

tools = NavigationToolbar2Tk(canvas, window)
tools.update()

r1 = False
r2 = ""
r3 = ""

def re(n):
    for i in funcs:
        if i in n:
            n = n.replace(i, funcs[i])
        return n

def create(x):
    if r1:
        try:
            min_value = float(r3[0])
            max_value = float(r3[1])
            if min_value < max_value:
                rango = np.linspace(min_value, max_value, 0.1)
                r2 = [min_value, max_value]
            else:
                r1 = False
        except Exception as e:
            messagebox.showwarning("Los limites que ingreso son incorrectos")
            r1 = False
            lims.delete(0, len(lims.get()))
    
    else :
        if r2 != "":
            rango = np.linspace(r2[0], r2[1], 0.1)
        else:
            x = np.linspace(-5, 5, 0.1)
    try:
        y = eval(data)
        ax.clear
        ax.plot(rango, y)
    except Exception as e:
        ax.plot()
    ax.axhline(0, color="red")
    ax.axvline(0, color="blue")
    ani.event_source.stop()

def graph():
    global data, r3, r1
    ecuation = user_input.get()
    if lims.get() != "":
        r = lims.get()
        r3 = r.split(",")
        r1 = True
    data = re(text)
    ani.event_source.start()

ani = animation, animation.FuncAnimation(fig, create, interval=1000)
plt.show()


submit = tk.Button(window, text="Plot", command="graph")
submit.pack(side=tk.BOTTOM)

window.mainloop()
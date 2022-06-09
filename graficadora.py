import numpy as np
import sympy as sm
from math import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib import style
import  matplotlib.animation as anim
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


import tkinter as tk
from tkinter import Label, messagebox


def derivative(eq, l):
    """Esta funcion calcula la derivada de la ecuacion que el usuario ingreso

    Args:
        eq (str): Es el input del usuario, el cual hace referencia a la ecuacion para graficar
        l (str): Es el tipo de variable para realizar la derivada de la ecuacion principal

    Returns:
        str: Retorna le ecuacion derivada
    """
    # a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = sm.symbols("a b c d e f g h i j k l m n o p q r s t u v w x y z")
    der = sm.diff(eq, sm.symbols(l))
    print(der)
    return str(der)

def integral(eq, l):
    """Esta funcion calcula la integral de la ecuacion que el usuario ingreso

    Args:
        eq (str): Es el input del usuario, el cual hace referencia a la ecuacion para graficar
        l (str): Es el tipo de variable para realizar la derivada de la ecuacion principal

    Returns:
        str: Retorna le ecuacion integrada
    """
    # a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = sm.symbols("a b c d e f g h i j k l m n o p q r s t u v w x y z")
    inte = sm.integrate(eq, sm.symbols(l))
    print(inte)
    return str(inte)

funcs = {
    "sin":"np.sin",
    "cos":"np.cos",
    "tan":"np.tan",
    "sqrt":"np.sqrt",
    "e":"np.exp",
    "log":"np.log",
    "pi":"np.pi",
}

window = tk.Tk()
fig = Figure()
ax = fig.add_subplot(111)
plt.style.use("ggplot")

window.title("GRAFICADOR DE ECUACION CON SU DERIVADA E INTEGRAL")
window.geometry("600x600")

cvs = FigureCanvasTkAgg(fig, window)
cvs.draw()
cvs.get_tk_widget().pack(side=tk.BOTTOM)
tools = NavigationToolbar2Tk(cvs, window)
tools.update()
cvs.get_tk_widget().pack(side=tk.TOP)

rango1 = False
rango2 = ""
rango3 = ""


def replace(eq):
    for i in funcs:
        if i in eq:
            eq = eq.replace(i, funcs[i])
        return eq


def calculate_eqs(i):
    global rango1
    global rango2
    if rango1:
        try:
            min = float(rango3[0])
            max = float(rango3[1])
            if min < max:
                x = np.arange(min , max, 0.01)
                rango2=[min, max]
            else:
                rango1 = False
        except:
            messagebox.showwarning("Error al ingresar los rangos")
            rango1 = False
            var.delete(0, len(var.get()))
    else:
        if rango2 != "":
            x = np.arange(rango2[0], rango2[1], 0.01)
        else:
            x = np.arange(0, 10, 0.01)
    
    try:
        y_1 = eval(graph_data)
        y_2 = eval(graph_data_derivative)
        y_3 = eval(graph_data_integral)
        ax.clear()
        ax.plot(x, y_1, label=f"Ecuacion {graph_data_derivative}", color="yellow")
        ax.plot(x, y_2, label=f"Derivada {graph_data_derivative}", color="purple")
        ax.plot(x, y_3, label=f"Integral {graph_data_integral}", color="red")

        ax.legend()
        
    
    except Exception as e:
        ax.plot()

    ax.axhline(0, color="red", alpha=0.6)
    ax.axvline(0, color="blue", alpha=0.6)
    ani.event_source.stop()

def plot():
    global graph_data
    global graph_data_derivative
    global graph_data_integral
    global rango3
    global rango1

    eq = main_func.get()
    if var.get() != "":
        ran = var.get()
        rango3 = ran.split(",")
        rango1 = True
    d_eq = derivative(eq, "x")
    i_eq = integral(eq, "x")
    graph_data = replace(eq)
    graph_data_derivative = replace(d_eq)
    graph_data_integral = replace(i_eq)
    print(graph_data)
    print(f"Derivada: {d_eq}")
    print(f"Integral: {i_eq}")
    ani.event_source.start()

ani = anim.FuncAnimation(fig, calculate_eqs, interval=1000)
plt.show()

btn = tk.Button(window, text="Plot", command=plot)
btn.pack(side=tk.BOTTOM)

main_func = tk.Entry(window, width=60)
main_func.pack(side=tk.TOP)

var = tk.Entry(window, width=20)
var.pack(side=tk.TOP)

window.mainloop()
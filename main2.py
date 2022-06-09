from cgitb import text
import numpy as np  
import matplotlib.pyplot as plt
import sympy as sm
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import time



funcs = {
    "sin":"np.sin",
    "cos":"np.cos",
    "tan":"np.tan",
    "sqrt":"np.sqrt",
    "e":"np.exp",
    "log":"np.log",
    "pi":"np.pi",
}
 

def replace(eq):

    for i in funcs:
        if i in eq:
            eq = eq.replace(i, funcs[i])
        return eq

def derivative(eq, l):

    # a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = sm.symbols("a b c d e f g h i j k l m n o p q r s t u v w x y z")
    der = sm.diff(eq, sm.symbols(l))
    print(der)
    return str(der)

def integral(eq, l):

    # a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = sm.symbols("a b c d e f g h i j k l m n o p q r s t u v w x y z")
    inte = sm.integrate(eq, sm.symbols(l))
    print(inte)
    return str(inte)

def plot(eq=None, der=None, inte=None, lims=["-5","5"]):

    l = lim.get()
    lims = l.split(",")
    # x = np.linspace(int(lims[0]), int(lims[1]))
    x = np.linspace(int(lims[0]), int(lims[1]))

    user_input = ecuacion.get()
    variable = var_respect.get()
    der = derivative(user_input, variable)
    inte = integral(user_input, variable)

    for i in funcs:
        if i in user_input:
            user_input = user_input.replace(i, funcs[i])
            print("Ecuacion transformada: ",user_input)

    for i in funcs:
        if i in der:
            der = der.replace(i, funcs[i])
            print("Derivada transformada: ",der)
    for i in funcs:
        if i in inte:
            inte = inte.replace(i, funcs[i])
            print("Interal transformada: ",inte)

    fig = Figure(figsize=(10,6), dpi=100)
    p_1 = fig.add_subplot(111)

    y_1 = eval(user_input)
    y_2 = eval(der)
    y_3 = eval(inte)

    
    p_1.clear()
    
    Label(window, text=f"Ecuacion Original: {user_input}").pack()
    Label(window, text=f"Derivada: {der}").pack()
    Label(window, text=f"Integral: {inte}").pack()

    p_1.plot(x, y_1, label="Ecuacion")
    p_1.plot(x, y_2, label="Derivada")
    p_1.plot(x, y_3, label="Integral")

    p_1.legend()


    canvas = FigureCanvasTkAgg(fig, master = window)  
    canvas.draw()
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,window)
    toolbar.update()
    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()

    # plt.legend()

    # plt.show()
        

window = Tk()
window.title("GRAFICADOR DE ECUACION CON SU DERIVADA E INTEGRAL")
window.geometry("600x600")          

label_eq = StringVar()
label_lims = StringVar()
label_var = StringVar()

label_eq.set("Ecuacion")
label_lims.set("Limites para evaluar")
label_var.set("Variable con respecto a derivar")

ecuacion = Entry(window)
lim = Entry(window)
var_respect = Entry(window)

ecuacion.pack()
lim.pack()
var_respect.pack()

btn = Button(master=window, command=plot, height=2, width=10, text="Plot")
btn.pack()



window.mainloop()




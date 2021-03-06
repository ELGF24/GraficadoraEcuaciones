import numpy as np  
import matplotlib.pyplot as plt
import sympy as sm

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
    """Esta funcion busca en el diccionario funcs si se encuentra la llave para hacer uso de los metodos de numpy y realizar las graficas

    Args:
        eq (str): Es el input del usuario, el cual hace referencia a la ecuacion para graficar

    Returns:
        str: Retorna la ecuacion modificada para poderla utilizar evaluar
    """
    for i in funcs:
        if i in eq:
            eq = eq.replace(i, funcs[i])
        return eq

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

def plot(eq, der, inte, lims):
    """Esta funcion genera las tres graficas con la ecuacion que ingreso el usuario, su derivada y su integral

    Args:
        eq (str): Es el input del usuario, el cual hace referencia a la ecuacion para graficar
        der (str): Es la ecuacion derivada
        inte (str): Es la ecuacion integrada
    """
    x = np.linspace(int(lims[0]), int(lims[1]))

    for i in funcs:
        if i in eq:
            eq = eq.replace(i, funcs[i])
            print("Ecuacion transformada: ",eq)

    for i in funcs:
        if i in der:
            der = der.replace(i, funcs[i])
            print("Derivada transformada: ",der)
    for i in funcs:
        if i in inte:
            inte = inte.replace(i, funcs[i])
            print("Interal transformada: ",inte)

    
    y_1 = eval(eq)
    y_2 = eval(der)
    y_3 = eval(inte)

    plt.title("Graficadora de ecuaciones")
    plt.grid()

    plt.plot(x, y_1, label=f"Ecuacion {eq}")
    plt.plot(x, y_2, label=f"Derivada {der}")
    plt.plot(x, y_3, label=f"Integral {inte}")

    plt.legend()

    plt.show()
        

            






if __name__ == "__main__":
    while True:
        print("GRAFICADORA DE ECUACIONES")
        eq = str(input("Ingresa la funcion a graficar, ex:(x**2+sin(x+2): "))
        var_res = input("Ingresa la variable a derivar/integrar con respecto: ")
        lims_in = input("Ingresa los limites separados por coma: ")
        lims = lims_in.split(",")

        der = derivative(eq, var_res)
        inte = integral(eq, var_res)
        print("Ecuacion: ", eq)
        print("Integral:", inte)
        print("Derivada:", der)
        
        plot(eq, der, inte, lims)

        cont = input("Desea realizar otra grafica? s/n: ")
        if cont == "s":
            continue
        else:
            break



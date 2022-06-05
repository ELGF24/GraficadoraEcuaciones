import matplotlib.pyplot as plt
import numpy as np
import sympy as sm

funcs = {
    "sin":"np.sin",
    "cos":"np.cos",
    "tan":"np.tan",
    "sqrt":"np.sqrt",
    "e":"np.exp",
    "log":"np.log",
    "pi":"np.pi",
}

def calculate_dif_intg():
    funciont = input("Ingresa la funcion a grafica, EX:(x**2+2*x+5): ")
    # diff = sm.diff
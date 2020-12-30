from math import cos
import numpy as np
import matplotlib.pyplot as plt
import math
import sympy as sy
import brain
import pandas as pd
class NewtonRapson:
    def __init__(self, funcion):
        self.funcion = funcion

    def calculate(self):

        ldict = {}
        sToCode  = "x = sy.symbols('x')\nf = myExp "
        sToCode = sToCode.replace("myExp", self.funcion)
        exec(sToCode, globals(), ldict)
        f = ldict['f']

        xi = 1
        itr = 6 # numero de iteraciones a realizar 

        xplt = np.linspace(0.00001, 100, 2000) #para funciones con los logs 
        yplt = np.array([], float)

        dx = sy.diff(f)
        dx = dx.doit()

        v = [f"f(x) = {f}" , f"f'(x) = {dx}" ,f"Xi = {xi}"]

        f = str(f)
        dx = str(dx)

        f = f.replace("exp", "math.exp")
        f = f.replace("cos", "math.cos")
        f = f.replace("sin", "math.sin")
        f = f.replace("log", "math.log")

        dx = dx.replace("exp", "math.exp")
        dx = dx.replace("cos", "math.cos")
        dx = dx.replace("sin", "math.sin")
        dx = dx.replace("log", "math.log")


        strCode = """fun = lambda x : myExp"""
        strCode = strCode.replace("myExp", f)
        exec(strCode, globals(), ldict)
        fun = ldict['fun']

        strCode = """fun_der = lambda x : myExp"""
        strCode = strCode.replace("myExp", dx)
        exec(strCode, globals(), ldict)
        fun_der = ldict['fun_der']

        filas = []
        columnas = ['','']
        xxx = []

        for xp in range(itr):
            xi = xi - ( fun(xi) / fun_der(xi) )
            filas.append(f"X({xp + 1})")  
            xxx.append([ " ->", xi])

        resultadosFinales = pd.DataFrame(xxx,filas,columnas)
            
        for xp in xplt:         
            res = fun(xp)
            yplt = np.append(yplt , res)

        return v, resultadosFinales, f"Raíz -> {xi:.5f}"

        '''
        plt.plot(xplt, yplt, 'b-')
        plt.plot(xi, 0, 'ro')
        plt.xlabel('X')
        plt.ylabel('Y')
        winTitle = plt.gcf()
        winTitle.canvas.set_window_title("Newton - Raphson")
        plt.grid()
        gridSize = [-(10), (10), -(10), (10)] #Limite de ejes
        plt.axis(gridSize)
        plt.show()
        '''
'''
#f = sy.log(x) - sy.cos(x) #función
myFunc = NewtonRapson("sy.log(x) - sy.cos(x)")
x = myFunc.calculate()#myFunc.calculate( "sy.Pow(x, 3) - 6*(sy.Pow(x, 2)) + 11*x - 6.1 ")

print(x)

'''
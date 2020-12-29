from math import cos
import numpy as np
import matplotlib.pyplot as plt
import math
import sympy as sy


class NewtonRapson:
    def __init__(self):
        None

    def calculate(self, funcion):

        ldict = {}
        sToCode  = "x = sy.symbols('x')\nf = myExp "
        sToCode = sToCode.replace("myExp", funcion)
        exec(sToCode, globals(), ldict)
        f = ldict['f']

        xi = 1
        itr = 6 # numero de iteraciones a realizar 

        xplt = np.linspace(0.00001, 100, 2000) #para funciones con los logs 
        yplt = np.array([], float)

        dx = sy.diff(f)
        dx = dx.doit()
        print(f"f(x) = {f}")
        print(f"f'(x) = {dx}")
        print(f"Xi = {xi}")

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


        for xp in range(itr):
            xi = xi - ( fun(xi) / fun_der(xi) )
            print(f"X({xp + 1}) -> {xi}")
        print(f"Raíz -> {xi:.5f}")
            
        for xp in xplt:         
            res = fun(xp)
            yplt = np.append(yplt , res)


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
  #f = sy.log(x) - sy.cos(x) #función
myFunc = NewtonRapson()
myFunc.calculate("sy.log(x) - sy.cos(x)")
#myFunc.calculate( "sy.Pow(x, 3) - 6*(sy.Pow(x, 2)) + 11*x - 6.1 ")
'''
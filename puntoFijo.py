import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd


class PuntoFijo:
    def __init__(self, ecu, desp1, desp2, a, b, itr=10):
        self.ecu = ecu
        self.ecu_desp = desp1
        self.ecu_desp_2 = desp2
        self.a = a
        self.b = b
        self.itr = itr

    def calculate(self):
        value = self.a
        value_2 = self.b
        itr = self.itr

        self.ecu = self.ecu.replace('^', "**")
        self.ecu_desp = self.ecu_desp.replace('^', "**")
        self.ecu_desp_2 = self.ecu_desp_2.replace('^', "**")

        xplt = np.linspace(-10, 10, 200)
        yplt = np.array([], float)
        yplt_desp = np.array([], float)

        ldict = {}
        sToCode = "fun = lambda x: myExp "
        sToCode = sToCode.replace("myExp", self.ecu)
        exec(sToCode, globals(), ldict)
        fun = ldict['fun']

        sToCode = "fun_desp = lambda x: myExp "
        sToCode = sToCode.replace("myExp", self.ecu_desp)
        exec(sToCode, globals(), ldict)
        fun_desp = ldict['fun_desp']

        sToCode = "fun_desp_2 = lambda x: myExp "
        sToCode = sToCode.replace("myExp", self.ecu_desp_2)
        exec(sToCode, globals(), ldict)
        fun_desp_2 = ldict['fun_desp_2']

        g1 = []
        g2 = []
        d1 = []
        d2 = []

        for xp in xplt:  # evalua
            res = fun(xp)
            yplt = np.append(yplt, res)

        try:
            for i in range(itr):
                value = fun_desp(value)
                g1.append(f"g1(x{i + 1}) = ")
                d1.append(f'{value:.8f}')
        except:
            print("Este no es el despeje correcto")

        try:
            for i in range(itr):
                value_2 = round(fun_desp_2(value_2))
                g2.append(f"g2(x{i + 1}) = ")
                d2.append(f"{value_2}")
        except:
            print("Este no es el despeje correcto")

        resultadosFinales = pd.DataFrame(d1, g1, ['Datos'])
        resultadosFinales2 = pd.DataFrame(d2, g2, ['Datos'])

        plt.plot(xplt, yplt, 'b-')
        plt.plot(value, 0, 'ro')
        plt.plot(value_2, 0, 'ro')
        plt.xlabel('X')
        plt.ylabel('Y')
        winTitle = plt.gcf()
        winTitle.canvas.set_window_title("Punto Fijo")
        plt.grid()
        gridSize = [-(10), (10), -(10), (10)]  # Limite de ejes
        plt.axis(gridSize)
        plt.show()

        return resultadosFinales, resultadosFinales2


'''
func = PuntoFijo(" x^2 - (2)*(x) - 3",
                 " math.sqrt( (2)*(x) + 3 ) ", "3/(x - 2)  ", 0, 5, 15)
#func = PuntoFijo("  x^3 + (4*x^2) - x - 1", " -1 + (4*x^2) + (x^3) ", "6 - (x^3)   ")
f1, f2 = func.calculate()

print(f1)
print(f2)
'''

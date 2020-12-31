# from math import factorial
# import brain
# from sympy import *
# '''    
# Las series de Taylor nos sirven para poder da la expresion de una funcion en terminos de una suma infinita
# Un requisito para poder obtener la serie de una funicón es que pertezca al C^infinito es decir que la pueda
# derivar cuantas veces quiera y podamos encontrar derivada

# Ejemplo f(x) = e^n   

# Es un aproximación de funciones mediante una serie de potencias o suma de potencias enteras de polinomios
# ''' 
# def serie_mcLaurin(funcion):  #CADA QUE SE AGREGUE UN TERMINO UN TERMINO AL POLINOMIO NOS ACECAMOS MÁS A LA FUNCION ORIGINAL

#   sumatoria = 0

# x = symbols('x')

# expresion = cos(x)
# brain.grafica(expresion)
# print(expresion.series(x))

# print(factorial(5))



import numpy as np
import math 
import sympy as sy
from sympy.interactive import printing
printing.init_printing(use_latex=True)
import matplotlib.pyplot as plt
from fractions import Fraction
import pandas as pd


class McTaylor:
    
    def __init__(self, fun, x0):
        fun = fun.replace("ln","sy.ln")
        fun = fun.replace("log","sy.log")
        fun = fun.replace("cos","sy.cos")
        fun = fun.replace("sin","sy.sin")
        fun = fun.replace("tan","sy.tan")
        fun = fun.replace("cot","sy.cot")
        fun = fun.replace("sec","sy.sec")
        fun = fun.replace("csc","sy.csc")
        fun = fun.replace("sinc","sy.sinc")
        fun = fun.replace("acos","sy.acos")
        fun = fun.replace("asin","sy.asin")
        fun = fun.replace("atan","sy.atan")
        fun = fun.replace("acot","sy.acot")
        fun = fun.replace("asec","sy.asec")
        fun = fun.replace("acsc","sy.acsc")
        fun = fun.replace("acsc","sy.acsc")
        fun = fun.replace("x","(x)")
        fun = fun.replace("X","(x)")
        fun = fun.replace("^","**")
        
        fun = fun.replace("π","math.pi")
        fun = fun.replace("e","math.e")
        
        self.f = fun
        self.x0 = x0
        
    def calculate(self):
        
        global x, fx, n, x0
        x, fx, n, x0 = sy.symbols('x fx n x0') 
        #sym = "x, fx, n, x0 = sy.symbols('x fx n x0')"
        #self.f = ( sy.log(x) )
        
        ldict = {}
        sToCode  = "f = myExp "
        sToCode = sToCode.replace("myExp", self.f)
        exec(sToCode, globals(), ldict)
        f = ldict['f']
        fIni = f
        
        #xi = 0 #---------- 
        xi = self.x0
        itr = 7
        res = 0
        listx = np.array([])
        
        res =  (f.subs(x, xi )).evalf() 
        datos = []
        datos.append([f ,'->',res])
        
        
        
        for xp in range(1, itr + 1):
            f = sy.diff(f)
            f = f.doit()
            res =  (f.subs(x, xi )).evalf() 
            datos.append([f,'->',res])
        
            listx = np.append(listx, res)
        
        func =  ( (fx / sy.factorial(n) ) * (x - x0)**2 )
        
        xxx = []
        
        for xp in range( len(listx) ):
          xxx.append(  sy.Rational(float(listx[xp]), math.factorial(xp + 1)) * (x - xi)**(xp + 1) )
        filas = []
        for i in range(1,len(datos)+1):
          filas.append(i)
        
        resultadosFinales = pd.DataFrame(datos,filas,['Derivada',' ','Sustituyendo'])
        
        
        # print(resultadosFinales)
        # display(xxx)
        # print(xxx)
        
        # sumad =  (  xxx[0] + xxx[1] + xxx[2] + xxx[3] + xxx[4] + xxx[5] + xxx[6] )
        # print("-------", sumad)
        
        p1 = ( xxx[0] )
        p2 = ( xxx[0] + xxx[1]) 
        p3 = (  xxx[0] + xxx[1] + xxx[2] ) 
        p4 = (  xxx[0] + xxx[1] + xxx[2] + xxx[3] )
        p5 = (  xxx[0] + xxx[1] + xxx[2] + xxx[3] + xxx[4] ) 
        p6 = (  xxx[0] + xxx[1] + xxx[2] + xxx[3] + xxx[4] + xxx[5] )
        p7 = (  xxx[0] + xxx[1] + xxx[2] + xxx[3] + xxx[4] + xxx[5] + xxx[6] )

        p0 = ( fIni )
        
        p = sy.plot( p0, p1, p2, p3, p4, p5, p6, p7, xlim=[-10,10], ylim=[-5,5], title=fIni)
        
        p[0].line_color = 'red'
        p[1].line_color = 'blue'
        p[2].line_color = 'green'
        p[3].line_color = 'black'
        p[4].line_color = 'yellow'
        p[5].line_color = 'gray'
        p[6].line_color = 'cyan'
        p[7].line_color = 'magenta'
        
        p.show()
        
        return resultadosFinales, xxx

#obj = McTaylor('log(x)', 1)
#obj = McTaylor('sin(x)', 0)
# r1, r2 = obj.calculate()
# print(r1)
# print(r2)

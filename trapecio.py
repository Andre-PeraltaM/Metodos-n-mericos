import brain
import pandas as pd
import numpy as np
import sympy as sy
from matplotlib import style
style.use('ggplot')


class trapecio_1:
    def __init__(self, funcion, a, b, num_iteraciones=9):
        self.funcion = brain.ecuacion(funcion)
        self.a = a
        self.b = b
        self.num_iteraciones = num_iteraciones

    def h(self):
        return (self.b - self.a)/self.num_iteraciones

    def graf(self):
    
        p0 = ( self.funcion )
        p = sy.plot( p0, xlim=[-10,10], ylim=[-5,5], title=self.funcion)
        p[0].line_color = 'red'
        p[1].line_color = 'blue'
        p.show()

    def operacion(self):
        global x, fx, n, x0
        x, fx, n, x0 = sy.symbols('x fx n x0')
    
        resultado = []
        total = 0
    
        h = self.h()
        aaa = []
    
        for i in range(self.num_iteraciones+1):
            sustitucion = f'{self.a + i*h}'
            aaa.append(sustitucion)

            resultado.append(eval(self.funcion.replace('x', sustitucion)))

        for i in range(len(resultado)):
            if i == 0 or i == len(resultado)-1:
                total += resultado[i]
            else:
                total += resultado[i]*2
        total = (h/2)*total
        n = list(range(self.num_iteraciones+1))
        zzz = ['a+n*h = xi', f'f(x) = {self.funcion} ']
        datos = []

        x = f'{self.funcion} = {self.b-self.a}/{self.num_iteraciones}/2*('

        for i in range(self.num_iteraciones+1):
            datos.append([aaa[i], resultado[i]])

            if i == 0:
                x = x+f' {resultado[i]} +'
            elif i == len(resultado)-1:
                x = x+f' {resultado[i]} )'
            else:
                x = x+f' {resultado[i]}*2 + '

        resultadosFinales = pd.DataFrame(datos, n, zzz)
        
        self.graf()

        return resultadosFinales, x, total


# xxxxx = trapecio_1('3*(x)**2 - 10*x + 8',2,3,11)

# print(xxxxx.operacion())

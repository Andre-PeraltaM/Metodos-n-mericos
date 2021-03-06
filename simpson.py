import pandas as pd
import simpson3_8
import brain
import sympy as sy
import math

class simpson_tercio:
    def __init__(self, funcion, a, b, num_iteraciones=9):
        self.funcion = funcion
        self.a = a

        self.b = b
        self.num_iteraciones = num_iteraciones

    def h(self):
        return (self.b - self.a)/self.num_iteraciones

    def operacion(self):
        resultado = []
        total = 0

        h = self.h()
        aaa = []

        for i in range(self.num_iteraciones+1):
            sustitucion = f'{self.a + i*h}'
            aaa.append(sustitucion)
            www = self.funcion.replace('x', sustitucion)

            resultado.append(eval(www))

        for i in range(len(resultado)):
            if i == 0 or i == len(resultado)-1:
                total += resultado[i]
            elif i < 4:
                pass
            else:
                if i % 2 == 0:
                    total += resultado[i]*2

                else:
                    total += resultado[i]*4

        total = (h*1/3)*total
        n = list(range(self.num_iteraciones+1))
        zzz = ['a+n*h = xi', f'f(x) = {self.funcion} ']
        datos = []

        x = f'{self.funcion} = {self.b-self.a}/{self.num_iteraciones}/3*('

        for i in range(self.num_iteraciones+1):
            datos.append([aaa[i], resultado[i]])

            if i == 0:
                x = x+f' {resultado[i]} +'
            elif i < 4:
                pass
            elif i == len(resultado)-1:
                x = x+f' {resultado[i]} )'
            elif i % 2 == 0:
                x = x+f' {resultado[i]}*2 + '
            else:
                x = x+f' {resultado[i]}*4 + '

        resultadosFinales = pd.DataFrame(datos, n, zzz)

        return resultadosFinales, x, total


class Simp:
    def __init__(self, funcion, a, b, num_iteraciones=9,funcion_ori = None):
        self.funcion = funcion
        self.a = a
        self.b = b
        self.num_iteraciones = num_iteraciones
        self.funcion_original = funcion_ori
        
    def graf(self):
        try:

            funcion_o = brain.ecuacion2(self.funcion_original)

            p0 = (funcion_o )
            p = sy.plot( p0, xlim=[-100,100], ylim=[-50,50], title = self.funcion_original)
            p[0].line_color = 'red'
            p[1].line_color = 'blue'
            p.show()            
        except Exception as e:
            pass   


    def solucion(self):
        un_tercio = simpson_tercio(
            self.funcion, self.a, self.b, self.num_iteraciones)
        tres_octavos = simpson3_8.simpson_tresoctavos(self.funcion, self.a, self.b, self.num_iteraciones)

        x = un_tercio.operacion()

        y = tres_octavos.operacion()

        return x, y[1:], (x[2]+y[2])




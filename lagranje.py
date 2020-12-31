import sympy as sy
import lagrange2grafica
import matplotlib.pyplot as plt


class lagran:
    def __init__(self, fila1, fila2):
        fila1 = fila1.replace(' ', '')
        fila2 = fila2.replace(' ', '')
        self.fila1 = fila1.replace(',', ' ')
        self.fila2 = fila2.replace(',', ' ')
        self.x = list(map(str, self.fila1.split(' ')))
        self.y = list(map(str, self.fila2.split(' ')))

    def procedimiento(self):
        '''Regresa dos cosas, la ecuacion antes de ser simplificada y la ecuación ya simplificada'''
        X = sy.symbols('X')

        P = [[['[]'for i in range(
            len(self.x)-1)], '/', ['[]' for i in range(len(self.x)-1)]] for i in range(len(self.x))]
        cont = 0
        for i in P:
            elemento = self.x.pop(cont)
            for j in range(len(self.x)):

                i[0][j] = f'({X}-{self.x[j]})'
                i[2][j] = f'({elemento}-{self.x[j]})'
            self.x.insert(cont, elemento)

            cont += 1
        for i in range(len(P)):
            for j in 0, 2:
                P[i][j] = '*'.join(P[i][j])
                P[i][j] = f'({P[i][j]})'

            P[i].insert(0, f'{self.y[i]}*')
            P[i] = ''.join(P[i])
        P = '+'.join(P)
        ecuacion = sy.simplify(P)

        return P, ecuacion
    def graf(self): 
        plot = lagrange2grafica.Lagrange(self.x, self.y)
        selfx, selfy, xplt, yplt = plot.calculate()

        plt.plot(selfx, selfy, 'ro', xplt, yplt, 'b-')
        plt.xlabel('X')
        plt.ylabel('Y')
        winTitle = plt.gcf()
        winTitle.canvas.set_window_title("LAGRANGE")
        plt.grid()
        plt.show()

        


# x =lagran('1, 3, 5','2, 5, 3')#Ejemplo
# y = x.procedimiento()

# print(y[0])
# print(y[1])

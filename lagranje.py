from sympy import *

class lagran:
    def __init__(self,fila1,fila2):
        self.fila1 = fila1
        self.fila2 = fila2

    def procedimiento(self):
        '''Regresa dos cosas, la ecuacion antes de ser simplificada y la ecuación ya simplificada'''
        X = symbols('X')
        x = list(map(str,self.fila1.split(' ')))
        y = list(map(str,self.fila2.split(' ')))
        P = [ [ ['[]'for i in range(len(x)-1)] , '/' , ['[]' for i in range(len(x)-1)]] for i in range(len(x))]
        cont = 0
        for i in P:
            elemento = x.pop(cont) 
            for j in range(len(x)):
        
                i[0][j] = f'({X}-{x[j]})'
                i[2][j] = f'({elemento}-{x[j]})'
            x.insert(cont,elemento)

            cont += 1
        for i in range(len(P)):
            for j in 0,2:
                P[i][j] = '*'.join(P[i][j])
                P[i][j] = f'({P[i][j]})'

            P[i].insert(0,f'{y[i]}*')
            P[i] = ''.join(P[i])
        P = '+'.join(P) 
        ecuacion = simplify(P)

        return P,ecuacion
'''
x =lagran('1 3 5','2 5 3')#Ejemplo
y = x.procedimiento()

print(y[0])
print(y[1])
'''
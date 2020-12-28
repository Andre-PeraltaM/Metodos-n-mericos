import sympy as sy

class lagran:
    def __init__(self,fila1,fila2):
        fila1 = fila1.replace(' ', '')
        fila2 = fila2.replace(' ', '')
        self.fila1 = fila1.replace(',', ' ')
        self.fila2 = fila2.replace(',', ' ')
       

    def procedimiento(self):
        '''Regresa dos cosas, la ecuacion antes de ser simplificada y la ecuación ya simplificada'''
        X = sy.symbols('X')
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
        ecuacion = sy.simplify(P)

        return P,ecuacion


# x =lagran('1, 3, 5','2, 5, 3')#Ejemplo
# y = x.procedimiento()

# print(y[0])
# print(y[1])

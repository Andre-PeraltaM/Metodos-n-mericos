#importamos 
import math     
import numpy as np
from matplotlib import pyplot as plt

class Biseccion:
    def __init__(self):
        #self.ecu = funcion
        None
        
    def calculate(self, exp):        

        ecu = exp#f(x) = x^4 + 3x^3 − 2
        limInf = -2
        limSup = 3
        itr = 16
            
        ecu = ecu.replace('^', "**")
        #print ( ecu )

        #fun = lambda x: x**3 + x - 1 #expresión
        ldict = {}
        sToCode = """fun = lambda x: myExp #expresión"""
        sToCode = sToCode.replace("myExp", ecu)
        exec(sToCode, globals(), ldict)
        fun = ldict['fun']

        a = limInf #x inferior
        b = limSup #x superior

        x = self.biseccion(fun, a, b , itr)
        #print (f"Raiz -> {x:.4f}")
        raiz = x


        ###PARA GRÁFICA
        #x = np.linspace(-10,10,200)
        sToCodeY = """x = np.linspace(-10,10,200)\ny =  myExp """
        sToCodeY = sToCodeY.replace("myExp", ecu)
        exec(sToCodeY, globals(), ldict)
        y = ldict['y']
        x = np.linspace(-10,10,200)
        winTitle = plt.gcf()
        winTitle.canvas.set_window_title(ecu)
        plt.plot(x, y, "b-", raiz, 0, "ro")
        plt.grid()
        plt.xlabel("X")
        plt.ylabel("Y")
        #plt.title("Funcion: {}, Raíz: {:.5f}". format(ecu, raiz))
        plt.title("Raíz: {:.5f}". format(raiz))
        #gridSize = [-(raiz + 1), (raiz + 1), -(raiz + 1), (raiz + 1)] #Limite de ejes
        gridSize = [-(10), (10), -(10), (10)] #Limite de ejes
        plt.axis(gridSize)
        plt.show()


    def biseccion(self,evalFun,a,b, itr):

        functa = evalFun(a) # evalua en la Función
        functb = evalFun(b) # evalua en la Función
        lastc = 0
        
        if functa * functb > 0 :
            print("No hay raices para esta función entre estos limites ")
            return None

        for i in range(itr): #iter

            c = (a + b) / 2 #aproximación 
            functc = evalFun(c) 
            error = abs((c-lastc)/c)*100

            # if i == 0:
            #     print("iteración {}: {:.5f} \tC: {:.5f} ".format((i + 1), c, functc))

            # if i > 0:
            #     print("iteración {}: {:.5f} \tC: {:.5f}  \t'%'error: {:.4f}% \terror: {:.4f}  ".format((i + 1), c, functc, error, (error/100) ) )
            
            if functc == 0:
                break
            if functa*functc > 0: # revisa si tienen el mismo signo y por lo tanto hace el cambio
                a = c
                functa = functc   
                lastc = c
            if functb*functc > 0: # revisa si tienen el mismo signo y por lo tanto hace el cambio
                b = c
                functb = functc  
                lastc = c
        return c 


#func = Biseccion()
#func.calculate("x^4+3*x^3-2")
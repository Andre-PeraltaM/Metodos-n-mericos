#tutorial "https://www.youtube.com/watch?v=gUdU6BgnJ2c"
import numpy as np
import math
import matplotlib.pyplot as plt
from numpy.core.defchararray import index
#distancia de cada punto a la recta = Ei = mxi +yi

class MinCuadradosGrafica:
    
    def __init__(self):
        None
    
    def process(self, filax, filay):
        

        sigma_x = 0
        sigma_y = 0
        sigma_x2 = np.array([])
        sigma_y2 = np.array([])
        sigma_xy = 0
        beta2 = np.array([])
        sigma_beta2 = np.array([])
        m = 0 #pendiente
        n = 0 #numero de elementos en las listas
        b = 0 #punto de corte con el eje y
        r = 0 #coeficiente de relación lineal Entre más cercano a 1 mayor leración lineal tiene
        e = 0 #error en la pendiente
        eCorte = 0 #error en el punto de corte
        
        sorted_x = np.array([])
        plty = np.array([])
        
        x = np.array(filax, float)
        y = np.array(filay, float)
        
        # x = np.array([1, 1.5, 2.5, 3, 3.5, 4.5, 5.5, 6, 6.5, 8], float)
        # y = np.array([2, 3, 3, 4, 3.5, 4, 4.5, 5, 5.5, 6], float)
        
        #x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], float)
        #y = np.array([220, 230, 220, 240, 250, 250, 300, 300, 250, 300, 275, 200], float)
        
        sigma_x = np.sum(x)
        sigma_y = np.sum(y)
        sigma_xy = np.sum( np.multiply(x,y) )
        sigma_x2 = np.sum( np.append(sigma_x2, i**2) for i in x )
        sigma_y2 = np.sum( np.append(sigma_y2, i**2) for i in y )
        
        n = ( np.size(x) )
        m = ( n*sigma_xy - sigma_x*sigma_y ) / (n*sigma_x2 - sigma_x**2)
        b = (sigma_y*sigma_x2 - sigma_x*sigma_xy) / ( n*sigma_x2 - sigma_x**2)
        r = ( (n * sigma_xy) - (sigma_x * sigma_y) ) / ( (math.sqrt((n*sigma_x2)-(sigma_x**2))) * (math.sqrt((n*sigma_y2)-(sigma_y**2))) )
        
        for px , py in zip(x, y):
            res = (b + m*(px) - (py) )**2
            beta2 = np.append(beta2, res)
        
        sigma_beta2 = np.sum(beta2) 
        e = math.sqrt( (n/ (n*sigma_x2 - sigma_x**2) ) * (sigma_beta2 / (n-2 ) ) )
        eCorte = math.sqrt( (sigma_x2/ (n*sigma_x2 - sigma_x**2) ) * (sigma_beta2 / (n-2 ) ) )
        
        def getY(givenX):
            res_y = (m)*(givenX) + b
            return res_y
        
        sorted_x = np.sort(x) #acomoda las listas por tamaño para que podamos hayar un mínimo y un máximo
        plty = np.append( plty, [getY(px) for px in sorted_x] )
        
        # print(f"N -> {n}")
        # print(f"Sx -> {sigma_x}")
        # print(f"Sy -> {sigma_y}")
        # print(f"Sxx -> {sigma_x2[0]}")
        # print(f"Syy -> {sigma_y2[0]}")
        # print(f"m -> {m[0]}")
        # print(f"r -> {r}")
        # print(f"β^2 -> {sigma_beta2}")
        # print(f"Error en la pendiente -> {e}")
        # print(f"Error en el punto de corte -> {eCorte}")
        # print(f"Ecuación final-> y = ({m[0]:.3f} ± {e:.3f})x + ({b[0]:.3f} ± {eCorte:.3f})")
        
        
        # print("\n       | i\t| X\t| Y\t| x*y\t| x^2\t| y^2\t| (b+mx-y)^2   \t| \'Y\' En la recta ")
        # print("-----------------------------------------------------------------------------------------------------------------------------")
        # for i in range(len(x)):
        #     print(f"       | {i + 1}\t| {x[i]}\t| {y[i]}  \t| {x[i]*y[i]:.2f}\t| {x[i]**2:.2f}\t| {y[i]**2:.2f}\t| {(b + m*(x[i]) - (y[i]) )**2} \t| {plty[i]:.3f}" )
        
        # print("-----------------------------------------------------------------------------------------------------------------------------")
        
        # print(f"   Σ = | {n} \t| {sigma_x} \t| {sigma_y}\t| {sigma_xy} \t| {sigma_x2[0]} \t| {sigma_y2[0]}\t| β^2={sigma_beta2}")
        
        
        plt.plot(x, y, 'bo')
        plt.plot(sorted_x, plty, 'r-', sorted_x, plty, 'mo')
        plt.xlabel('X')
        plt.ylabel('Y')
        winTitle = plt.gcf()
        winTitle.canvas.set_window_title("Mínimo Cuadrado")
        plt.grid()
        plt.show()


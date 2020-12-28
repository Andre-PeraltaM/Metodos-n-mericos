
import numpy as np
import matplotlib.pyplot as plt


class Lagrange:
    def __init__(self, listx, listy):
        self.x = listx
        self.y = listy
    
    def calculate(self):

        #x = np.array([-4, -3, -2, -1], float)
        #y = np.array([0, -4, -6, -6], float)

        self.x = np.array(self.x, float)
        self.y = np.array(self.y, float)

        xplt = np.linspace(self.x[0], self.x[-1]) 
        yplt = np.array([], float)

        for xp in xplt:
            yp = 0 # = sum 

            for xi, yi in zip(self.x, self.y):
                yp += yi *  np.prod( (xp - self.x[self.x != xi]) / (xi - self.x[self.x != xi]) )
            
            yplt = np.append(yplt,yp)


        #ploting
        plt.plot(self.x, self.y, 'ro', xplt, yplt, 'b-')
        plt.xlabel('X')
        plt.ylabel('Y')
        winTitle = plt.gcf()
        winTitle.canvas.set_window_title("LAGRANGE")
        plt.grid()
        plt.show()

myLagrange = Lagrange([1, 3, 5], [2, 5, 3])
myLagrange.calculate()
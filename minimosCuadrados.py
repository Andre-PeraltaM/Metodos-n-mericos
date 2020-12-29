import math
import pandas as pd
from pylab import *
import brain as br

class miniCuadrados:
	def __init__(self):
        
		None

	def procedimiento(self,filax,filay):
		filax = filax.replace(' ', '')
		filay = filay.replace(' ', '')
		filax = filax.replace(',', ' ')
		filay = filay.replace(',', ' ')
        
		filax = filax.split(' ')
		filay = filay.split(' ')

		filax = list(map(float,filax))
		filay = list(map(float,filay))
		xy = []
		y2 = []
		x2 = []

		for i in range(len(filax)):
			xy.append(filax[i]*filay[i])
			y2.append(filay[i]**2)
			x2.append(filax[i]**2)

		Sx = sum(filax)
		Sy = sum(filay)
		Sxy =sum(xy)
		Sy2 =sum(y2)
		Sx2 =sum(x2)
		N = len(filax)

		m = (N*Sxy-Sx*Sy)/(N*Sx2-Sx*Sx)
		b = (Sy*Sx2-Sx*Sxy)/(N*Sx2-Sx*Sx)
		r = (N*Sxy-Sx*Sy)/(math.sqrt(N*Sx2-Sx*Sx)*math.sqrt(N*Sx2-Sy-Sy))
		B2 = []
		for i in range(len(filax)):
			B2.append((b+m*filax[i]-filay[i])**2)
		
		B2 = B2 + [sum(B2)]
		filaxf = filax + [Sx]
		filayf = filay + [Sy] 
		xy = xy + [Sxy] 
		y2 = y2 + [Sy2]
		x2 = x2 + [Sx2] 


		y_graf = []

		for i in filax:
			y_graf.append(m*i+b)
		y_graf.append('')


		datos = filaxf , filayf , xy ,  x2 , y2 , B2 , y_graf


		datosReal = []

		for j in range(len(filaxf)):
			datosReal.append([])
			for i in range(len(datos)):
				datosReal[-1].append(datos[i][j])

		columnas = ["X","Y",'x*y','x^2','y^2','(b+mx-y)^2', 'y en la grafica']
		filas =  list(range(1,len(filaxf))) + [f'N = {len(filaxf)-1}']

		tablaFinal = pd.DataFrame(datosReal,filas,columnas)

		año_2021 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
		w_graf = []
		for i in año_2021:
			w_graf.append(m*i+b)



		figura = plt.figure()  #creamos la figura
		grafico = figura.add_axes([0.1,0.1,0.8,0.8]) #Le damos tamaño a la ventana
		grafico.plot(año_2021,w_graf, 'o-')#Primera función
		grafico.plot(filax,filay, 'o')#Segunda

		show()

		return 	f'm = {m} b = {b} r = {r}' , tablaFinal , f'y = {m}*x+{b}'

# x = miniCuadrados()
# y = x.procedimiento('1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12','220, 230, 220, 240, 250, 250, 300, 300, 250, 300, 275, 200')

# print(y[0])
# print(y[1])

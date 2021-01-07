import pandas as pd
import simpson1_3
import brain
import math
import sympy as sy

class simpson_tresoctavos:

	def __init__(self,funcion,a,b,num_iteraciones = 9,funcion_ori = None):
		self.funcion = funcion
		self.a = a
		self.b = b
		self.num_iteraciones = num_iteraciones
		self.funcion_original = funcion_ori
	def h(self):
		return (self.b - self.a)/self.num_iteraciones
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
	       

            
	def operacion(self):
		resultado = []
		total = 0

		h = self.h()
		aaa = []

		for i in range(self.num_iteraciones+1):
			sustitucion = f'{self.a + i*h}'
			aaa.append(sustitucion)

			resultado.append(eval(self.funcion.replace('x',sustitucion)))

		for i in range(len(resultado)):
			if  i == 0 or i == 3:
				total += resultado[i]
			elif i > 3:
				break
			else:
				total += resultado[i]*3



		total = (h*3/8)*total

		x = f'{self.funcion_original} = {self.b-self.a}/{self.num_iteraciones}/3*('

		for i in range(self.num_iteraciones+1):

			if i == 0 :
				x = x+f' {resultado[i]} +'
			elif i == 3:
				x = x+f' {resultado[i]} )'
			elif i > 3 :
				break
			else:
				x = x+f' {resultado[i]}*3 + '
		n_tercio = simpson1_3.simpson_tercio(self.funcion,self.a,self.b,self.num_iteraciones)
		y = n_tercio.operacion()




		return y[0],x , total
	
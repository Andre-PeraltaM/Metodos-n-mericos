import pandas as pd
import simpson1_3

class simpson_tresoctavos:

	def __init__(self,funcion,a,b,num_iteraciones = 9):
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

			resultado.append(eval(self.funcion.replace('x',sustitucion)))

		for i in range(len(resultado)):
			if  i == 0 or i == 3:
				total += resultado[i]
			elif i > 3:
				break
			else:
				total += resultado[i]*3



		total = (h*3/8)*total

		x = f'{self.funcion} = {self.b-self.a}/{self.num_iteraciones}/3*('

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
	
'''
xxxxx = simpson_tresoctavos('3*(x)**2 - 10*x + 8',2,3,11)

print(xxxxx.operacion())
'''
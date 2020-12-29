import pandas as pd
class simpson_tercio:
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
			if  i == 0 or i == len(resultado)-1:
				total += resultado[i]

			else:
				if i %2 == 0:
					total += resultado[i]*2
					
				else:
					total += resultado[i]*4


		total = (h*1/3)*total
		n = list(range(self.num_iteraciones+1))
		zzz = ['a+n*h = xi', f'f(x) = {self.funcion} ']
		datos = []

		x = f'{self.funcion} = {self.b-self.a}/{self.num_iteraciones}/3*('

		for i in range(self.num_iteraciones+1):
			datos.append([aaa[i],resultado[i]])

			if i == 0 :
				x = x+f' {resultado[i]} +'

			elif i == len(resultado)-1:
				x = x+f' {resultado[i]} )'
			elif i %2 == 0:
				x = x+f' {resultado[i]}*2 + ' 
			else:
				x = x+f' {resultado[i]}*4 + '


		resultadosFinales = pd.DataFrame(datos,n,zzz) 


		return resultadosFinales, x , total

'''
xxxxx = simpson_tercio('1/(1+x)',0,1,6)

print(xxxxx.operacion())
'''
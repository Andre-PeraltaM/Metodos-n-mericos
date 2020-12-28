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
			elif i < 4:
				pass
			else:
				if i %2 == 0:
					total += resultado[i]*4
					
				else:
					total += resultado[i]*2


		total = (h*1/3)*total
		n = list(range(self.num_iteraciones+1))
		zzz = ['a+n*h = xi', f'f(x) = {self.funcion} ']
		datos = []

		x = f'{self.funcion} = {self.b-self.a}/{self.num_iteraciones}/3*('

		for i in range(self.num_iteraciones+1):
			datos.append([aaa[i],resultado[i]])

			if i == 0 :
				x = x+f' {resultado[i]} +'
			elif i < 4 :
				pass
			elif i == len(resultado)-1:
				x = x+f' {resultado[i]} )'
			elif i %2 == 0:
				x = x+f' {resultado[i]}*4 + ' 
			else:
				x = x+f' {resultado[i]}*2 + '


		resultadosFinales = pd.DataFrame(datos,n,zzz) 


		return resultadosFinales, x , total

xxxxx = simpson_tercio('3*(x)**2 - 10*x + 8',2,3,11)

print(xxxxx.operacion())

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





		return x , total
print('')
xxxxx = simpson_tresoctavos('3*(x)**2 - 10*x + 8',2,3,11)

print(xxxxx.operacion())
import brain
import pandas as pd
""" Modulo de HyperBrain para resolver operaciones por metodo de bolzano"""

class Biseccion:
	def __init__(self,funtion):
		self.funcion = funtion#este será un encabezado de columna
	def bolzano(self,a,b):
		'''
		Ecuación del teorema de Bolzano
		Resive dos valores y devuelve el resultado
		'''
		return (a+b)/2

	def error(self,a,b):
		'''
		Calcula el error de Bolzano
		Resive dos valores y devuelve un valor 
		'''
		return abs((a-b)/b)

	def cambioSigno(self,tablaTabulacion):
		'''
		Resive un dataframe para buscar un cambio de signo en la tabulacion de Y
		regresa la posición del cambio de signo
		'''
		signo = '+' if tablaTabulacion['Y'][0] >= 0 else '-'
		signoVar = ''
		cambioS = [[],[]]
		for i in range(len(tablaTabulacion['Y'])):
			signoVar = '+' if tablaTabulacion['Y'][i] >= 0 else '-'
			if signo != signoVar:
				cambioS[0].append(tablaTabulacion['X'][i-1])
				cambioS[0].append(signoVar)
				cambioS[1].append(tablaTabulacion['X'][i])
				cambioS[1].append(signoVar)
				break
		if cambioS[1][1] == '-' :
			cambioS[0][1] = '+'
		else:
			cambioS[0][1] = '-'	
		return cambioS
			

	def solucion(self):

		funcionConstruida = brain.ecuacion(self.funcion)

		listaY = brain.tabulacion(funcionConstruida)

		filas =  ["X",'Y']
		columnas = [">",">",">",">",">",">",">"]

		datos = [[-3],[-2],[-1],[0],[1],[2],[3]]

		for i in range(len(listaY)):
			datos[i].append(listaY[i])

		tablaTabulacion = pd.DataFrame(datos,columnas,filas) #La primera tabla 
		x = self.cambioSigno(tablaTabulacion)
		for i in range(2):
			x[i].append(brain.sustitucion(funcionConstruida,value = str(x[i][0])))
		
		ValorAnterior = x[0][0]
		Valoractual = x[1][0]
		UltimoPositivo = x[1][0]
		for i in range(1,20):
			if x[i][1] == '+':
				ValorAnteriorTemp = Valoractual
				Valoractual = self.bolzano(Valoractual,ValorAnterior)
				ValorAnterior = ValorAnteriorTemp
				x.append([Valoractual])
			else:
				ValorAnteriorTemp = Valoractual
				Valoractual = self.bolzano(Valoractual,UltimoPositivo)
				ValorAnterior = ValorAnteriorTemp
				x.append([Valoractual])

			sustitucionActual = brain.sustitucion(funcionConstruida,value = str(x[-1][-1]) )

			if sustitucionActual >= 0 :
				x[-1].append('+')
			else:
				x[-1].append('-')
			x[-1].append(sustitucionActual)

			if x[-1][1] == '+':
				UltimoPositivo = x[-1][0]
			if len(x)  == 18:
				break
		f = self.funcion
		self.funcion = f'     f(x) = {self.funcion}'
		filas =  ["Bolzano  ",'  Signo',self.funcion]
		columnas = ['a','b',"1","2","3","4","5","6","7",'8','9','10','11','12','13','14','15','16']

		resultadosFinales = pd.DataFrame(x,columnas,filas) #La Segunda tabla
		resultadoError = []
		for i in range(3,len(resultadosFinales['Bolzano  '])):
			resultadoError.append(self.error(resultadosFinales['Bolzano  '][i-1],resultadosFinales['Bolzano  '][i]))

		resultadosFinales['  Error  '] = ['-','-','-'] + resultadoError
		#brain.grafica(f)
		return tablaTabulacion,resultadosFinales
'''
x = Biseccion('x^4+3x^3-2')#Ejemplo
y =x.solucion()

print(y[0])
print(y[1])
'''

import math
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl

''' El cerebro de toda la libreria'''
def prueba(x):
	x = str(x)
	apertura = ['(','[','{']
	cierre = [')',']','}']

	lista ={')':'(',']':'[','}':'{'}

	orden = []

	for i in x:
		if i in apertura:
			orden.append(i)
			print('s')
		elif i in cierre:
			print('a')
			if orden[-1] == lista[i]:
				orden.pop()
			else:
				return False
	if len(orden) == 0:

		return True
	else:

		return False

def comprobar(funcion):

	x = prueba(funcion)

	if x == False:
		return False
	else:
		return True





def sic(x):
	return 1/math.cos(x)

def csc(x):
	return 1/math.sin(x)

def cot(x):
	return 1/math.tan(x)



def grafica(function):
	'''
	Tabula y grafica una función  
	'''
	
	x = np.linspace(-10,3,100)

	x_str = list(map(str,np.linspace(-10,3,100)))
	y = []
	for i in x_str:
		y.append(sustitucion(function,i))

	figura = plt.figure(figsize=(7,7),edgecolor = 'black') 
	grafico = figura.add_axes([0.1,0.1,0.9,0.9])
	grafico.plot(x,y ,'red',label = f"f(x)={function}")
	grafico.legend(loc = 0)

	plt.title(f" f(x) = :  {function} ") 
	ax = pl.gca()  # gca stands for 'get current axis'
	ax.spines['right'].set_color('none')
	ax.spines['top'].set_color('none')
	ax.xaxis.set_ticks_position('bottom')
	ax.spines['bottom'].set_position(('data',0))
	ax.yaxis.set_ticks_position('left')
	ax.spines['left'].set_position(('data',0))

	plt.xlabel("Eje X")

	plt.ylabel("Eje Y")
	plt.show()
	

def __parentesis(function,caracter):
	#ESTE METODO DEBE SER PRIVADO
	if caracter == '(':
		sustitucion = '*('
		contra = ')'
		x = -1
		y = 0
	if caracter == ')':
		sustitucion = ')*'
		contra = '('
		x = +1
		y = 1

	if caracter in function:
		lugar_caracter = function.find(caracter)+1
		numero_repeticiones = function.count(caracter)
		s = 0
		for i in range(numero_repeticiones):
			cacho_cadena = function[s:lugar_caracter + y]
			posicion = cacho_cadena.find(caracter)
			try:
				if cacho_cadena[posicion+ x].isdecimal() or cacho_cadena[posicion+ x] == contra:
					cacho_cadena = cacho_cadena.replace(caracter,sustitucion)
			except IndexError:
				break
			function = function.replace(function[s:lugar_caracter+y],cacho_cadena)
			s = lugar_caracter+1
			lugar_caracter = function[s:].find(caracter)+1+s

	return function

def ecuacion(function):
	'''
	Sustituye los valores de una ecuacion en su forma str para hacerla valida por el metodo eval()
	Resive un valor Str y devuelve un valor str equivalente que puede ser introducido en eval()
	Si la función está mal entonces se devuelve 'error'
	'''
	

	tabla_de_valores = { 88: '(x)', 120: '(x)', 94: '**'}
	function = function.translate(tabla_de_valores)
	#Las anteriores 3 lineas son para sustituir X, x y ^
	diccionario_otras_variables = {'sec':'(sic','csc':'(csc','cot':'(cot','sen':'(math.sin','cos':'(math.cos','tan':'(math.tan','senh':'(math.sinh','cosh':'(math.cosh','tanh':'(math.tanh','sin^-1': '(math.asin', 'cos^-1' : '(math.acos' , 'tan^-1' : '(math.atan','π':'(math.pi)','sqrt':'(math.sqrt','√':'(math.sqrt','Ln':'PROCESO','PROCESO':'(math.log10','PROCESO':'(math.log','PROCESO':'(math.acos','PROCESO':'(math.asin','PROCESO':'(math.atan','e':'(math.e)'}

	#math.log(x, base)
	for i in diccionario_otras_variables:
		if i in function:
			for j in range(function.count(i)):
				z = function[function.find(i)+len(i)+1:]
				function = function[:function.find(i)+len(i)+1+z.find(')')] + '))' + function [function.find(i)+len(i)+1+z.find(')')+1:] 
				function = function.replace(i,diccionario_otras_variables[i],1)


	function = __parentesis(function,'(')#Hace que los parentesis multipliquen
	function = __parentesis(function,')')
	
	#Valor absoluto
	return function
def sustitucion(function, value = '1'):
	'''
	Sustituye los valores de X en una ecuación por el valor dado
	Si no se da un valor se evalua en 1 
	'''
	function = ecuacion(function)
	function = function.replace('x',value)
	try:
		return eval(function)
	except ZeroDivisionError:
		return None
	except ValueError:
		return None


def tabulacion(function,value1 = -3,value2 = 3):
	'''
	Tabula una función tipo eval() en un rango de valores.
	Recibe una función str y dos valores que son los limites, para devolver una lista con los resultados
	'''
	valuesX = list(map(str,range(value1,value2+1)))

	rango_valoresY = []

	for i in valuesX:
		rango_valoresY.append(sustitucion(function,i)) 

	return rango_valoresY

def hay(un_objeto , en_este_argumento , y_este_aparece_solo = 1):
	'''
	Usando un if se lee de la siguiente manera:

	Si hay un objeto (x) en un argumento (y) , devuelve true si este elemento está presente éste numero de veces (z)

	Funcion que retorna True si un objeto está presente en un argumento (listas,tuplas,str etc.)
	Si le aplica el tercer argumento entonces se le puede pedir que nos diga si está presente el número de veces que queremos
	Si como tercer argumento se le pone un 0 entonces estamos diciendo que nos diga si no está


	'''
	cont = 0
	for i in en_este_argumento:
		if un_objeto == i:
			cont += 1

	if y_este_aparece_solo == cont:
		return True
	else:
		return False


#AQUI EMPEZAMOS CON LA CALCULADORA





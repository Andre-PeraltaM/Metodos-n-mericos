from math import factorial
import brain
from sympy import *
'''    
Las series de Taylor nos sirven para poder da la expresion de una funcion en terminos de una suma infinita
Un requisito para poder obtener la serie de una funicón es que pertezca al C^infinito es decir que la pueda
derivar cuantas veces quiera y podamos encontrar derivada

Ejemplo f(x) = e^n   

Es un aproximación de funciones mediante una serie de potencias o suma de potencias enteras de polinomios
''' 
def serie_mcLaurin(funcion):  #CADA QUE SE AGREGUE UN TERMINO UN TERMINO AL POLINOMIO NOS ACECAMOS MÁS A LA FUNCION ORIGINAL

	sumatoria = 0

x = symbols('x')

expresion = cos(x)
brain.grafica(expresion)
print(expresion.series(x))

print(factorial(5))
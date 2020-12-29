import simpson1_3
import simpson3_8

class simp:
	def __init__(self,funcion,a,b,num_iteraciones = 9):
		self.funcion = funcion
		self.a = a
		self.b = b
		self.num_iteraciones = num_iteraciones
	def solucion(self):
		un_tercio = simpson1_3.simpson_tercio(self.funcion,self.a,self.b,self.num_iteraciones)
		tres_octavos = simpson3_8.simpson_tresoctavos(self.funcion,self.a,self.b,self.num_iteraciones)

		x = un_tercio.operacion() 

		y = tres_octavos.operacion()


		return x,y[1:],(x[2]+y[2])	
'''
xxxxx = simp('3*(x)**2 - 10*x + 8',2,3,11)

print(xxxxx.solucion())
'''
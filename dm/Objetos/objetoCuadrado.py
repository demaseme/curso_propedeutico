class Cuadrado:
	p=0
	def __init__(self) :
		self.p = [0.0,0.0]
	def imprime(self) :
		print Cuadrado.p, self.p

c1 = Cuadrado()
c2 = Cuadrado()

c1.p[0] = 12
c2.p[1] = 24

c1.imprime()
c2.imprime()

Cuadrado.p = 221
c1.imprime()
c2.imprime()

class Rectangulo :
	def __init__(self,x1,y1,x2,y2,data):
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.y2 = y2
		self.data = data

	def imprimeValores(self) :
		print x1,y1,x2,y2

	def compara(self,other) :
		print self.data,self.x1,self.y1,self.x2,self.y2
		print other.data,other.x1,other.y1,other.x2,other.y2


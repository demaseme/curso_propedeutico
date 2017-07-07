class punto2D:
	def __init__(self,x,y) :
		self.x = x
		self.y = y
	def __add__(self,other) :
		return (punto2D (self.x + other.x, self.y + other.y) )
	def myprint(self):
		print self.x,self.y

p1 = punto2D(1.0,0.0)
print type(p1)
p1.myprint()

p2 = punto2D(5.0,4.0)
p2.myprint()

p3 = p1 + p2
print type(p3)
p3.myprint()


#encoding: utf-8
import math
class Circulo:
	def __init__(self,x1,y1,r):
		self.x1 = x1
		self.y1 = y1 
		self.r = r
	def imprime(self) :
		print x1,y1,r
	def compara(self,other):
		#aquì se va a comparar si hay o no colisión
		d = math.sqrt( pow( (other.x1 - self.x1) ,2) + pow( (other.y1 - self.y1), 2 ))
		rs = self.r + other.r
		if d <= rs :
			return 0
		return 1	

class Cuadrado:
	pass

def procesa(pd,vx,vy):
	pd.x = vx
	pd.y = vy

def imprime(pd):
	print pd.x,pd.y


Datos = Cuadrado()
#imprime(Datos)

Datos.x = 40
Datos.y = 20

imprime(Datos)
procesa(Datos,1,2)
imprime(Datos)

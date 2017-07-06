#coding: utf-8
#1 Necesitamos valores de a,b y c
#2 introducir estos valores por linea de comandos
#3 Discriminante d = b*b - 4*a*c
# Caso 1 : d > 0, las raices son reales y diferentes.
# Caso 2 : abs(d) < 1e-9, las raices son reales e iguales.
# Caso 3 : d < 0, las raices son complejas.
#4 
# Caso 1
# x1 = (-b - sqrt(d))/(2a)
# x2 = (-b + sqrt(d))/(2a)
# Caso 2
# x1 = x2 = -b/(2a)
# Caso 3
# Re(x1) = -b/2a
# Im(x1) = -sqrt(-d)/2a
# Re(x2) = Re(x1)
# Im(x2) = -Im(x1)
#*Salida: Imprimimos que caso se trata y los valores de las raices.

import sys
import math
if len(sys.argv) != 4:
	print "Args a b c"
	sys.exit(1)
try:
	a = float(sys.argv[1])
except ValueError:
	print "El primer argumento no es un número."
	sys.exit(2)
try:
	b = float(sys.argv[2])
except ValueError:
	print "El segundo argumento no es un número."
	sys.exit(2)
try: 
	c = float(sys.argv[3])
except ValueError:
	print "El tercer argumento no es un número."
	sys.exit(2)
d = b*b - (4*a*c)
#print "Determinante : ",d
if d > 0:
	print "Las raices son reales y diferentes."
	x1 = (-b + math.sqrt(d))/(2*a)
	x2 = (-b - math.sqrt(d))/(2*a)
	print x1,x2
elif math.fabs(d) < 1e-09:
	print "Las raices son reales e iguales."
	x1 = x2 = -b/(2*a)
	print x1
else:
	print "Las raices son complejas"
	rx1 = -b/(2*a)
	ix1 = -math.sqrt(-d)/(2*a)
	print rx1, "j", ix1
	print rx1, "j",-ix1

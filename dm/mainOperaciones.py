#coding: utf-8

import operaciones
import sys

n = len(sys.argv)
if n != 3 : 
	print "Args: numero1 numero2"
	sys.exit(1)

try: 
	n1 = float ( sys.argv[1] )
except ValueError:
	print "El primer argumento no es un número"
	sys.exit(2)

try: 
	n2 = float ( sys.argv[2] )
except ValueError:
	print "El segundo argumento no es un número"
	sys.exit(2)

r1 = operaciones.suma (n1,n2)
r2 = operaciones.resta(n1,n2)
r3 = operaciones.multiplicacion(n1,n2)

print r1,r2,r3

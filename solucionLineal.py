#coding: utf-8

import sys

#Los valores de m y b por la línea de comandos
if len( sys.argv ) != 3: 
	print "Args: m b"
	sys.exit(1)

try:
	m = float(sys.argv[1])
except ValueError:
	print "El argumento 1 no es un número."
	sys.exit(2)

try:
	b = float(sys.argv[2])
except ValueError:
	print "El argumento 2 no es un número."
	sys.exit(2)

try:
	x = (-b/m)
	print x 
except ZeroDivisionError:
	print "El argumento 1 no debe ser 0."
	sys.exit(3)


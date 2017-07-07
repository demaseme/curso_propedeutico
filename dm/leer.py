#coding utf-8
import sys

n = len(sys.argv)
if n != 2 :
	print "Args: nombre_archivo"
	sys.exit(1)

nombre = sys.argv[1]
try:
	arch = open( nombre, 'r' )
except IOError:
	print "No pude abrir el archivo", nombre
	sys.exit(2)

for linea in arch: 
	print linea,
arch.close()

#encoding: utf-8

#Patron 1, la n especifica la altura del triángulo. Debe ser mayor o igual a 6

import sys
if len(sys.argv) != 2 :
	print 'Args: número'
	sys.exit(2)
n = int(sys.argv[1])
if n < 6 :
	print 'El primer argumento debe ser mayor o igual a 6'
	sys.exit(1)
i = 0
j = n
c = n*4
espacios = 0 
while i <= n :
	while espacios > 0 :
		print '',
		espacios -= 1
	while c > 0:
		print '*',
		c-=1
	i+= 1	
	espacios = i*4
	c = (n - i) * 4
	if c == 0 :
		c = 2
		espacios = espacios - 2
	print

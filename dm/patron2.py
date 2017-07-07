#encoding: utf-8

#Patron 1, la n especifica la altura del romboide. Debe ser mayor o igual a 5

import sys
if len(sys.argv) != 2 :
	print 'Args: número'
	sys.exit(2)
n = int(sys.argv[1])
if n < 5 :
	print 'El primer argumento debe ser mayor o igual a 5'
	sys.exit(1)
i = 0
j = 0
c = n
espacios = 0 #espacios despues del primer asterisco
while i < n :
	j = 0
	while c > 0:
		print '',
		c-=1
		j+=1 #contador de espacios en blanco insertados
	print '*',
	i+=1
	c = n - i
	#insertamos espacios y otro asterisco
	espacios = n - j
	if espacios > 0 :	
		while espacios -1 > 0 :
			print ' ',
			espacios -= 1
		print '*',
	print
c = 2
i = 0
while i < n - 1 :
	j = 0 
	while c > 0 :
		print '',
		c-=1
		j+=1 
	print '*',
	i+=1
	c += i + 2 
	espacios = n - j
	if espacios > 0 :
		while espacios - 1 > 0 :
			print ' ',
			espacios -= 1
		print '*',
	print

		

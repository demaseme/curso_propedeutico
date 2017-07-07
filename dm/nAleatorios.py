#encoding: utf-8

import random
import sys

if len(sys.argv) != 2 :
	print 'Args: número'
	sys.exit(1)
veces = int(float(sys.argv[1]))

media = 100
sigma = 20
indice0 = media - 3*sigma
indice1 = media + 3*sigma

print "# ", indice0, indice1

amplitud = indice1-indice0 + 1

varreglo = [0]*amplitud

i=0
while i < veces:
	n = random.gauss(media,sigma)
	v = int(n+0.5) - indice0
	if v >= 0 and v<amplitud : 
		varreglo[v] += 1
	i += 1
i = 0
while i<amplitud : 
	v = i + indice0
	norma = float(varreglo[i])/veces
	#print v, varreglo[i]
	print v, norma
	i+=1


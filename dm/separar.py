#coding: utf-8

a = "Esta es una prueba de una línea de texto"
b = a.split()

for palabra in b: 
	print palabra,

c = b[3]
print "Otro: ", c

n = len(b)
i = 0 
while i < n :
	print b[i]
	i = i + 1


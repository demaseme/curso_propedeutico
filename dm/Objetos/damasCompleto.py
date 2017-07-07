#encoding: utf-8
#Para representar los tableros posibles se usan las permutaciones.


#El tablero es un arreglo de numeros de 1 ... n
def permutaciones(tablero) :
	if len(tablero) == 0 :
		return [[]]
	return sum([insertaMultiple(tablero[0],s) for s in permutaciones(tablero[1:])],[])

#Para hacer las permutaciones necesitamos un metodo para insertar x en una lista en la posicion i
def inserta(x,lista,i) :
	res = lista[:i] + [x] + lista[i:]
	return res
#También necesitamos un metodo para insertar x en una lista
#en todas las posiciones posibles de la lista.
def insertaMultiple(x,lista) :
	return [ inserta(x,lista,i) for i in range(len(lista) + 1) ]
		
	
#ya podemos representar tableros de tamaño n y obtener sus diferentes jugadas posibles.
#ahora es necesario saber cuando hay jaque horizontal y en diagonal.

#para saber si hay jaque horizontal es necesario comparar si hay dos numeros iguales en el tablero
def hay_jaque_horizontal(tablero) :
	i = j = 0 
	while i < len(tablero):
		j = i + 1
		while j < len(tablero) :
			if tablero[i] == tablero[j] :
				return 1
			j += 1
		i += 1
	return 0 

#para saber si hay jaque diagonal es necesario comparar 
#si la distancia entre dos numeros es igual a la resta de ellos
def hay_jaque_diagonal(tablero) :
	i = j = 0 
	while i < len(tablero):
		j = i + 1
		dama1 = tablero[i]
		while j < len(tablero) :
			dama2 = tablero [j] 
			d = j - i
			p = dama2 - dama1
			if p < 0 :
				p = p*-1
			if p == d :
				return 1
			j += 1
		i += 1
	return 0

#para imprimir el tablero rotado 90°
def imprime(tablero) :
	i = 0 
	n = len(tablero) 
	while i < n :
		dama1 = tablero[i] - 1
		j = 0
		while j < n :
			if j == dama1 :
				print "* ",
			else:
				print "- ",
			j += 1
		print	
		i += 1
def main():
	sol = 0
	#Establecemos el tablero.
	tablero = [1,2,3,4]
	#Establecemos sus combinaciones.
	combinaciones = permutaciones(tablero) 
	#Para cada combinación probamos si resuelve el problema
	for c in combinaciones:
		if not hay_jaque_horizontal(c):
			if not hay_jaque_diagonal(c):
				sol += 1
				print 'Solución #',sol
				imprime(c)
main()
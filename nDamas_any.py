#encoding: utf-8
import copy
import permutaciones
#Given n, returns a list of all the permutations 
#of the list from 1..n, example:
#permutatiosnR(2) returns [[1 2] [2 1] [1 1] [2 2]]
def permutationsR(n) :
	i = 2 #ya son pares...
	#generar la lista [1...n]
	lista = generaLista(n)
	pares = paresLista(lista)
	res = []
	newel = []
	#agregar items a pares hasta que se llegue a items de longitud n
	#print pares
	#print lista
	while i < n :
		for el in lista :
			newel = []
			for p in pares :
				newel = list(p)
				newel.append(el)
				#if pertenece(newel,res) == 1 :
				res.append(newel)
				#print newel
		pares = list(res)
		res = []
		i += 1
	#print pares
	return pares

def generaLista(n) :
	i = 0
	res = []
	while i < n :
		res.append(i+1) 
		i += 1
	return res
#Genera todos los pares posibles de una lista de números
def paresLista(l) :
	res = []
	i = 0 
	j = 0
	while i < len(l) :
		j = 0
		while j < len (l) :
			tmp = [l[i],l[j]]
			res.append(tmp)
			j += 1
		i += 1
	return res
#retorna 0 si el elemento e pertenece a la lista l y 1 de otra manera
def pertenece(e,l) :
	i = 0
	while i < len(l) :
		if e == l[i] :
			return 0
		i += 1
	return 1

def hay_jaque_fila(combinacion) :
	i = 0
	n = len(combinacion)	
	while i < n:
		posicion_dama = combinacion[i]
		j = i + 1
		while j < n:
			if posicion_dama == combinacion[j]:
				return 1
			j += 1
		i = i + 1
	return 0
def hay_jaque_diag(combinacion) :
	i = 0
	n = len(combinacion)
	while i < n:
		posicion_dama = combinacion[i]
		j = i + 1
		while j < n :
			posicion_dama2 = combinacion[j]
			dif = posicion_dama2 - posicion_dama
			if dif < 0 :
				dif *= -1
			if dif == j-i:
				return 1
			j = j + 1
		i = i + 1
	return 0
def imprime(tab) :
	i = 0 
	n = len(tab)
	while i <  n :
		posicion_dama = tab[i] - 1
		j = 0 
		while j < n :
			if j == posicion_dama :
				print "* ",
			else :
				print "- ",
			j = j + 1
		print
		i = i + 1
def main():
	n = 8
	tableros = permutaciones.permutaciones_tr(generaLista(n),[])  
	posicion = 0 
	for t in tableros :
		if hay_jaque_fila(t) == 0 :
			if hay_jaque_diag(t) == 0:
				#Una solución
				print t
				posicion += 1
				print 'Posición :', posicion
				imprime(t)
main()

#encoding: utf-8 
def hay_jaque_fila(combinacion) :
	i = 0 
	while i < 8:
		posicion_dama = combinacion[i]
		j = i + 1
		while j < 8:
			if posicion_dama == combinacion[j]:
				return 1
			j += 1
		i = i + 1
	return 0
def hay_jaque_diag(combinacion) :
	i = 0
	while i < 8:
		posicion_dama = combinacion[i]
		j = i + 1
		while j < 8 :
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
	while i < 8 :
		posicion_dama = tab[i] - 1
		j = 0 
		while j < 8 :
			if j == posicion_dama :
				print "* ",
			else :
				print "- ",
			j = j + 1
		print
		i = i + 1
print 'Comenzando'
def main() :
	tablero = [0,0,0,0,0,0,0,0]
	pos = [1,2,3,4,5,6,7,8]
	posicion = 0 
	for i in pos:
		tablero[0] = i 
		for j in pos: 
			tablero[1] = j
			for k in pos :
				tablero[2] = k
				for l in pos : 
					tablero[3] = l
					for m in pos :
						tablero[4] = m 
						for n in pos :
							tablero[5] = n
							for o in pos :
								tablero[6] = o
								for p in pos:
									tablero[7]= p
								
									if hay_jaque_fila(tablero) == 0 :
										if hay_jaque_diag(tablero) == 0:
											#Una solución
											print tablero
											posicion += 1
											print 'Posición :', posicion
											imprime(tablero)

main()





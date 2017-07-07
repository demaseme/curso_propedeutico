#encoding: utf-8
import rectangulo

def main() :
	#Crea los rectangulos.
	listaR = []
	listaR.append( rectangulo.Rectangulo (0,0,3,4,'A') )
	listaR.append( rectangulo.Rectangulo (1,1,3,4,'B') )
	listaR.append( rectangulo.Rectangulo (2,2,3,4,'C') )
	listaR.append( rectangulo.Rectangulo (3,3,3,4,'D') )

	n = len(listaR) 
	print 'Hay: ', n, ' objetos en la lista.'

	i = 0 
	while i < n :
		j= i + 1
		while j < n :
			listaR[i].compara(listaR[j])
			j += 1
		i += 1 
main()

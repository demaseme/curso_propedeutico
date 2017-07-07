#encoding: utf-8 
 
def permutaciones(lista):
	if len(lista) == 0:
		return [[]]
	return sum([inserta_multiple(lista[0], s) for s in permutaciones(lista[1:])],[])

def permutaciones_tr(lista,res):
	#print 'permutaciones_tr(',lista,res,')'
	if len(lista) == 0:
		return res
	if len(res) == 0 :
		r = [lista[0]]
	else: 
		r=inserta_multiple_tr(lista[0],res)

	return permutaciones_tr(lista[1:],r)

def inserta_multiple_tr(x,lista) :
	res = []
	if len(lista) > 1 :
		for item in lista :
			res.extend(inserta_multiple(x,item))
		return res
	else :
		return inserta_multiple(x,lista)
def inserta(x,lista,i):
	res = lista[:i] + [x] + lista[i:]
	return res
def inserta_multiple(x,lista) :
	#'inserta_multiple(',x,lista,')'
	res = []
	for i in range(len(lista)+1): 
		res.append(inserta(x,lista,i))
	return res
print permutaciones_tr([1,2,3,4],[])

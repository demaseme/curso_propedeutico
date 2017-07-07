#encoding: utf-8

class Empleado:
	pass

listaTodos = []

Juan = Empleado()
Juan.nombre = 'Juan Pérez'
Juan.salario = 1000
listaTodos.append(Juan)

Maria = Empleado()
Maria.nombre = 'María Hernández'
Maria.salario = 1100
listaTodos.append(Maria)

for obj in listaTodos :
	print type(obj), obj.nombre,obj.salario

print 'Ok!'

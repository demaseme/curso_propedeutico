#coding: utf-8
#
# El módulo de expresiones regulares en python: 
import re

#Este es un comentario, en una línea
a = "# El comienzo de una línea!"

if re.match( "^\s*#",a ) != None : 
	print a


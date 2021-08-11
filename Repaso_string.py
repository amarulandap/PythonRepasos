# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 11:38:24 2021

@author: Andres Marulanda
"""

"""REPASO OBJETOS STRING"""

"""
from string import digits
from string import ascii_letters
from string import ascii_lowercase
from string import ascii_uppercase
from string import octdigits
from string import hexdigits
from string import punctuation


Imprimir los diferentes tipos de caracteres
print("\ndigitos: ",digits)
print("caracteres ascii: ",ascii_letters)
print("caracteres ascii_mayusculas: ",ascii_lowercase)
print("caracteres ascii_minusculas: ",ascii_uppercase)
print("Signos de puntuación: ",punctuation)
print("Octales: ",octdigits)
print("Hexadecimales: ",hexdigits)
"""

#Definiendo una cadena de caracteres
str_1 = "nueva frase"
str_2 = "HOLA mundo"

#str_1 = input("Ingrese un primer conjunto de caracteres: ")
#str_2 = input("Ingrese un segundo conjunto de caracteres: ")
#print("\n",str_1)
#print(str_2)

#Determinar el tamaño de un string
print(str_1)
print(str_2)
print("\nTamaño de la cadena str_2: ",len(str_2))

#Convertir a mayuscula la pimera letra
print("\nPalabra con la primera letra en mayuscula: ",str_1.capitalize())

#Convertir una cadena de caracteres a minuscula
print("\ncadena convertida a minúsculas: ",str_2.lower())

#Convertir una cadena a mayusculas
print("\ncadena convertida a mayúsculas: ",str_1.upper())

#Convertir de manera simultanea mayúsculas en minúsculas y viceversa
print("")
str_3 = "HoLa MuNdO CrUeL"
print("\nCadena despues del método swapcase: ",str_3.swapcase())

#hallar el número de veces que un caracter se encuentra en una cadena
#El metodo count diferencia letras mayúsculas, minúsculas y con tilde. 
str_4 = "\nEste es un texto de prueba para contar el número de veces que se encuentra un caractér"
print(str_4)
print("Número de veces que se encuentra un caractér en la cadena: ",str_4.count('é'))

#Buscar el indice de una coincidencia
print("\ncuál es el indice de la coincidencia tex: ",str_4.find('tex'))

#Remplazar una subcadena en una cadena
print("\nCadena con la letra e remplazada por la E: ",str_4.replace('e', 'E'))

#Verificar si una subcadena se encuentra en la cadena de caracteres
prueba = "pru" in str_4
print("\n",prueba)

#Eliminar uno o varios caracteres de la cadena (contando las posiciones desde 1)
str_5 = "Bienvenidos"
print("\ncadena sin el primer caracter: ",str_5[4:])
print("\ncadena sin el último caracter: ",str_5[:5])

#Convertir una cadena en formato de Título
str_1a = str_1.title()
print("\ncadena en formato de Título: ", str_1a)

#Centrar una cadena en la pantalla
str_6 = "Texto de prueba método de centrado"
print("\n",str_6.center(50, ' '))
print(str_1)

#Ajustar un texto a la izquierda
str_7 = "Texto de prueba para ajustar"
print("\n",str_7.ljust(50, '*'))

#Ajustar a la derecha
print("\n",str_7.rjust(50, '*'))

#Rellenar un texto anteponiendo ceros
numero_factura = 1575
print("\n",str(numero_factura).zfill(8))

#Convertir una cadena en una lista
print("\nCadena convertida en lista: ",str_7.split(','))
str_8 = "abc,def,ghi,jkl,mno,pqr"
print("\nCadena convertida en lista: ",str_8.split(','))

#Insertar separadores de caracteres
print("\nCadena con separadores insertados: ",'-'.join(str_1))

#Convertir una cadena en una lista de códigos ascii
c = [ord(i) for i in str_1]
print("\ncadena convertida en lista de codigos ascii: ",c)

#Determinar si una palabra es o no el principio de una cadena
print("\nDeterminar si la palabra Texto es el inicio de la cadena 6: ",str_6.startswith('Texto'))

#Determinar si un palabra es el fin de una cadena
print("\nDeterminar si la palabra centrado es el final de la cadena 6: ",str_6.endswith('centrado'))

#determinar si una cadena es alfanumérica
#El método no evalua caracteres diferentes a letras y números
str_9 = "pepegrillo278"
print("\nEs la cadena 9 alfanumérica: ",str_9.isalnum())

#Determinar si una cadena es alfabética
print("\nEs la cadena 9 alfabética: ",str_9.isalpha())

#Determinar si un cadena es numérica
#Si estos métodos encuentran un carater diferente a una letra o número inmeditamente generan False
print("\nEs la cadena 9 numérica: ",str_9.isdigit())

#Determinar si una cadena contiene solo letras minúsculas
#El método solo evalua los caracteres que son letras
str_10 = " *HELLO WORLD* "
print("\nLa cadena 10 contiene solo letras minúsculas: ",str_10.islower())

#Determinar si una cadena contiene solo letras mayúsculas
print("\nLa cadena 10 contiene solo letras mayúsculas: ",str_10.isupper())

#Determinar si una cadena contiene solo espacios en blanco
print("\nla cadena 10 tiene solo espacios en blanco: ",str_10.isspace())

#Determinar si una cadena tiene formato de título
print("\nTiene la cadena 3 formato de título: ",str_1.istitle())

#Dar formato a una cadena sustituyendo texto dinamicamente
cadena = "Importe bruto: ${0} + IVA: ${1} = Importe neto: {2}"
print("\n",cadena.format(100, 19, 119))
cadena_1 = "Importe bruto: ${bruto} + IVA: ${iva} = Importe neto: {neto}"
print(cadena_1.format(bruto=100, iva=100 * 19 / 100, neto=100 * 19 / 100 + 100))

#Remplazar palabra por palabra
print("\ncadena 4 con 'el número rempalzado' por la cantidad: ",str_4.replace('el número', 'la cantidad'))

#Eliminar caracteres a izquierda y derecha
print("\nCadena 10 con caraceteres eliminados a izquierda y derecha: ",str_10.strip(''))

#Eliminar caracteres a la izquierda de la cadena
print("\nCadena 10 con caracteres eliminados a la izquierda: ",str_10.lstrip('*H'))

#Eliminar caracteres a la derecha de la cadena
#Los métodos permiten eliminar uno o varios caracteres, siempre y cuando se incluya el primero
print("\ncadena 10 con carateres eliminados a la derecha: ",str_10.rstrip('D*'))

#--------------------------------
primer_nombre = "Andres"
segundo_nombre = "Felipe"
apellido = "Marulanda"
print("")
print(f"{primer_nombre} {segundo_nombre} {apellido}")

#Utilizar el método join para unir una cadena de manera iterativa
formato_nombre = ("Nombre: ", " Marulanda")
nombre = "Andres Felipe"
print("\n",nombre.join(formato_nombre))

#Partir una cadena en 3 utilizando un separador
print("\nCadena 9 dividida en 3: ",str_9.partition('grillo'))

#Dividir una cadena de lineas en varias partes
str_11 = """Hola
Buenos
días,
cómo amanecen?"""

print("\nCadena de comentarios convertida en lista: ",str_11.splitlines())

















 
















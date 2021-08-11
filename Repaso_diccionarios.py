# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 10:49:35 2021

@author: Andres Marulanda
"""

"""REPASO OBJETOS TIPO DICCIONARIO"""

#Crear un diccionario vacio
dic_1 = {}
print("diccionario vacio: ",dic_1)

#crear un diccionario para verificar sus componentes
dic_2 ={'nombre':'Andres', 'apellido':'Marulanda'}
print("\nDiccionario 2: ",dic_2)

#Obtener el tamaño de un diccionario
print("\nTamaño del dccionario 2: ",len(dic_2))

#Tener acceso a algún elemento del diccionario
print("\nElemento nombre del diccionario: ",dic_2['nombre'])

#Agregar un elemento al diccionario
dic_2['segundo_apellido'] = 'Patiño'
print("\nDiccionario con un dato agregado: ",dic_2)

#Modificar un elemento del diccionario
dic_2['nombre'] = 'Cristina'
print("\nDiccionario modificado: ",dic_2)
 
#Eliminar un elemento del diccionario
del dic_2['segundo_apellido']
print("\nDiccionario después de eliminar el elemento segundo apellido:",dic_2)

val = dic_2.pop('nombre')
print("\nValor eliminado con el método pop: ",val)

#Vaciar un diccionario.
print("\nDiccionario 2 vacio: ",dic_2.clear())

#Copiar un diccionario
dic_3 = {'a':'1', 'b':'2', 'c':'3', 'd':'4', 'e':'5'}
copia = dic_3.copy()
print("\nCopia del diccionario 3: ",copia)

# Crear las claves de un diccionario desde una secuencia
secuencia = ['f', 'g', 'h', 'i', 'j']
numeros = [1,2,3,4,5]
dic_4 = dict.fromkeys(secuencia, [i for i in numeros])
print("\nDiccionario generado a partir de una secuencia, dic_4: ",dic_4)

#Concatenar diccionarios
#Si en los diccionarios hay claves repetidas estas se actualizan
dic_3.update(dic_4)
print("\nConcatenar los diccionarios 3 y 4: ",dic_3)

dic_5 = {'f':'6', 'g':'7', 'h':'8', 'i':'9', 'j':'10'}
dic_3.update(dic_5)
print("\nConcatenar los diccionarios 3 y 5: ",dic_3)


#Acceder al valor asociado a una clave
print("\nValor asociado a la clave b del diccionario 3: ",dic_3.get('b'))

#Conocer las claves que tiene un diccionario
print("\nClave del diccionario 3: ",dic_3.keys())

#Conocer los datos de un diccionario
print("\nValores del diccionario 3: ",dic_3.values())

#-----------------------------------------------------
#métodos adicionales para los objetos de la clase diccionario

#Convertir, si es factible, una representación de diccionario, en diccionario
dic_6 = dict(nombre='nestor', apellido='Plasencia', edad=22)
print("\nDiccionario generado a partir de una representación: ",dic_6)

#Crear un diccionario a partir de dos elementos iterables con la misma cantidad.
#Pueden ser listas, tuplas o cadenas
cadena_a = 'lmnopq'
cadena_b = [10,20,30,40,50,60]
print("\nDiccionario generado a partir de dos iterables: ",dict(zip(cadena_a, cadena_b)))

#Generar una lista de tuplas a partir de un diccionario
print("\nLista de tuplas generada a partir de un diccionario: ",dic_5.items())







    







      



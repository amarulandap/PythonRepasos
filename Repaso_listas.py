# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 07:30:42 2021

@author: Andres Marulanda
"""

"""REPASO OBJETOS TIPO LISTA"""

import random
import numpy as np

#Crear diferentes objetos de la clase list

#Lista vacia
a = []
print("Lista a: ",a)

#Lista cargada con datos directamente.
b = [1, 2, 3, 3, 3, 4.5, 5.3, 5.9, 'a', 'b', 'c', "Hello", "Buenos días", "Cómo estan?"]
print("Lista b: ",b)

#Lista con datos aleatorios
n = 15
c = [0] * n
for i in range (0, n):
    c[i] = random.randint(10, 50)
print("Lista c: ",c)

#Forma alterna de cargar una lista con datos aleatorios
c_1 = [random.randint(10, 50) for i in range(15)]
print("Lista c_1: ",c_1)
    
#Lista de números en un rango definido
d = [i for i in range (10, 21)]
print("Lista d: ",d)

#Lista cargada con datos desde el teclado
m = int(input("Tamaño de la lista: "))
e = [0] * m
for i in range(0, m):
    e[i] = int(input("Ingrese el dato: "))
print("Lista e: ",e)
    
#Lista con datos tipo string desde el teclado
l = int(input("tamaño de la lista de caracteres: "))
f = [''] * l
for i in range(0, l):
    f[i] = input("Ingrese la letra o frase: ")
print("\nLista f: ",f)    

#Agregar un elemento al final de la lista
a.append('q')
print("\nLista a con un elemento agragedo: ",a)

a.append('r')
print("\nLista a con un elemento agragedo: ",a)

#Insertar un elemento en una posición determinada
b.insert(0, 0)
print("\nLista b con un elemento insertado: ",b)

#Agregar varios datos al final de la lista
a.extend(['a', 1])
print("\nLista a con una extensión de datos: ",a)

#Saber el tamaño de la lista
tamagno = len(b)
print("\ntamaño de la lista b: ",tamagno)

#Determinar cuantas veces se encuentra un elemento en una lista
c_1 = b.count(3)
print("")
print("Número de veces que el elemento esta en la lista: ",c_1)

#Conocer en que posición esta un determinado elemento
i_1 = d.index(19)
print("")
print("Posición en la que se encuentra el dato: ",i_1)

#Acceso a secciones de una lista
print("")
print(b[:4])
print(b[4:8])
print(b[8:])

#Concatenar dos lista(sobrecarga del operador +)
print("")
print("Lista a concatenada con una parte de b: ",a + b[4:8])

#Eliminar un elemento por su valor
print("")
b.remove(3)
print("Lista b después de remover el dato 3: ",b)

#Eliminar el último elemento de la lista
print("")
x = b.pop()
print(x)
print("Lista b después de eliminar el último dato: ",b)

#Eliminar un dato en una determinada posición
#Podemos utilizar el método del[2], indicando la posición del elemento a eliminar
print("")
b.pop(4)
print("Lista b después de eliminar el dato de la posicion 4: ",b)

#Eliminar todos los datos de la lista
print("")
a.clear()
print("Lista a de nuevo vacia: ",a)

#Invertir el orden de una lista
print("")
d.reverse()
print("Lista d en orden inverso: ",d)

#Ordenar la lista de manera ascendente
print("")
c.sort()
print("Lista c ordenada ascendentemente: ",c)

#caso especial de sort()
#no se pueden ordenar datos de diferentes tipos
print("")
g = [[1, 2], [4, 5], [9, 8], [3, 6]]
g.sort()
print("Lista g ordenada ascendentemente: ",g)

#Ordenar la lista de forma descendente
h = [1, 90, 8, 58, 15, 12, 18]
print("")
h.sort(reverse=True)
print("Lista h ordenada descendentemente: ",h)

#Reproducción de listas
print("")
h_1 = h * 2
print("Lista h reproducida: ",h_1)

#Formar pares entre dos listas, o construir una lista de tuplas
h_2 = [6, 0, 25, 45, 16, 3, 4]
print("")
print(list(zip(h, h_2)))

#tener acceso a un elemento en particular
print("")
print(h_2[0])
#Se pueden construir listas por mapeo con los datos retornados por una función
#h_3 = map(nombre_función, range(número de datos que deseo cargar))
#print(list(h_3))

#Construir listas mediante un filtro
#h_4 = [1,2,3,4,5,6,7,8,9,10]
#h_5 = filter(nombre de una función,h_4)
#def función(h_4)
#print(list(h_5))

#Convertir una lista en un arreglo
arreglo_1 = np.array(b)
print("\n",arreglo_1)










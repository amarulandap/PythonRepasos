# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 21:26:09 2021

@author: Andres Marulanda
"""

"""OPERACIONES CON VECTORES Y MATRICES"""

import numpy as np

vec_1 = np.array([1, 2, 3, 4, 5])
vec_2 = np.random.randint(1, 20, size = 10)
vec_3 = np.array([6, 7, 8, 9, 10])
vec_4 = np.arange(12)

mat_1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
mat_2 = np.random.randint(1, 20, size = (4,5))
mat_3 = np.random.randint(21, 40, size = (4,5))

mat_4 = np.array([[1, 1], [2, 2]])
mat_5 = np.array([[3, 3],[4, 4]])


#Ordenar los datos de los arreglos de manera ascendente
#En las matrices quedan ordenados los elementos de las filas
vec_2.sort()
mat_2.sort()
print("\nVector 2 ordenado ascendentemente: ",vec_2)
print("\nMatriz 2 ordenada ascendentemente: ",mat_2)

#Generar arreglos con los datos de 0 a n
print("")
print(vec_2.argsort())
print(mat_2.argsort())

#Concatenar arreglos(agregar un arreglo a continuacion del otro)
vec_2c3 = np.concatenate((vec_2,vec_3))
print("\nVector 2 concatenado con vector 3: ",vec_2c3)

mat_2c3 = np.concatenate((mat_2,mat_3), axis=0)
print("\nMatriz 2 concatenda con matriz 3: ",mat_2c3)

#Reformar una matriz
print("\nVector 3 reformado en una matriz: ",vec_4.reshape(3,4))
print("\nMatriz 1 reformada: ", mat_1.reshape(9))

np.reshape(mat_1, newshape = (9)) #order = 'C')
print("\n",mat_1)

#Agregar un nuevo eje a la matriz
vec_2a = vec_2[np.newaxis, :]  #Convierte el arreglo en un vector fila(row_vector)
print("\nvector 2 como vector fila: ",vec_2a.shape)
vec_1a = vec_1[:, np.newaxis]
print("\nvector 1 como vector columna: ",vec_1a.shape)
mat_2a = mat_2[np.newaxis, :]
print("\nMatriz 2 con un nuevo eje: ",mat_2a.shape)

#Insertar un nuevo eje en una posicion especifica
#axis = 0, vector fila
#axis = 1, vector columna
vec_3a = np.expand_dims(vec_3, 1)
print("\nvector 3 como vector columna: ",vec_3a.shape)
print("\nVector 3 con un nuevo eje en la posición 2: ",vec_3a)

#Conocer los subindices de los elmentos que cumplen con una caracteristica
#Genera una tupla de listas donde la primera indica la fila y la segunda la columna de cada elemento
#Puedo usar nonzero para saber si un elemento pertenece al arreglo
mat_2b = np.nonzero(mat_2 < 10)
print("\nPosiciones de los elementos menores que 10 en la matriz 2: ",mat_2b)

#Lista de coordenadas de una matriz
lista_cord = list(zip(mat_2b[0], mat_2b[1]))
for i in lista_cord:
    print(i)
    
#Apilar matrices vertical y horizontalmente
apilar_1 = np.vstack((mat_4, mat_5))
print("\nMatrices 4 y 5 apiladas verticalemnte: ",apilar_1) #Mismo número de columnas
apilar_2 = np.hstack((mat_4, mat_5))
print("\nMatrices 4 y 5 apiladas horizontalmente: ",apilar_2) #Mismo numero de filas

#Convertir un arreglo en una lista
lista_1 = mat_1.tolist()
print("\nMatriz 1 convertida en lista: ",lista_1)


#-----------------------------------------------------------------------------

"""Operaciones básicas con los arreglos"""
#Sobreacarga de operadores
#Puede realizar estas operaciones aritméticas en matrices de diferentes tamaños, 
#pero solo si una matriz tiene solo una columna o una fila. 

#Sumar dos arreglos (estos deben tener las mismas dimensiones)
vec_suma = vec_1 + vec_3
print("\nVector suma: ",vec_suma)

mat_suma = mat_2 + mat_3
print("\nMatriz suma: ",mat_suma)

#Sumar todos los elementos de un arreglo
print("\nSumatoria de los elementos del vector 2: ",vec_2.sum())
print("\nSumatoria de los elementos de la matriz 4: ",mat_4.sum(axis = 0)) #Suma las columnas
print("\nSumatoria de los elementos de la matriz 4: ",mat_4.sum(axis = 1)) #Suma las filas

#Restar dos arreglos
vec_resta = vec_3 - vec_1 
print("\nVector resta: ",vec_resta)
mat_resta = mat_3 - mat_2
print("\nMatriz resta: ",mat_resta)

#Multiplicación termino a termino
vec_producto = vec_1 * vec_3
print("\nVector producto: ",vec_producto)
mat_producto = mat_3 * mat_2
print("\nMatriz producto: ",mat_producto)

vec_prod = vec_4 * 4
print("\nVector de radiodifusión: ",vec_prod)

#Producto punto entre dos arreglos
vec_producto_1 = np.dot(vec_1,vec_1a)
print("\nProducto punto entre dos vectores: ",vec_producto_1)
mat_3_prod = mat_3.reshape(5,4)
mat_producto_1 = np.dot(mat_3_prod,mat_2)
print("\nProducto punto entre dos matrices: ",mat_producto_1)

#Division entre arreglos
vec_division = vec_3 / vec_1 
print("\nDivisión de dos vectores: ",vec_division)
mat_division = mat_3 / mat_2
print("\nDivisión de dos matrices: ",mat_division)

#Hallar el mínimo y el máximo valor de un arreglo
print("\nMínimo valor del vector 2: ",vec_2.min())
print("\nMáximo valor de la matriz: ",mat_producto_1.max())

#Hallar el valor mínimo dentro de cada columna
print("\nMínimo valor de las columnas de la matriz: ",mat_producto_1.min(axis = 0))
#Hallar el mímino valor dentro de cada fila
print("\nMínimo valor de las filas de la matriz: ",mat_producto_1.min(axis = 1))

#Hallar la raiz cuadrada de un arreglo
print("\nRaiz cuadrada de una matriz: ",np.sqrt(mat_producto_1))

#-----------------------------------------------------

#Operaciones trigonometricas
mat_angulos = np.array([15, 30, 45, 60, 75, 90, 120, 150, 180, 225, 270, 315])
print("\nMatriz de angulos: ",mat_angulos)

#seno
senos = np.sin(mat_angulos)
print("\nSeno: ",senos)

#coseno
cosenos = np.cos(mat_angulos)
print("\ncosenos: ",cosenos)

#Función exponencial
exponencial = np.exp(mat_angulos)
print("\nExponencial: ",exponencial)

#Función logaritmo
logaritmos = np.log(mat_angulos)
print("\nLogaritmos: ",logaritmos)












    










 

























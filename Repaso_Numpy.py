# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 18:37:41 2021

@author: Andres Marulanda
"""

"""REPASO NUMPY"""

import numpy as np

#Una matriz es un arreglo de arreglos, es decir, un vector es un arreglo de una dimension.
#Crear vectores y matrices

#vector con datos asignados directamente
vec_1 = np.array([1, 2, 3, 4, 5])
print("Vector 1: ",vec_1)

#vector con datos aleatorios
vec_2 = np.random.randint(1, 20, size = 10)
print("\nVector con datos aleatorios: ",vec_2)

vec_2_al = np.random.random(10)
print("\nvector con datos aleatorios 2: ",vec_2_al) #Genera números aleatorios entre cero y uno

#Vector 0
vec_3 = np.zeros(5)
print("\nvector zero: ",vec_3)

#Vector 1
vec_4 = np.ones(5)
print("\nvector 1: ",vec_4)

#Vector vacio
vec_empty = np.empty(5)
print("\nVector vacio: ",vec_empty)

#Vector con el mismo valor
vec_5 = np.full(5, 8)
print("\nvector con datos iguales: ",vec_5)

#Vector con un rango de elementos
vec_6 = np.arange(10)
print("\nVector con números en un rango de 0 a n: ",vec_6)

#vector que contiene un rango de intervalos espaciados uniformemente
vec_7 = np.arange(1, 20, 2)
print("\nvector por intervalos de 2: ",vec_7)

#Vector con valores espaciados linealmente en un intervalo especificado
vec_8 = np.linspace(0, 20, 8, dtype = np.int32)
print("\nVector con datos espaciados linealemnte: ",vec_8)

#Especificar el tipo de dato
vec_9 = np.ones(5, dtype = np.int64)
print("\nvector con tipo de dato especifico: ",vec_9)

#Acceso a un dato de un vector
print("\nDato en la posicion uno del vector 8: ",vec_8[1])

#Modificar el dato en una determinada posición
vec_9[1] = 5
print("\nVector 9 con un dato modificado: ",vec_9)

#Subarreglos
vec_2a = vec_2[:4]
print("\nSubvector 2: ",vec_2a)

vec_2b = vec_2[5:]
print("\nSubvector 2: ",vec_2b)

vec_2c = vec_2[1:8:2]
print("\nSubvector 2: ",vec_2c)


"""matrices"""

#Matriz con datos asignados directamente
mat_1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("\nMatriz  1: ",mat_1)

#Matriz con datos aleatorios
mat_2 = np.random.randint(1, 20, size = (4,5))
print("\nmatriz de datos aleatorios: ",mat_2)

mat_2_al = np.random.random((4,5))                  #matriz con datos entre 0 y 1
print("\nMatriz con datos aleatorios 2: ",mat_2_al)

#matriz de 3 dimensiones
#3 matrices de 4 filas y 5 columnas
mat_3 = np.random.randint(1, 20, size = (3,4,5))
print("\nMatriz de 3 dimensiones: ",mat_3)

#Matriz con un tipo de dato determinado
mat_4 = np.array([[10,20,30],[40,50,60],[70,80,90]], dtype = np.complex128)
print("\nMatriz con un tipo de dato especifico: ",mat_4)

#Matriz 0
mat_5 = np.zeros((2,3))
print("\nmatriz cero: ",mat_5)

#Matriz 1
mat_6 = np.ones((4,5))
print("\nMatriz uno: ",mat_6)

#Matriz vacia
mat_7 = np.empty((3,4), dtype = np.int32)
print("\nMatriz vacia: ",mat_7)

#Matriz con un solo dato
mat_8 = np.full((3,2), 7)
print("\nMatriz full: ",mat_8)

#Matriz Identidad
mat_9 = np.eye(4,4)
print("\nMatriz identidad 1: ",mat_9)

mat_9a = np.identity(4)
print("\nMatriz identidad 2: ",mat_9a)

#Acceso a un elemento de una matriz
print("\nDato de la matriz 1 en la posicioón (2, 2): ",mat_1[2,2])

#Modificar un dato de una matriz
mat_1[1,1] = 2*3
print("\nMatriz 1 modificada: ",mat_1)

#Subarreglos
mat_2a = mat_2[:2, :3]
print("\nSub matriz 2: ",mat_2a)

mat_2b = mat_2[1:, 1:]
print("\nSub matriz 2:",mat_2b)

mat_2c = mat_2[::2, ::2]
print("\nSub matriz 2: ",mat_2c)

#------------------------------------------------

#Conocer la dimension de los arreglos
print("\nDimensión del vector 1: ",vec_1.ndim)
print("Dimensión de la matriz 1: ",mat_1.ndim)

#Conocer el número total de elementos de la matriz
print("\nNúmero de elementos del vector 1: ",vec_1.size)
print("Número de elementos de la matriz 1: ",mat_1.size)

#Determinar que forma tiene el arreglo
print("\nForma del vector 1: ",vec_1.shape)
print("Forma tiene la matriz 1: ",mat_1.shape)

#-------------------------------------------------

#Subarraeglos con caracetristicas particulares

print("\nSubarreglos de a: ")
a = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

five_up = (a >= 5)
print(a[five_up])
print("")
divisible_by_2 = a[a%2 == 0]
print(divisible_by_2)
divisible_by_3 = a[a%3 == 0]
print(divisible_by_3)

#Dividir una matriz en matrices mas pequeñas
vec_b = np.arange(1, 25).reshape(2, 12)
print("\n",vec_b)
vec_b_div = np.hsplit(vec_b, 4)                 #Divide el arreglo de manera horizontal
print("\nMatriz b dividida en 4: ",vec_b_div)   #vsplit lo divido de manera vertical

#Realizar una copia profunda de una matriz
#Si se modifica la copia, cambia la matriz original
copia_mat_4 = mat_4.copy()
print("\nCopia de la matriz 4: ",copia_mat_4)

#Otra forma de obtener la copia de una matriz 
x = mat_4.view()
print("\nCopia de la matriz 4: ",x)


















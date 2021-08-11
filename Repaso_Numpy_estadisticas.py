# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 17:47:42 2021

@author: Andres Marulanda
"""

"""OPERACIONES ESTADISTICAS Y MATRICIALES"""

import numpy as np

vec_1 = np.random.randint(1, 10, size = 20)
vec_2 = np.arange(15)

mat_1 = np.random.randint(1, 50, size = (5,5))
mat_2 = np.random.randint(1, 21, size = (4,5))
mat_3 = np.random.randint(1, 10, size =(2,3))
mat_4 = np.array([[1,2,3],[4,5,6],[7,8,9]])


print("\n",mat_1)
#Hallar la media aritmética
print("\nMedia aritmética de la Matriz: ",np.mean(mat_1))

#Hallar la desviación standard
print("\nDesviación estandard de la Matriz: ",np.std(mat_1))

#Determinar la diagonal principal de la matriz
print("\nDiagonal principal de la matriz: ",np.diagonal(mat_1))

#Determinante de la matriz
print("\ndeterminante de la matriz: ",np.linalg.det(mat_1))
#Inversa de la matriz
print("\nInversa de la matriz: ",np.linalg.inv(mat_1))

#Transpuesta de la matriz
print("\nTranspuesta de la matriz: ",np.transpose(mat_1))

#Hallar la matriz triangular inferior
print("\nMatriz triangular inferior: ",np.tril(mat_1))

#Hallar la matriz triangular superior
print("\nMatriz triangular superior: ",np.triu(mat_1))

#Eliminar los datos repetidos de un arreglo
unicos_valores = np.unique(vec_1)
print("\nVector con datos únicos: ",unicos_valores)

#Los subindices de los datos únicos
unicos_valores, indice_uni_val = np.unique(vec_1, return_index = True)
print("\nIndices de valores únicos: ",indice_uni_val)

#Con contador_ocurrencias obtengo un vector de ocurrencias de cada dato
#unicos_valores, indice_uni_val = np.unique(vec_1, return_index = True)
#Sustituir return_index por return_counts

unicos_valores_mat = np.unique(mat_2)
print("\nVector con datos únicos: ",unicos_valores_mat)

unicos_valores_filas = np.unique(mat_2, axis = 0)
print("\nValores únicos por filas: ",unicos_valores_filas)

#A las matrices tambien se le pueden aplicar los métodos return_index y return_counts
#unique_rows, indices, occurrence_count = np.unique(
#a_2d, axis=0, return_counts=True, return_index=True)
#print(unique_rows)
#print(indices)
#print(occurrence_count)

#Invertir el orden de un arreglo
vec_2_inv = np.flip(vec_2)
print("\nVector 2 con orden invertido: ",vec_2_inv)
mat_3_inv = np.flip(mat_3)
print("\nmatriz 3 con orden inverso: ",mat_3_inv) #Invierte el orden de las filas y columnas de manera simultanea
mat_3_inv_1 = np.flip(mat_3, axis = 0)
print("\nmatriz 3 con orden inverso: ",mat_3_inv_1) #Invertir el orden solo de las columnas
#Usando axis = 1 invertimos el orden de las filas

#Si deseo invertir el orden solo una fila -- np.flip(mat_3[1])
#Si deseo invertir el orden solo una columna -- np-flip[:,1] 

#Aplanar y acoplar matrices
print("\nMatriz 4 acoplada: ",mat_4.flatten()) #Los cambios en la nueva matriz no generan cambios en la original
mat_4_a = np.ravel(mat_4)
print("\nMatrix acoplada con ravel: ",mat_4_a)# Los cambios en lamatriz nueva si afectan a la orginal
mat_4_a[2] = 11

#Guardar arreglos en un archivo para no tener que reutilizar el codigo
#Si desea almacenar un único objeto, almacéne como un archivo .npy 
#Puede guardar varias matrices en un solo archivo en formato .npz comprimido con savez_compressed

#a = np.array([1, 2, 3, 4, 5, 6])
#np.save('filename', a)
#np.savez --- guardar varios arreglos en un solo archivo

#Puede utilizar para reconstruir la matriz. np.load()
#b = np.load('filename.npy')
#print(b)

#Puede guardar una matriz NumPy como un archivo de texto sin formato 
#como un archivo .csv o .txt con .np.savetxt
#csv_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
#np.savetxt('new_file.csv', csv_arr)
#np.loadtxt('new_file.csv')













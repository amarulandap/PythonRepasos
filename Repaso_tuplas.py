# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 10:39:33 2021

@author: Andres Marulanda
"""

"""REPASO DE TUPLAS"""

import random

#Crear una tupla vacia no tiene sentido ya que estas no se pueden modificar
#después de ser creadas
#No es posible crear una tupla con datos aleatorios

#Crear una tupla con elementos conocidos por el usuario
t_1 = (1, 2, 3, 4, 5, 6, 7)
t_2 = ('a', 'b', 'c', 'd', 'e')
t_3 = (1, 'a', 2, 'b', 4.5, 'Hola', 3.8, 'buenas tardes')
t_4 = ()
print("Tupla 1: ",t_1)
print("Tupla 2: ",t_2)
print("Tupla 3: ",t_3)
print("Tupla 4: ",t_4)

#Para tener acceso a un dato de la tupla
print("")
print("Dato de la tupla 2 en la posisicon 4: ",t_2[4])

#Acceso por secciones a una tupla
print("")
print(t_3[:3])
print(t_3[2:5])
print(t_3[5:])

#Agregar datos a una tupla usando la sobrecarga de opaeradores
#Sin embargo, no modifica la tupla original
print("")
print("Tupla 4 después de agregarle datos: ", t_4 + (10, 11, 12, 13, 14, 15, 16))
print(t_4)

#Concatenar tuplas
print("")
print(f"Tupla 1 + Tupla 4: {t_4 + t_1}")

#Conversión de tipos: Convertir una lista en tupla y viceversa
print("")
print("Tupla 1 convertida en lista:", list(t_1))

print("")
b = [1, 2, 3, 3, 3, 4.5, 5.3, 5.9, 'a', 'b', 'c', "Hello", "Buenos días", "Cómo estan?"]
print("Lista b convertida en Tupla: ",tuple(b))

#Daterminar la cantidad de elementos que tiene una tupla
print("")
print("Tamaño de la tupla 3: ", len(t_3))

#Determinar el mínimo y maxímo valor en una lista o en una tupla
c = [random.randint(10, 50) for i in range(15)]
c.sort()

print("")
print("El mínimo valor de la tupla 1 es: ",min(t_1))
print("El máximo valor de la tupla 1 es: ",max(t_1))

print("")
print("Lista c: ",c)
print("El mínimo valor de la lista c es: ",min(c))
print("El máximo valor de la lista c es: ",max(c))





    
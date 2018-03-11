# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 23:52:18 2018

@author: jonas.j.torres
"""
#Usar la formula de constrained composition
#1)tengo que buscar todas las combinaciones posible de los 3 dados
#2)contar todas las permutaciones que cumplen con que el mayor de todos los
#    numeros sea x_max
#3) dividir la las permutaciones que cumplen este criterio por el numero
#    total de permutaciones

f = [2,5,8]
x_max = 8

#You can use one for loop to compute P(X<=x) and P(X<=x-1) and return 
#the difference since the number of elements for both the computation is same.

#I iteratively calculated P(X≤x) by multiplying the probablities of all dices 
#with one another for all cases when X≤x. Then I did the same for P(X<=x-1) 
#and returned the difference of both results. You really don't need any 
#numpy/itertools functionalities to solve problem.

 
def largest_face(f, x_max):
    
    p1=1
    p2=1    
    for die in f:
        if die >= x_max:
            A = np.array([i for i in range(1,die+1)])
            e = sum(A<=x_max)
            p1 *= e/float(die)
            p2 *= (e-1)/float(die)
        
    return p1-p2



# Face Sum

m = [3,4,5]
s = 3

def face_sum(m, s):
    ar = np.array(m)
    events = constrained_compositions(s, m)
        
    return len(events)/float(ar.prod())


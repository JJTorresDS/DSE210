# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 23:52:18 2018

@author: jonas.j.torres
"""


parts = set()


#compute combinations of the possible elements. We can use the combinations
#functions

# example of 2 dice 3 and 4 faced:
largest_face([2,5,8],8)

f = [2,5,8]
x_max = 8
#Usar la formula de constrained composition
1)tengo que buscar todas las combinaciones posible de los 3 dados
2)contar todas las permutaciones que cumplen con que el mayor de todos los
    numeros sea x_max
3) dividir la las permutaciones que cumplen este criterio por el numero
    total de permutaciones


def largest_face(f, x_max):
    
    def product(*args, repeat=1):
        # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
        # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
        pools = [tuple(pool) for pool in args] * repeat
        result = [[]]
        for pool in pools:
            result = [x+[y] for x in result for y in pool]
        for prod in result:
            yield tuple(prod)
    
    #Base case: Only one die
    if type(f)==int:
        # Posibles combinaciones del dado
        A = {i for i in range(1,f+1)} 
        # Si el número máximo esta en el dado entonces prob=1/|A|
        if x_max in A:
            return 1/len(A)
        else:
            return 0
  
    else:
        # Por cada dado en F
        temp = list()
        for die in f:
            temp.extend([i for i in range(1,die+1)])
        
        temp = set(product(temp, repeat=len(f)))
        
        temp2 = set()     
        for x in temp:
            boolVector = []
            counter = 0
            for i in x:         
                boolVector.append(i > f[counter])
                counter += 1
                   
            if sum(boolVector) == 0:
                temp2.add(x)
        
        temp3 = set()     
        for x in temp2:
                               
            if max(x)==x_max:
                temp3.add(x)
                    
        
        return len(temp3)/len(temp2)     

# Face Sum
def face_sum(m, s):
    #m=[3,4,5]
    #s=3
    def product(*args, repeat=1):
        # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
        # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
        pools = [tuple(pool) for pool in args] * repeat
        result = [[]]
        for pool in pools:
            result = [x+[y] for x in result for y in pool]
        for prod in result:
            yield tuple(prod)
   
    # Por cada dado en F
    temp = list()
    f = m
    for die in f:
        temp.extend([i for i in range(1,die+1)])
    
    temp = set(product(temp, repeat=len(f)))
    
    temp2 = set()     
    for x in temp:
        boolVector = []
        counter = 0
        for i in x:         
            boolVector.append(i > f[counter])
            counter += 1
               
        if sum(boolVector) == 0:
            temp2.add(x)
    
    temp3 = constrained_compositions(s, m)
        
    return len(temp3)/len(temp2)

# i.e (1,2), (2,2), (2,1) 
# I could either loop through each element and create a boolean and some up
# the true values
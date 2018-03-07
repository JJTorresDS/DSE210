# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 20:44:11 2018

@author: jonas.j.torres
"""
import numpy as np


##### Problem 1: Integer Compositions
def compositions(k, n):
    
    def product(*args, repeat=1):
        # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
        # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
        pools = [tuple(pool) for pool in args] * repeat
        result = [[]]
        for pool in pools:
            result = [x+[y] for x in result for y in pool]
        for prod in result:
            yield tuple(prod)
            
    A= {i for i in range(1,n+1)}     
    permute_k = set(product(A, repeat=k)) 
    
    finalComp = set()        
    for x in permute_k:
        tempSum = 0
        for i in x:
           tempSum = tempSum + i
        
        if tempSum == len(A):
            finalComp.add(x)
               
    return finalComp 
    
##### Problem 2: Counting Compositions

def composition_formula(k, n):
    # inputs: k and n are of type 'int'
    # output: a set of tuples, (int, int)
    def binom(n,k):
        n= n-1
        k= k-1
        def factorial(n):
            if n == 0:
                return 1
            else:
                return n * factorial(n-1)
        
        
        return factorial(n)/(factorial(k)*factorial((n-k)))
    return (len(compositions(k,n)), int(binom(n, k)))

#### Problem 3: Contrained compositions
n = 7
m = [3, 2, 5]

def constrained_compositions(n, m):
    # inputs: n is of type 'int' and m is a list of integers
    # output: a set of tuples
    
    tempComp = compositions(len(m), n)
    
    finalComp = set()        
    for x in tempComp:
        boolVector = []
        counter = 0
        for i in x:         
            boolVector.append(i > m[counter])
            counter += 1
               
        if sum(boolVector) == 0:
            finalComp.add(x)
               
    return finalComp 
    
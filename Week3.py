# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 21:23:09 2018

@author: jonas.j.torres
"""

A = {1, 2, 3}
B = {3, -6, 2, 0}

# Problem 1.1
def union(A, B):
    # inputs: A and B are of type 'set'
    # output: a tuple of the type (set, set_length)
    
    #
    # YOUR CODE HERE
    #
    union = A | B
    return (union, len(union))

# Problem 1.2

A = {1, 2, 3, 4, 5}
B = {0, 2, -6, 5, 8, 9}


def inclusion_exclusion(A, B):
    # inputs: A and B are of type 'set'
    # output: a tuple of four integers
    
    inter = A & B
    
    return (len(A), len(B), len(inter), len(A|B))

#Problem 2.1

A = {1, 2, 4, 5, 10}
B = {5, 2, -6, 5, 8, 9}
C = {2, 10, 13}

def union3(A, B, C):
    # inputs: A, B and C are of type 'set'
    # output: a tuple of the type (set, set_length)
    
    return (A | B | C, len(A | B | C))

#Problem 2.2
A = {1, 2, 4, 5, 10}
B = {5, 2, -6, 5, 8, 9, 10}
C = {2, 10, 13}


def inclusion_exclusion3(A, B, C):
    # inputs: A, B and C are of type 'set'
    # output: a tuple of two integers
    sizeA = len(A)
    sizeB = len(B)
    sizeC = len(C)
    sizeAB = len(A&B)
    sizeAC = len(A&C)
    sizeBC = len(B&C)
    inter = A & B & C
    
    
    return (len(A&B&C), len(A|B|C))
    
    
    
    
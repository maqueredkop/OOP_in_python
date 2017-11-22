# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 15:05:21 2017

@author: maque
"""

class Complex:
    def __init__(self,realpart,imagpart):
        self.r = realpart
        self.i = imagpart
        
    def f(self):
        return "hello world"
    
    def f2(self, name):
        return 'Hi...'

       
## class instantiation
## now the x is a instance object
x = Complex(3.0, -4)

## instance object has two kinds of valid attribute names
## one is data attribute and methods

## data attribute call be called
x.r

## also, Data attributes need not be declared; like local variables, 
## they spring into existence when they are first assigned to.
x.name = 'world'

##  The other kind of instance attribute reference is a method.
##  A method is a function that “belongs to” an object.

##  By definition, all attributes of a class that are function objects define corresponding methods of its instances.
##  So, x.f is a valid method reference, since Complex.f is a function
## x.f is a method object
x.f

## a method is called:
x.f()

## x.f() was called without an argument above
## the special thing about methods is that the instance object is passed as the first argument of the function.
## so the two lines below is exactly equivalent
x.f()
Complex.f(x)

## so the two lines below is exactly equivalent
x.f2('foo')
Complex.f2(x, 'foo')


####################################

class Dog:
    
    kind = 'canine'
    
    def __init__(self, name):
        self.name = name
        
d = Dog('Fido')
e = Dog('Buddy')

d.kind
e.kind
d.name
e.name


######################################
## Methods may call other methods by using method attributes of the self argument:

class Bag:
    def __init__(self):
        self.data = []
        
    def add(self, x):
        self.data.append(x)
        return self.data

x = Bag()
print(x.add(5))

#####################################

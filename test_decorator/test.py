#!/usr/bin/env python
# coding=utf-8
def decorator1(func):  
    def wrapper():  
        print 'hello python 1'  
        func()
        print 'end 1'
    return wrapper  

def decorator2(func):  
    def wrapper():  
        print 'hello python 2'  
        func()
        print 'end 2'
    return wrapper  

@decorator1  
def test():  
    print 'hello python!'  

test() 

'''
Created on Jan 3, 2013

@author: achock
'''

class Calculator:
    '''
    classdocs
    '''


    def __init__(self,num1=0,num2=0):
        '''
        Constructor
        '''
        self.num1 = num1
        self.num2 = num2
        
    def add(self,num1,num2):
        result = num1 + num2
        return result
    
    def sub(self,num1,num2):
        result = num1 - num2
        return result
    
    def divide(self,num1,num2):
        if num2 != 0 :
            result = num1/num2
            return result
        else:
            print "This can not be divided"
        
    def multiply(self,num1,num2):
        result = num1 * num2
        return result
    

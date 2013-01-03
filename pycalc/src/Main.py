'''
Created on 01/01/2013

@author: Steven Rey Sequeira
'''
from PyCalc import PyCalc

if __name__ == '__main__':
    opcion= 0
    
    try :
        calc= PyCalc()
       
        while opcion != 5:
            opcion= calc.printMenu()
        
            if int(opcion) == 5:
                break
            else :
                calc.calcular(int(opcion))
    except ValueError as ex:
        print 'El valor {0} no es un numero: '.format(opcion)
    
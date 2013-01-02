'''
Created on 01/01/2013

@author: Steven Rey Sequeira
'''

class PyCalc(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self._valor1= 0
        self._valor2= 0
    
    def printMenu(self):
        print """
        Primer calculadora en Python v1.0
              
        1. Sumar
        2. Restar
        3. Multiplicar
        4. Dividir
                
              """
        return raw_input('Selecciona la operacion: ')
    
              
    def calcular(self, opcion):
        try:
            self._valor1= float(raw_input('Primer Numero: '))
            self._valor2= float(raw_input('Segundo Numero: '))
                
            if(opcion == 1): # Suma
                print 'El resultado de la suma es: {0}'.format(self._valor1 + self._valor2)
                
            elif(opcion == 2): # Resta
                print 'El resultado de la resta es: {0}'.format(self._valor1 - self._valor2)
            
            elif(opcion == 3): # Mutiplicar
                print 'El resultado de la multiplicacion es: {0}'.format(self._valor1 * self._valor2)
            
            elif(opcion == 4): # Dividir
                if(self._valor2 == 0):
                    print 'El divisor no puede ser <= a 0'
                else:
                    print 'El resultado de la divicion es: {0}'.format(self._valor1 / self._valor2)
                    
            else:
                print 'El valor {0} no es correcto'.format(opcion)
            
                
        except ValueError as ex:
            print 'Error al intentar obtener el valor, numero: {0}, mensaje: {1}'.format(ex.errono, ex.strerror)
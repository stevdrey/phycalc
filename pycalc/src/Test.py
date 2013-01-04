#!/usr/bin/python

import os
import sys
import platform
from File import File
from Calculator import Calculator

loop = 1 # 1 means loop; anything else means don't loop.
choice = 0 # This variable holds the user's choice in the menu
 
while loop == 1:
    # Print what options you have
    print "Please choose from the following menu:"
    print "1) Move File "
    print "2) Calculator"
    print " "
    choice = int(raw_input("Choose your option:").strip())
    if choice == 1:
        opsys = platform.system()
        sourcePath = r'C:\Users\achock\PythonDev'
        destPath = r'C:\Users\achock\PythonDev'
        print "Welcome"
        print "Current working dir : %s" % os.getcwd()
        print "Please name your file"
        fname = raw_input("Enter name of file\n")
        file = File(sourcePath,destPath,fname) 
        fnew = os.path.isfile(fname)#checks to see if the file exist on curdirectory
        file.exists(fnew)#gives message if exists
        destPath = raw_input("Enter the directory in which you would like to copy file. \n For example C:\Users\achock\PythonDev\n")
        ndir = os.path.isdir(destPath)
        file.verDir(ndir)
        file.moveFile(fname,destPath,opsys) 
    elif choice == 2:
        print "Your options are:"
        print " "
        print "1) Addition"
        print "2) Subtraction"
        print "3) Multiplication"
        print "4) Division"
        print "5) Quit calculator"
        print " "
        operator = int(raw_input("Choose your option: ").strip())
        calc = Calculator()
        if operator == 1:
            add1 = input("Add this: ")
            add2 = input("to this: ")
            print add1, "+", add2, "=", calc.add(add1,add2)
        elif operator == 2:
            sub2 = input("Subtract this: ")
            sub1 = input("from this: ")
            print sub1, "-", sub2, "=", calc.sub(sub1,sub2)
        elif operator == 3:
            mul1 = input("Multiply this: ")
            mul2 = input("with this: ")
            print mul1, "*", mul2, "=", calc.multiply(mul1,mul2)
        elif operator == 4:
            div1 = input("Divide this: ")
            div2 = input("by this: ")
            print div1, "/", div2, "=", calc.divide(div1,div2)
        elif choice == 5:
            loop = 0
            print "Bye"
            sys.exit() 
    
        
    

      


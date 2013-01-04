'''
Created on Jan 2, 2013

@author: achock
'''
import os, sys
import shutil

class File:


    def __init__(self,curdir,destdir,name):
        '''
        Constructor
        '''
        self.name = name
        self.curdir = curdir
        self.destdir = destdir

    def exists(self,mfile):
        if mfile == True :
            print "The file already exist."
            sys.exit()
            
    def checkOs(self,opsys,directory):
        if opsys != 'Windows':
            return directory
        else:
            return directory
        
    def verDir(self,directory):
        mdir = directory
        if mdir == False :
            print "This is not a correct directory"
            sys.exit()
            
    def moveFile(self,nfile,address,opsys):
        #r = "r'"
        currentdirectory = os.getcwd()
        temp_path = currentdirectory + nfile
        nfile = open(temp_path, 'w')
        nfile.write('')
        nfile.close()
        if opsys == 'Windows':
            dst = address
            print dst
            shutil.move(nfile,dst)
        else:
            shutil.move(nfile,address)
            
            
            
        
         
        
        

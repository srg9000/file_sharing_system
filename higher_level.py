#!/usr/bin/python
#-*- coding: utf-8 -*-

from node import node
#from request import request
import os.path

class higher_level():
    '''Node with privileges to remove requests''' 
    #node_list_hl=[]
    def __init__(self):
        node.__init__(self)
        #request.__init__(self)
        #higher_level.node_list_hl.append((self.id,self.ip_address))
        pass
    
    def choose_req(self ):
        #print(request.request_list)        
        l=input("Enter request number,('0' to do nothing and exit): ")
        if l[0]=='0':
            return None,None
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        print(files)
        path=input("Enter full path:")
        path=os.path.abspath(path)
        while(os.path.isfile(path)==False):
            input("Incorrect path! Input full path again:")
        #request.find(self.ip_address,l[1],path)
        return path,l[0]
    
#    def remove_req(self,req_num):
#        for i in request.request_list:
#          if i[2]==req_num:
#            request.request_list.remove(i)
#            break
    
    def __str__(self):
      return str(self.ip_address)
    

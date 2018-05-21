#!/usr/bin/python
#-*- coding: utf-8 -*-

from node import node
from request import request
import os.path
class lower_level(node,request):
    node_list_hl=[]
    def __init__(self):
        node.__init__(self)
        lower_level.node_list_ll.append((self.id,self.ip_address))
        pass
    
    def choose_req(self ):
        print(request().request_list)        
        l=input("Enter node id and request number,('0 0' to do nothing and exit): ").split()
        if l[0]==l[1]=='0':
            return None
        path=input("Enter full path:")
        path=os.path.abspath(path)
        while(not os.path.exists(path)):
            input("Incorrect path! Input full path again:")
        request.find(self.ip_address,l[1],path)

    def __str__(self):
      return str(self.id)+'::'+str(self.ip_address)
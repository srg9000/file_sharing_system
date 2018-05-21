#!/usr/bin/python
#-*- coding: utf-8 -*-

#import ipgetter
#from request import request
from link import link
import socket
class node(object):
    #node_id=0
   # node_list=[]#(id,ip,server created,client created)
    def __init__(self):
       
        self.ip_address = ([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0])
        #self.ip_address=socket.gethostname()
        #self.ip_address=socket.gethostbyname(socket.getfqdn())
        
        
        #self.id = node.node_id+1
        #self.finds = None
        #self.list_of_clients = []
        #self.list_of_servers=[]
        #node.node_list.append((self.id,self.ip_address,0,0))
        #node.node_id+=1
        
#    def create_request(self,req):
#        request.add(self.id,self.ip_address,req)

    def __str__(self):
      return str(self.id)+'::'+str(self.ip_address)
    

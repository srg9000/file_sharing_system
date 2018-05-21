#!/usr/bin/python
#-*- coding: utf-8 -*-
#from link import link
class request(object):
    request_list=[]
    req_no=1
    def __init__(self):
        self.node_list = []

    def find(self,ip_address_ser,req_num,path ):
        for i in request.request_list:
          if i[1]==req_num:
            k=i[2]
            #link.connect(ip_address_ser,i[1],path)
            request.request_list.remove(i)
            return k
        print("No such request number")
        return

    def add(self,ip_address,req):
        request.request_list.append((ip_address,str(request.req_no),req))
        request.req_no+=1
        
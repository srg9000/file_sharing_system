# -*- coding: utf-8 -*-
"""
Created on Sun May  6 23:38:37 2018

@author: srg
"""

#!/usr/bin/python
#-*- coding: utf-8 -*-
import socket
#from sendfile import sendfile
import os.path

class link(object):
  
    def __init__(self):
        #request.__init__(self)
        self.connected_by = []

#    def connect(ip1_ser, ip2_cli,path):
#        link.create_server(ip1_ser,path)
#        link.create_client(ip1_ser)
       

    
    def create_server(self,ip,path ): #ip is of the server
        connection_list = []
        print(ip)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((ip, 12345))
        print("server created")
        connection_list.append(sock)
        sock.listen(1)
        #offset = 0
        file = open(path, "rb")
        print("file opened")
        print("waiting for connection...")
        conn, addr = sock.accept()
        print ('New connection from %s:%d' % (addr[0], addr[1]))
        print("accepted connection")
        connection_list.append(conn)  
        while True:
         
            conn.send(str("Start").encode()) # THIS CAUSES BROKEN PIPE ERROR
            chunk = file.read(65536)
            print("chunk read")
            if not chunk:
                break  # EOF
                file.close()
                conn.close()
            #conn.send(str(chunk).encode())
            conn.send(chunk)
            print("chunk sent")
        #conn.send(str("ENDED").encode())
        print("Transfer complete")
        conn.close()

        
                
    def create_client(self,ip,file ): #ip of server
        print(ip)
        print("going to download",str(file))
        try:
            client=socket.create_connection((ip, 12345 ))
        except:
            client=socket.create_connection((ip, 12346 ))
        print("client created")
        dat=client.recv(4096)
        with open(str(file), 'wb') as f:
          socket_list = [client]
          print("file opened")
          
          while True:
               print("started")
               data=client.recv(65536)
               dat=data
               if  not data:
                       break
               else:
                   f.write(data)
                   print("recieved data")
               
          
          print("Transfer complete")
        f.close()
        #time.sleep(5)
        client.close()

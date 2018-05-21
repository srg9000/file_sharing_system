#from node import node
import socket,select,sys,time
from higher_level import higher_level
#from lower_level import lower_level
from link import link
class main(object):
    def __init__(self):
        self.server_ip='192.168.43.20'
        self.port=12349
        self.c=socket.create_connection((self.server_ip,self.port))
        self.socket_list=[sys.stdin,self.c]
    def login(self):
      usid=input("Enter user id:")
      psw=input("Enter password:")
      #self.c=socket.create_connection((self.server_ip,self.port))
      
      self.c.send(usid.encode('utf-8'))
      rec=self.c.recv(1024).decode()
      if rec == '0':
          self.c.send(psw.encode('utf-8'))
          rec2=self.c.recv(1024).decode()
          if rec2=='0':
              print("Login successful")
              return True
          else:
              print("incorrect usid,psw combination or check network connection.")
              return False
      else:
              print("Check network connection.")
              return False
    def main2(self):
     if(self.login()):
        new=higher_level()
        while(1):
            #read_sockets,write_sockets,error_sockets = select.select(self.socket_list,[],[])
            k=int(input("Select an operation\n1.See details\n2.Create a request\n3.Choose request to fulfill\n4.Exit\n"))
            if k==1:
                print(new)
            elif k==2:
                req=input("What is your request?\n")
                stri="create request"
                self.c.send(stri.encode('utf-8'))
                rec=str(self.c.recv(4096))
                if rec[2:len(rec)-1]=='0':
                    self.c.send(req.encode('utf-8'))
                    print("request sent,waiting to find sender")
                    ip=self.c.recv(4096).decode()
                    print("recieved something")
                    fn=ip.split()[1]
                    ip=ip.split()[0]
                    fn="rec"+fn
                    print("Found sender, downloading...")
                    lin1=link()
                    #time.sleep(10)
                    lin1.create_client(ip,fn)
                else:
                    print("network error, try again")
            elif k==3:
                stri="show list"
                self.c.send(stri.encode('utf-8'))
                lst=str(self.c.recv(4096))
                print(lst[2:len(lst)-1])
                path,req_num=new.choose_req()
                if path!=None:
                    stri="choosing request"
                    self.c.send(stri.encode('utf-8'))
                    rec=str(self.c.recv(4096))
                    if rec[2:len(rec)-1]=='0':
                        self.c.send(path.encode('utf-8'))
                    rec=str(self.c.recv(4096))
                    if rec[2:len(rec)-1]=='0':
                        self.c.send(str(req_num).encode('utf-8'))    
                    rec=self.c.recv(4096).decode('utf-8')
                    print(rec)
                    if(rec=='1'):
                        print("other user is not active")
                    elif(rec=='0'):
                        lin=link()
                        self.c.send(str('true').encode())
                        print("sent conf")
                        lin.create_server(new.ip_address,path)
                        
            elif k==4:
                self.c.send(str("close").encode())
                #self.c.shutdown(self.c.SHUT_RDWR)
                self.c.close()
                break

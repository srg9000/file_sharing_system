import hashlib,binascii,os,socket,_thread,threading,select,sys,time
#from node import node
from request import request
class server(object):
    def __init__(self):
        self.salt=os.urandom(16)
        self.uid=[]
        self.list_of_conns=[]
        self.lock=threading.Lock()
        #thread=threading.Thread(target=self.main2)
        #thread.start()
    def encrypt(self,psw):
        #l=hashlib.pbkdf2_hmac('sha512',psw.encode(),self.salt,100000,dklen=15)
        l=psw
        return l
#    def pad(self,psw):
#        return psw+str((8-len(psw.encode())%8)*'s')
    def update_dict(self,usid,psw):
        self.uid.append([usid,str(self.encrypt(psw)),0])
    def login(self,usid,psw):
        if( [usid,self.encrypt(self.pad(psw)),0] in self.uid):
            return True
        else:
            print ("Wrong combination")
            return False
    def logout(self,usid):
            for i in self.uid:
                if i[0]==str(usid):
                    i[2]=0
        
    def activate(self,usid):
        for i in self.uid:
            if i[0]==str(usid):
                i[2]=1
    def ui(self):
        global reqt
        reqt=request()
        while(1):
            _=input("Enter 1 to update, 2 to read list of connections,3 to get list of user id's,4 to start server")
            if(_=='1'):
                filename=input("input file name:")
                print("Updating list...")
                with open(filename,"r+") as f:
                    for n in f:
                        for i in range(len(n)-1,0,-1):
                            #print(i,' ',n[i])
                            if n[i]==' ':
                                usid=n[:i]
                                psw=n[i+1:len(n)-1]
                                self.update_dict(usid,psw)
                                break
                    f.close()
                self.update_dict('123','123')        
            elif(_=='2'):
                print(self.list_of_conns)
            elif (_=='3'):
                print(self.uid)
            elif(_=='4'):
                break
    def main2(self):
        host=([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0])             
        print(host)
        #host='127.0.0.1'
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         
        port = 12349
        #s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        count=0
        while(1):
            
            try:
                s.bind((host, port))   
                break
            except:
                print(count)
                count+=1
        s.listen(150)
        while(1):
                
                c,addr=s.accept()
                self.list_of_conns.append([c,addr])
                with self.lock:
                    _thread.start_new_thread(self.comm,(c,addr))
                    print("started new thread")
                    print(self.list_of_conns)
    def comm(self,c,addr):    
            
            usid=str(c.recv(4096))
            usid=usid[2:len(usid)-1]
            try:
                c.send(str(0).encode('utf-8'))
            except:
                c.send(str(1).encode())
            psw=str(c.recv(4096))
            psw=psw[2:len(psw)-1]
            if([usid,str(self.encrypt(psw)),0] in self.uid):
                self.activate(usid)
                c.send(str(0).encode('utf-8'))
            else:
                try:
                    c.send(str(1).encode('utf-8'))
                except:
                    c.send(str(0).encode('utf-8'))
            while(1):
                req=str(c.recv(4096))
                req=req[2:len(req)-1]
                if req=="show list":
                    c.send(str("List of requests="+str(reqt.request_list)).encode('utf-8'))
                elif req=="create request":
                    try:
                        c.send(str(0).encode('utf-8'))
                    except:
                        c.send(str(1).encode('utf-8'))
                    reques=str(c.recv(4096))
                    reqt.add(reques[2:len(reques)-1],addr[0])
                elif req=="choosing request":
                    try:
                        c.send(str(0).encode('utf-8'))            
                    except:
                        c.send(str(1).encode('utf-8'))
                    path=str(c.recv(4096))
                    path=path[2:len(path)-1]
                    for i in range(len(path)-1,0,-1):
                        if path[i]=='/' or path[i]=='\\'  :
                            filename=path[i+1:]
                            break
                    c.send(str(0).encode('utf-8'))            
                    reqnum=str(c.recv(4096))
                    reqnum=reqnum[2:len(reqnum)-1]
                    cli_ip=str(reqt.find(addr[0],reqnum,path))
                    m=0
                    for i in self.list_of_conns:
                        if i[1][0]==cli_ip:
                            k=i[0]
                            m=1
                            break
                    print(self.list_of_conns[1][1][0])
                    if m==0:
                        c.send(str(1).encode('utf-8'))
                    else:
                        c.send(str(0).encode('utf-8'))
                        print("asking for conf")
                        conf=c.recv(4096).decode('utf-8')
                        print("conf recieved")
                        if conf=='true':
                            k.send(str(addr[0]+' '+filename).encode())
                            print("sent to k")
                            time.sleep(30)
                elif req=="close":
                    #c.shutdown(c.SHUT_RDWR)
                    c.close()
                    self.list_of_conns.remove([c,addr])
                    self.logout(usid)
                
                    
            
            
            

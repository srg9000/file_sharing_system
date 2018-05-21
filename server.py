#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from _server import server
import threading,_thread
import os
import subprocess
import sys
#import tempfile
#from Queue import Queue, Empty
#from threading import Thread
#def launch_entry_console():
#    if os.name == 'nt': # or use sys.platform for more specific names
#        console = ['cmd.exe', '/c'] # or something
#    else:
#        console = ['xterm', '-e'] # specify your favorite terminal
#                                  # emulator here
#
#    cmd =t2

#    return subprocess.Popen(console + cmd)

#class myThread (threading.Thread):
#   def __init__(self, threadID, name, counter):
#      threading.Thread.__init__(self)
#      self.threadID = threadID
#      self.name = name
#      self.counter = counter
#   def run(self):
#      print ("Starting " + self.name)
#      # Get lock to synchronize threads
#      threadLock.acquire()
#      # Free lock to release next thread
#      threadLock.release()
#threadLock = threading.Lock()\

#print_lock=threading.Lock()
one=server()
one.ui()
one.main2()
#one.update_dict('123',one.pad('123'))
#t1=_thread.start_new_thread(target= one.main2())
#with print_lock:
#	t1=threading.Thread(target= one.ui())
#    launch_entry_console()
    
#threading.Thread.start(target= one.main2())
#t1.start()
#t2.start()

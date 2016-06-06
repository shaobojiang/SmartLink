'''

@author: peter.jiang
'''
import SocketServer
import socket
from SocketServer import TCPServer, BaseRequestHandler
import traceback
from multiprocessing import Process, Queue 

def socketInit():
    print "Run socketInit"
    p = Process(target=socketServerRun)
    p.start()



def socketServerRun():
    print "Run socket"
   
    ip_port = ('127.0.0.1',9999)
    server = SocketServer.ThreadingTCPServer(ip_port,MyBaseRequestHandler)
    server.serve_forever()




class MyBaseRequestHandler(BaseRequestHandler):
    """

    """
    def handle(self):

        while True:

            try:

                data = self.request.recv(1024).strip()
                

                print "receive from (%r):%r" % (self.client_address, data)
                

                self.request.sendall(data.upper())
            except:
                traceback.print_exc()
                break
    
        


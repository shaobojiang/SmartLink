'''

@author: peter.jiang
'''
import SocketServer
import socket
from SocketServer import TCPServer, BaseRequestHandler
import traceback
from multiprocessing import Process, Queue 

ip_port = ('127.0.0.1',9999)
    
def socketInit():    
    print "Run socketInit"
    p = Process(target=socketServerRun)
    p.start()
        



def socketServerRun():
    print "Run socket" 
    try:
        server = SocketServer.ThreadingTCPServer(ip_port,MyBaseRequestHandler)
        server.serve_forever()
    except Exception,ex:
        print Exception,":", ex
        return




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
    
        


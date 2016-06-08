'''

@author: peter.jiang
'''
import django
django.setup()
import SocketServer
import socket
from SocketServer import TCPServer, BaseRequestHandler,BaseServer
import traceback
from multiprocessing import Process
from Queue import Queue
from threading import Thread
from time import sleep


ip_port = ('127.0.0.1',9999)
      
q = Queue()


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

def sendSocketMessage(message):
    from MyHttpServer.models import CMMessage
    ob   = CMMessage()
    ob.message = message
    ob.save()
    pass

    
def sockedSend(request):
    while True:
        message = q.get()
        print message
        if not message:
            request.sendall(message)
            
            
class MessageSendHandler(Thread):
    dict = {}
    def __init__(self,socket,name):
        Thread.__init__(self)
        self.socket = socket
        self.name =name
        
    def run(self):
        from MyHttpServer.models import CMMessage
        while True:
            try:
                message = CMMessage.objects.get(code="CMD")      
                
                if message:
                    print  "message ="+message.message
                    self.socket.sendall(message.message)
                    message.delete()
            except Exception,ex:
                pass
                
            sleep(0.1)
                    
            
    
class MyBaseRequestHandler(BaseRequestHandler):
    """

    """
    def handle(self):

        while True:

            try:

                data = self.request.recv(1024).strip()
               
                print "receive from (%r):%r" % (self.client_address, data)    
                            
                sockedrequest = self.request
                newThread = MessageSendHandler(sockedrequest,self.client_address)
                newThread.daemon = True
                newThread.start()
                self.request.sendall(data.upper())

                #t = threading.Thread(target=sockedSend(self.request))
                #t.start()
            except:
                traceback.print_exc()
                break
    
        


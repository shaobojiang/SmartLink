'''

@author: peter.jiang
'''
import SocketServer

class  MySocketServer(SocketServer.BaseRequestHandler):
    
    def setup(self):
        print "MySocketServer"
        pass

    def handle(self):
        print self.request,self.client_address,self.server
        #self.request = socket
        #

    def finish(self):
        pass
    
    
    



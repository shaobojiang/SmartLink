'''

@author: peter.jiang
'''
from SocketServer import TCPServer, BaseRequestHandler
import traceback

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
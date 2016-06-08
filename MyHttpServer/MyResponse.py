'''

@author: PeterPKU
'''

from django.http.response import HttpResponse
import simplejson

def getSucessResponse():
    response = {}
    response['status']=200
    return response

def getErrorResponse(code):
    response = {}
    response['status']=201
    error = {}        
    error['code']=code
                
    if code == 101:
        error['message']="invalid username or password"    
    elif code == 102:
        error['message']="username already exsit"
            
    response['error']=error
        
    return response
     
def JSONResponse(result):
    return HttpResponse(simplejson.dumps(result),content_type="application/json")


def JSONError(code):
    return HttpResponse(simplejson.dumps(getErrorResponse(code)),content_type="application/json")
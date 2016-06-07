from django.shortcuts import render
from httpServer.models import User
from django.http.response import HttpResponse
import json
import simplejson
from httpServer.MyResponse import getErrorResponse,getSucessResponse,JSONResponse,JSONError

# Create your views here.

def register(request):
    struct = {}
    if request.method =='POST':
        struct = simplejson.loads(request.body)

    user_name =struct['username']
    password = struct['password']

    if len(user_name)==0 or  len(password)==0:
        return JSONError(101)
  
    user = User.objects.filter(username=user_name)  
    if user:
        return JSONError(102)     
    
    user = User()
    user.username =user_name
    user.password=password
    user.save()
    
    result = getSucessResponse()
    result['username']=user_name
    result['password']=password
    return JSONResponse(result)

  
def login(request):
    struct = {}
    if request.method =='POST':
        struct = simplejson.loads(request.body)
        #req = simplejson.loads(request.body,encoding='utf-8')
    user_name =struct['username']
    pass_word = struct['password']

    if len(user_name)==0 or  len(pass_word)==0:
        return JSONError(101)
  
    user = User.objects.filter(username=user_name,password=pass_word)  
    if not user:
        return JSONError(101)     
    
    result = getSucessResponse()
    result['username']=user_name
    result['password']=pass_word
    return JSONResponse(result)

from SocketServer import TCPServer
from MySocketServer import MyBaseRequestHandler

def users(request):
    users=User.objects.all()
    userdict = [ob.toDict() for ob in users]
    result = getSucessResponse()
    result['data'] = userdict
    return JSONResponse(result)

    
    
from django.shortcuts import render
from MyHttpServer.models import User,CMMessage
from django.http.response import HttpResponse
import json
import simplejson
from MyHttpServer.MyResponse import getErrorResponse,getSucessResponse,JSONResponse,JSONError

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


def users(request):
    users=User.objects.all()
    userdict = [ob.toDict() for ob in users]
    result = getSucessResponse()
    result['data'] = userdict
    return JSONResponse(result)


def sendMessage(request):
    struct = {}
    if request.method =='POST':
        struct = simplejson.loads(request.body)

    message =struct['message']
    code = struct['code']
    if len(message)==0:
        return JSONError(101)
    ob = CMMessage()
    ob.message = message
    ob.code=code
    ob.save()
   # sendSocketMessage(message)
    
    result = getSucessResponse()
    return JSONResponse(result)

    
    
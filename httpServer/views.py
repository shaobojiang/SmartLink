from django.shortcuts import render
from httpServer.models import User
from django.http.response import HttpResponse
import json
import simplejson
from httpServer.MyResponse import getErrorResponse,getSucessResponse


# Create your views here.

def register(request):
    struct = {}
    if request.method =='POST':
        struct = simplejson.loads(request.body)
        #req = simplejson.loads(request.body,encoding='utf-8')
    user_name =struct['username']
    password = struct['password']

    if len(user_name)==0 or  len(password)==0:
        return HttpResponse(simplejson.dumps(getErrorResponse(101)),content_type="application/json")
  
    user = User.objects.filter(username=user_name)  
    if user:
        return HttpResponse(simplejson.dumps(getErrorResponse(102)),content_type="application/json")     
    
    user = User()
    user.username =user_name
    user.password=password
    user.save()
    
    result = getSucessResponse()
    result['username']=user_name
    result['password']=password
    return HttpResponse(simplejson.dumps(result),content_type="application/json")


def login(request):
    struct = {}
    if request.method =='POST':
        struct = simplejson.loads(request.body)
        #req = simplejson.loads(request.body,encoding='utf-8')
    user_name =struct['username']
    pass_word = struct['password']

    if len(user_name)==0 or  len(pass_word)==0:
        return HttpResponse(simplejson.dumps(getErrorResponse(101)),content_type="application/json")
  
    user = User.objects.filter(username=user_name,password=pass_word)  
    if not user:
        return HttpResponse(simplejson.dumps(getErrorResponse(101)),content_type="application/json")     
    
    result = getSucessResponse()
    result['username']=user_name
    result['password']=pass_word
    return HttpResponse(simplejson.dumps(result),content_type="application/json")


def users(request):
    users=User.objects.all()
    userdict = [ob.toDict() for ob in users]
    result = getSucessResponse()
    result['data'] = userdict
    return HttpResponse(simplejson.dumps(result),content_type="application/json")

    
    
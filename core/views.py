from django.shortcuts import render
from django.contrib.auth import authenticate 
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User

import json
from core.models import *
from django.core.serializers.json import DjangoJSONEncoder
# Create your views here.
def signin(request):
    response_data ={}
    rp = request.POST.get
    print(rp)
    # logout(request)
    if request.POST:
        is_user = False
        try:

            if rp('password'):

                user = WebsiteUser.objects.get(user_id=rp('username'))
                if user.user_password == rp('password'):
                    print(user)
                    is_user = True
            else:
                user = WebsiteUser.objects.get(user_id=rp('username'))
                response_data['user'] = user.user_type
                response_data['user_id'] = user.user_id

                
                response_data['status'] = "success"
                return HttpResponse(json.dumps(response_data), content_type='application/json') 
        
            if is_user:
                response_data['user'] = user.user_type
                response_data['password_verified'] = True
                response_data['status'] = "success"
                print(response_data)
                return HttpResponse(json.dumps(response_data), content_type='application/json')    
        except:
            response_data['message'] = 'User ID or Password is Wrong Please Try Again'
            response_data['status'] = 'error'
            return HttpResponse(json.dumps(response_data,cls=DjangoJSONEncoder), content_type='application/json')

    return render(request,'common/signin.html')


def table(request):
    rp = request.POST.get
    print(rp)
    response_data ={}
    if request.POST:
        if rp('type') == "delete":

            user = WebsiteUser.objects.get(id=rp('id')).delete()
        if rp('type') == "add":
            try:
                user = WebsiteUser.objects.create(user_id=rp('user_id'),user_name=rp('user_name'),user_last_name=rp('user_last_name'),user_address=rp('user_address'),user_phone=rp('user_phone'),user_status=rp('user_status'),user_type="P",user_password=rp('password'))
                response_data['status'] = "success"

            except:
                response_data['status'] = "failed"
                response_data['message'] = "Patient with Same User Id Exists"

            return HttpResponse(json.dumps(response_data,cls=DjangoJSONEncoder), content_type='application/json')

    c = {"patients":WebsiteUser.objects.filter(user_type="P")}
    
    return render(request,'common/table.html',c)

def blank(request):
    return render(request,'common/blank.html',)

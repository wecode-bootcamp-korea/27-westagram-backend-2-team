import json, re

from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

from .models import User

class UserView(View):
    def post(self, request):
        data            = json.loads(request.body)
        regexr_email    = re.compile('[a-zA-Z0-9]+\.?\w*@\w+[.]?\w*[.]+\w{2,3}')
        regexr_password = re.compile('(?=.*[A-Za-z])(?=.*\d)(?=.*[~!@#$^&*()+|=])[A-Za-z\d~!@#$%^&*()+|=]{8,}')

        try:
            # email과 password가 비어있는 경우
            if data['email'] == '' or data['password'] == '':
                return JsonResponse({'message':'Email or Password is Blank'}, status = 400)
            # email 중복된 경우    
            elif data['email'] in [i.email for i in User.objects.all()]:
                raise JsonResponse({'message' : 'Email Reduplication'}, status=400)
            # email과 password가 정규식과 불일치한 경우
            elif regexr_email.match(data['email']) is None or regexr_password.match(data['password']) is None:
                raise ValueError

        except ValueError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)

        else:
            User.objects.create(
                name        = data['name'],
                email       = data['email'],
                password    = data['password'],
                address     = data['address'],
                information = data['information']
            )
            return JsonResponse({'message':'SUCESS'},status=201)
import json, bcrypt, jwt, re

from django.views import View
from django.http import JsonResponse, HttpResponse

from .models import User
from my_settings import SECRET_KEY, DATABASES

class SignupView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            name         = data['name']
            email        = data['email']
            password     = data['password']
            phone_number = data['phone_number']
            information  = data['information']

            if User.objects.filter(email=email).exists():
                return JsonResponse({'message' : 'ALREADY_EXISTS'}, status = 400)

            regex_email    = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9_-]+\.[a-zA-Z0-9-.]+$'
            regex_password = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}'

            if re.match(regex_email, email) is None:
                return JsonResponse({'message' : 'INVALID_EMAIL'}, status = 400)
            if re.match(regex_password, password) is None:
                return JsonResponse({'message' : 'INVALID_PASSWORD'}, status = 400)

            #password       = data['password'].encode('utf-8')
            #password_crypt = bcrypt.hashpw(password, bcrypt.gensalt()).decode('utf-8')

            User.objects.create(
                name         = name, 
                email        = email, 
                password     = password, 
                phone_number = phone_number,
                information  = information
            )
            return JsonResponse({'message' : 'SUCCESS!'}, status=201)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)

class SigninView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            if (data["email"] == "") or (data["password"] == ""):
                return JsonResponse({'message': 'KEY_ERROR'}, status=400)
            
            if not User.objects.filter(email=data['email']).exists():
                return JsonResponse({'message': 'INVALID_EMAIL'}, status=401)
    
            if not User.objects.get(password=data['password']):
               return JsonResponse({'massage': 'INVALID_PASSWORD'}, status=401)

            if User.objects.filter(email=data['email']) and User.objects.filter(password=data['password']):
                return JsonResponse({'message': 'SUCCESS'}, status=200)

        except KeyError:
            return JsonResponse({'massage': 'KEY_ERROR'}, status=400)

        
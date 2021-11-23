import json

from django.views     import View
from django.http      import JsonResponse, HttpResponse

from .models          import User
from my_settings      import SECRET_KEY, DATABASES
from .validation      import regex_match

class SignupView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            name         = data['name']
            email        = data['email']
            password     = data['password']
            phone_number = data['phone_number']
            information  = data.get('information', None)
            
            regex_match(
                email,
                password,
            )

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
            
            if not User.objects.filter(email=data['email']).exists():
                return JsonResponse({'message': 'INVALID_EMAIL'}, status=401)
    
            if not User.objects.filter(password=data['password']).exists():
               return JsonResponse({'massage': 'INVALID_PASSWORD'}, status=401)

            if User.objects.filter(email=data['email']) and User.objects.filter(password=data['password']).exists():
                return JsonResponse({'message': 'SUCCESS'}, status=200)

        except KeyError:
            return JsonResponse({'massage': 'KEY_ERROR'}, status=400)
        except User.DoesNotExist:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=401)


        
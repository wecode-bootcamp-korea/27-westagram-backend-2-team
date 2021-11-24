import json, bcrypt, jwt

from django.views     import View
from django.http      import JsonResponse, HttpResponse

from .models          import User
from my_settings      import SECRET_KEY, DATABASES
from .validation      import validate_email, validate_password

class SignupView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            name         = data['name']
            email        = data['email']
            password     = data['password']
            phone_number = data['phone_number']
            information  = data.get('information', None)
            
            validate_email(email)
            validate_password(password)

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            User.objects.create(
                name         = name, 
                email        = email, 
                password     = hashed_password, 
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

            if User.objects.filter(email=data['email']).exists():
                if bcrypt.checkpw(data['password'].encode('utf-8'), User.objects.get(email=data['email']).password.encode('utf-8')):
                    token = jwt.encode({'id' : User.objects.get(email=data['email']).id},SECRET_KEY, algorithm='HS256')
                    return JsonResponse({'MESSAGE':'SUCCESS', 'TOKEN' : token}, status=200)
    
            return JsonResponse({'massage': 'INVALID_USER'}, status=401)

        except KeyError:
            return JsonResponse({'massage': 'KEY_ERROR'}, status=400)
        except User.DoesNotExist:
            return JsonResponse({'message': 'INVALID_USER'}, status=401)

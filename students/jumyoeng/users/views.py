import json

from django.http import JsonResponse
from django.views import View

from users.models import User
from users.my_lib.validation import email_validation, password_validation

class SignUpView(View) :
    def post(self, request):
        try :
            data = json.loads(request.body)

            name         = data['name']
            email        = data['email']
            password     = data['password']
            phone_number = data.get('phone_number')
            description  = data['description']

            if User.objects.filter(email=email) :
                return JsonResponse({'MESSAGE': 'EMAIL_DUPLICATE'}, status=400)

            if not email_validation(email) :
                return JsonResponse({'MESSAGE': 'EMAIL_INVALID'}, status=400)

            if not password_validation(password) :
                return JsonResponse({'MESSAGE': 'PASSWORD_INVALID'}, status=400)

            User.objects.create(
                name         = name,
                email        = email,
                password     = password,
                phone_number = phone_number,
                description  = description
            )
            return JsonResponse({'MESSAGE': 'CREATED'}, status=201)

        except KeyError :
            return  JsonResponse({'MESSAGE': 'KEY_ERROR'}, status=400)

class SignInView(View) :
    def post(self, request) :
        try :
            data = json.loads(request.body)

            if User.objects.filter(email=data['email'], password = data['password']).exists() :
                return JsonResponse({'MESSAGE': 'SUCCESS'}, status=200)
            return JsonResponse({'MESSAGE': 'INVALID_USER'}, status=401)

        except KeyError :
            return  JsonResponse({'MESSAGE': 'KEY_ERROR'}, status=400)
import json
from django.core.exceptions import ValidationError
from django.db.models.base import Model

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

            email_validation(email)
            password_validation(password)

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
        except ValidationError :
            return  JsonResponse({'MESSAGE': 'Validation_ERROR'}, status=402)
        except Model.DoesNotExist :
            return JsonResponse({'MESSAGE': 'MODEL_DOES_NOT_EXIST'}, status=400)

class SignInView(View) :
    def post(self, request) :
        try :
            data = json.loads(request.body)

            if User.objects.filter(email=data['email'], password = data['password']).exists() :
                return JsonResponse({'MESSAGE': 'SUCCESS'}, status=200)
            return JsonResponse({'MESSAGE': 'INVALID_USER'}, status=401)

        except KeyError :
            return  JsonResponse({'MESSAGE': 'KEY_ERROR'}, status=400)
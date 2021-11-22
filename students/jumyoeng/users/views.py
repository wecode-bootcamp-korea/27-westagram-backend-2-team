import json

from django.http import JsonResponse
from django.views import View

from users.models import User
from users.my_lib.validation import email_validation, password_validation

class SignUpView(View) :
    def post(self, request):
        try :
            data = json.loads(request.body)

            if User.objects.filter(email=data['email']) :
                return JsonResponse({'MESSAGE': 'EMAIL_DUPLICATE'}, status=400)

            if not email_validation(data['email']) :
                return JsonResponse({'MESSAGE': 'EMAIL_INVALID'}, status=400)

            if not password_validation(data['password']) :
                return JsonResponse({'MESSAGE': 'PASSWORD_INVALID'}, status=400)

            User.objects.create(
            name         = data['name'],
            email        = data['email'],
            password     = data['password'],
            phone_number = None if data.get('phone') is None else data['phone'],
            description  = data['descr'],
            )
            return JsonResponse({'MESSAGE': 'CREATED'}, status=201)

        except KeyError:
            return  JsonResponse({'MESSAGE': 'KEY_ERROR'}, status=400)

        except Exception as e :
            print(e)
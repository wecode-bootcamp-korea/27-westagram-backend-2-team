import json,bcrypt

from django.http            import JsonResponse, HttpResponse
from django.views           import View
from django.core.exceptions import ValidationError

from .models      import User
from my_settings  import DATABASES, SECRET_KEY
from .validation  import validate_email, validate_password

class SignupView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            name         = data['name']
            email        = data['email']
            password     = data['password']
            phone_number = data['phone_number']
            address      = data.get('address', '')
            job          = data.get('job', '')

            validate_email(email)
            validate_password(password)

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            User.objects.create(
                name         = name,
                email        = email,
                password     = hashed_password,
                phone_number = phone_number,
                address      = address,
                job          = job
            )
            return JsonResponse({'MESSAGE' : 'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({'MESSAGE' : 'KEY_ERROR'}, status=400)
        except ValidationError:
            return JsonResponse({'MESSAGE':'VALIDATION_ERROR'}, status=400)

class SigninView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            if not User.objects.filter(email=data['email'], password=data['password']).exists():
                return JsonResponse({'MESSAGE' : 'INVALID_USER'}, status=401)

            return JsonResponse({'MESSAGE' : 'SUCCESS'}, status=200)

        except KeyError:
            return JsonResponse({'MESSAGE' : 'KEY_ERROR'}, status=400)
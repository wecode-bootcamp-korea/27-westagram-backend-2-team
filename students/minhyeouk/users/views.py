import json, re

from django.http  import JsonResponse, HttpResponse
from django.views import View

from .models      import User
from my_settings  import DATABASES, SECRET_KEY

class SignupView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            name         = data['name']
            email        = data['email']
            password     = data['password']
            phone_number = data['phone_number']
            address      = data['address']
            job          = data['job']

            email_regex    = '(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
            password_regex = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$'
        
            if User.objects.filter(email=email).exists():
                return JsonResponse({'MESSAGE' : 'ALREADY_EXISTS'}, status=400)

            if not re.match(email_regex, email):
                return JsonResponse({'MESSAGE' : 'INVALID_EMAIL'}, status=400)
            if not re.match(password_regex, password):
                return JsonResponse({'MESSAGE' : 'INVALID_PASSWORD'}, status=400)
            
            User.objects.create(
                name         = name,
                email        = email,
                password     = password,
                phone_number = phone_number,
                address      = address,
                job          = job
            )
            return JsonResponse({'MESSAGE' : 'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({'MESSAGE' : 'KEY_ERROR'}, status=400)
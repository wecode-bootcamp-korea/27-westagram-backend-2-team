import re, json

from django.http.response   import JsonResponse
from django.views           import View
from django.core.exceptions import ValidationError

from .models                import User

class SignUpView(View):
    def post(self, request):
        data         = json.loads(request.body)
        
        try:
            name         = data["name"]
            email        = data['email']
            password     = data["password"]
            phone_number = data["phone_number"]
            birthday     = data.get('birthday', None)
            gender       = data.get('gender', None)           
            
            regex_email    = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9_-]+\.[a-zA정규식-Z0-9-.]+$'
            regex_password = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}'
            regex_phone    = '/^01(?:0|1|[6-9])[.-]?(\\d{3}|\\d{4})[.-]?(\\d{4})$/'
                            
            
            if User.objects.filter(email=email).exists():
                return JsonResponse({"message" : "EMAIL_ALREADY_EXISTS"}, status=400)

            if not re.match(regex_email, email):
                return JsonResponse({"message": "EMAIL_ERROR"}, status=400)

            if not re.match(regex_password, password):
                return JsonResponse({"message": "PASSWORD_ERROR"}, status=400)
            
            if not re.match(regex_phone, phone_number):
                return JsonResponse({'message': 'INVALID_CONTACT'}, status=400)

            User.objects.create(
                name         = name,
                email        = email,
                password     = password,
                phone_number = phone_number,
                birthday     = birthday,
                gender       = gender,
                )
            return JsonResponse({"message": "Success"}, status = 201)
        
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
 
class SignInView(View):
    def post(self, request):
        try:
            data      = json.loads(request.body)
            email     = data["email"]
            password  = data["password"]
            
            if not User.objects.filter(email=email, password=password).exists():
                return JsonResponse({"message":"INVALID_USER"}, status=401)
            
            return JsonResponse({"message" : "SUCCESS"}, status=200)
        
        except KeyError:
              return JsonResponse({"message" : "KEY_ERROR"}, status=400)
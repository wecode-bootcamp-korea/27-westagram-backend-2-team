import json, re
 
from django.views           import View
from django.http            import JsonResponse
from django.core.exceptions import ValidationError
from django.db.models       import Q

from .models                import User
# from .validation            import Is_validate

class SignupView(View):
    def post(self, request):
        data            = json.loads(request.body)
        regexr_email    = '[a-zA-Z0-9]+\.?\w*@\w+[.]?\w*[.]+\w{2,3}'
        regexr_password = '(?=.*[A-Za-z])(?=.*\d)(?=.*[~!@#$^&*()+|=])[A-Za-z\d~!@#$%^&*()+|=]{8,}'

        try:
            if data.get('email') is None:
                raise KeyError('Email_is_Blank')
            if data.get('password') is None:
                raise KeyError('Password_is_Blank')
            if not re.match(regexr_email, data['email']) or not re.match(regexr_password,data['password']):
                raise ValidationError('Invalid_Key')
            if User.objects.filter(email = data['email']).exists():
                return JsonResponse({'message':'DUPLICATED_EMAIL'}, status=400)

            User.objects.create(
                name        = data['name'],
                email       = data['email'],
                password    = data['password'],
                address     = data['address'],
                information = data.get('information')
            )
            return JsonResponse({'message':'SUCESS'},status=201)

        except ValidationError as e:
            return JsonResponse({'message': e.message},status=400)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)
    
class SigninView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            if User.objects.filter(Q(email = data['email']) & Q(password=data['password'])).exists():
                return JsonResponse({'message':'SUCCESS'},status = 200)

            return JsonResponse({'message':'INVALID_USER'}, status = 401)

        except User.DoesNotExist:
            return JsonResponse({'message':'INVALID_USER'}, status = 401)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status = 400)
import json
 
from django.views           import View
from django.http            import JsonResponse
from django.core.exceptions import ValidationError

from .models                import User
from .validator             import *

class SignupView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            is_blank(data.get('email'), data.get('password'))
            is_regexr(data['email'], data['password'])
            is_duplicated(data['email'])
            
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
        try:
            data = json.loads(request.body)
            user_pwd = User.objects.get(email=data['email']).password
            
            if user_pwd != data['password']:
                raise ValidationError('INVALID_USER')

            return JsonResponse({'message': 'SUCCESS'})
        
        except User.DoesNotExist:
            return JsonResponse({'message':'INVALID_USER'}, status=401)
        except ValidationError as e:
            return JsonResponse({'message' : e.message}, status = 401)
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status = 400)
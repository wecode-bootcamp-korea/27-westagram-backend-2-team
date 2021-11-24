import json, bcrypt, jwt
 
from django.views           import View
from django.http            import JsonResponse
from django.core.exceptions import ValidationError

from .models                import User
from .validator             import is_blank, email_validate, password_validate
from my_settings            import SECRET_KEY

class SignupView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            is_blank(data.get('email'), data.get('password'))
            email_validate(data['email'])
            password_validate(data['password'])
            
            if User.objects.filter(email = data['email']).exists():
                raise ValidationError('DUPLICATED_EMAIL')

            hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode()
            
            User.objects.create(
                name        = data['name'],
                email       = data['email'],
                password    = hashed_password,
                address     = data['address'],
                information = data.get('information')
            )
            return JsonResponse({'message':'SUCCESS'},status=201)

        except ValidationError as e:
            return JsonResponse({'message': e.message},status=400)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)
    
class SigninView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = User.objects.filter(email = data['email'], password = data['password'])
            
            if not user.exists():
                raise ValidationError('INVALID_USER')

            return JsonResponse({'message': 'SUCCESS'}, status=200)
        
        except User.DoesNotExist:
            return JsonResponse({'message':'INVALID_USER'}, status=401)
        except ValidationError as e:
            return JsonResponse({'message' : e.message}, status = 401)
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status = 400)
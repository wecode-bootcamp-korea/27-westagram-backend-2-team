import json, jwt

from django.http    import JsonResponse

from my_settings    import SECRET_KEY, ALGORITHM
from users.models   import User

def signin_required(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            acces_token  = request.headers.get('Authorization', None)
            payload      = jwt.decode(acces_token, SECRET_KEY, algorithms=ALGORITHM)
            user         = User.objects.get(id = payload.get('user'))
            request.user = user

        except jwt.exceptions.DecodeError:
            return JsonResponse({'message':'INVALID_TOKEN'}, status = 400)
        except User.DoesNotExist:
            return JsonResponse({'message':'INVALID_USER'}, status = 401)
        
        return func(self, request, *args, **kwargs)
    return wrapper
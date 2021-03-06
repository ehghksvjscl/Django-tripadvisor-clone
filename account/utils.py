import jwt, json, requests

from django.http import JsonResponse
from my_settings import SECRET_KEY, ALGORITHM
from .models     import User

def login_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            token        = request.headers.get('Authorization')
            data         = jwt.decode(token, SECRET_KEY, algorithms = ALGORITHM)
            user         = User.objects.get(id = data['user'])
            request.user = user
        except jwt.exceptions.DecodeError:
            return JsonResponse({'message':'INVALID_ACCESS_TOKEN' }, status=401)
        except User.DoesNotExist:
            return JsonResponse({'message':'INVALID_USER'}, status=400)
        return func(self, request, *args, **kwargs)
    return wrapper


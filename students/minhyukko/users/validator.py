import re

from django.core.exceptions import ValidationError

from .models                import User

def is_blank(email, password):
    if email is None:
        raise KeyError('EMAIL_IS_BLANK')
    if password is None:
        raise KeyError('PASSWORD_IS_BLANK')

def is_regexr(email, password): 
    regexr_email = '[a-zA-Z0-9]+\.?\w*@\w+[.]?\w*[.]+\w{2,3}'
    regexr_password = '(?=.*[A-Za-z])(?=.*\d)(?=.*[~!@#$^&*()+|=])[A-Za-z\d~!@#$%^&*()+|=]{8,}'
    if not re.match(regexr_email, email) or not re.match(regexr_password,password): 
        raise ValidationError('INVALID_KEY')

def is_duplicated(email):
    if User.objects.filter(email = email).exists():
        raise ValidationError('DUPLICATED_EMAIL')
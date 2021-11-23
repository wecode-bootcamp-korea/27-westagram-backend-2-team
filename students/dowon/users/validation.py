import re

from django.core.exceptions import ValidationError

from .models                import User
            
regex_email    = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9_-]+\.[a-zA-Z0-9-.]+$'
regex_password = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}'

def validate_email(email):
    if re.match(regex_email, email) is None:
        raise ValidationError('INVALID_EMAIL')
    if User.objects.filter(email=email).exists():
        raise ValidationError('ALREADY_EXISTS')

def validate_password(password):
    if re.match(regex_password, password) is None:
        raise ValidationError('INVALID_PASSWORD')

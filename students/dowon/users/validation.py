import re

from django.core.exceptions import ValidationError

from .models                import User
            
regex_email    = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9_-]+\.[a-zA-Z0-9-.]+$'
regex_password = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}'

def validate_email(email):
    if not re.match(regex_email, email):
        raise ValidationError('INVALID_EMAIL')

def validate_password(password):
    if not re.match(regex_password, password):
        raise ValidationError('INVALID_PASSWORD')

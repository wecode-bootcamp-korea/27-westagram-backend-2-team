import re

from django.core.exceptions import ValidationError

from .models                import User


def validate_email(email):
    email_regex    = '(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
    
    if User.objects.filter(email=email).exists():
        raise ValidationError('ALREADY_EXISTS')
    if not re.match(email_regex, email):
        raise ValidationError('INVALID_EMAIL')

def validate_password(password):
    password_regex = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$'

    if not re.match(password_regex, password):
        raise ValidationError('INVALID_PASSWORD')
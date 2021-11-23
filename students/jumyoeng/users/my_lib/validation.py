import re 

from django.core.exceptions import ValidationError

def email_validation(email) :
    email_form =r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if not re.match(email_form , email) :
        raise ValidationError('EMAIL_INVALID')

def password_validation(password) :
    password_form = '^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$'
    if not re.match(password_form, password) :
        raise ValidationError('PASSWORD_INVALID')
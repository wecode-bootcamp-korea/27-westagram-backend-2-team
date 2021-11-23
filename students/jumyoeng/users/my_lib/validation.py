import re 

def email_validation(email) :
    em_form =r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    vaild = re.search(em_form , email)
    return vaild

def password_validation(password) :
    if len(password) < 8 :
        return False
    elif re.search('[\d]+', password) is None:
        return False
    elif re.search('[\D]+', password) is None:
        return False
    elif re.search('[,./~!@#$%^&*()><]+', password) is None:
        return False
    else :
        return True
 
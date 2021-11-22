import re 

def email_validation(email) :
    em_form =r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    vaild = re.search(em_form , email)
    if vaild : 
        return True
    else :
        return False

def password_validation(password) :
    if len(password) < 8 :
        print("최소 8자 이상 입력해주세요.")
        return False
    elif re.search('[\d]+', password) is None:
        print("최소 하나의 숫자가 포함되어야 합니다.")
        return False
    elif re.search('[\D]+', password) is None:
        print("최소 하나의 문자가 포함되어야 합니다.")
        return False
    elif re.search('[,./~!@#$%^&*()><]+', password) is None:
        print("최소 하나의 특수문자가 포함되어야 합니다.")
        return False
    else :
        return True
 
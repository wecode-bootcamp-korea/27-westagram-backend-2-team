import bcrypt

def psw_hash(password) :
    return bcrypt.hashpw( password.encode('utf-8'), bcrypt.gensalt())

def psw_check(password, hashed_password) :
    return  bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8') )
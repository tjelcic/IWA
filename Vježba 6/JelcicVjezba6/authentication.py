#!C:\Users\tjelcic\AppData\Local\Programs\Python\Python310\python.exe

import database
import password_utils

def register(username, password, email):
    user_id = database.create_user(username, password, email)
    if user_id:
        return True
    else:
        return False
        
def authenticate(username, password):
    user = database.get_user(username)
    if (user and password_utils.verify_password(password, user[2])):
        return True, user[0]
    else:
        return False, None
        
def change_password(username, old, new, new2):
    user = database.get_user(username)
    if (password_utils.verify_password(old, user[2]) and new==new2):
        success = database.change_user_password(username, new)
        if success:
            return True
        else:
            return False
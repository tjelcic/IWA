#!C:\Users\tjelcic\AppData\Local\Programs\Python\Python310\python.exe

import base
import os,cgi
import session
import authentication
from http import cookies

params = cgi.FieldStorage()
if (os.environ["REQUEST_METHOD"].upper() == "POST"):
    username = params.getvalue("username")
    password = params.getvalue("password")
    success, user_id = authentication.authenticate(username, password)
    if(success):
        session_id = session.create_session()
        session.add_user_to_session({"user_id": user_id}, session_id=session_id)
        print("Location: index.py")


base.start_html()
print ('''
<form method="POST">
Username <input type="text" name="username" /><br>
Password <input type="password" name="password"/><br>
<input type="submit" value="Login"/>
<br>
<br>
<a href="register.py">Register</a>
</form>''')
if (os.environ["REQUEST_METHOD"].upper() == "POST" and not success):
    print ("<div>Login Error</div>")
base.finish_html()


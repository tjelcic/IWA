#!C:\Users\tjelcic\AppData\Local\Programs\Python\Python310\python.exe

import base
import authentication
import cgi, os


params = cgi.FieldStorage()
if os.environ["REQUEST_METHOD"].upper() == "POST":
    
    username = params.getvalue("username")
    email = params.getvalue("email")
    password = params.getvalue("password")
    password2 = params.getvalue("password2")
    if(password==password2):
        success = authentication.register(username, password, email)
        if success:
            print('Location: login.py')

base.start_html()
print ('''<form method="POST">
username <input type="text" name="username"/><br>
email <input type="email" name="email"/><br>
password <input type="password" name="password"/><br>
repeat password <input type="password" name="password2"/><br>
<input type="submit" value="Register"/>
<br>
<br>
<a href="login.py">Log In</a>
</form>''')
if os.environ["REQUEST_METHOD"].upper() == "POST" and not success:
    print("<div>Registration Error</div>")
base.finish_html()
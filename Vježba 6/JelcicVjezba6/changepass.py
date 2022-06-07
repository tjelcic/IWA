#!C:\Users\tjelcic\AppData\Local\Programs\Python\Python310\python.exe

import base
import os
import cgi
import authentication
import database
from http import cookies

http_cookies_str = os.environ.get('HTTP_COOKIE', '')
get_all_cookies_object = cookies.SimpleCookie(http_cookies_str)
username = get_all_cookies_object.get("username").value
params = cgi.FieldStorage()
user = database.get_user(username)


if os.environ["REQUEST_METHOD"].upper() == "POST":
    old = params.getvalue("oldpass")
    new = params.getvalue("password")
    new2 = params.getvalue("password2")
    success = authentication.change_password(
                str(username), old, new, new2)
    if success:
        print('Location: login.py')


base.start_html()
print('''
<form method="POST">
<h2>Change Password</h2>
<p>''' + str(username) + ''' </p>
Old password <input type="password" name="oldpass"/>
New password <input type="password" name="password"/>
Repeat password <input type="password" name="password2"/>
<input type="submit" value="Change"/>
</form>
''')
if (os.environ["REQUEST_METHOD"].upper() == "POST" and not success):
    print("<div>Error</div>")
base.finish_html()
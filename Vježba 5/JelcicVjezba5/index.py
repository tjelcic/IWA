#!C:\Users\tjelcic\AppData\Local\Programs\Python\Python310\python.exe

import base
import cgi
import printTable
import session
import os
import database
from http import cookies

params = cgi.FieldStorage()
if (os.environ["REQUEST_METHOD"].upper() == "POST"):
    session.add_to_session(params)

http_cookies_str = os.environ.get('HTTP_COOKIE', '')
get_all_cookies_object = cookies.SimpleCookie(http_cookies_str)

if not get_all_cookies_object.get("username"):
    print("Location: login.py")
else:
    data = session.get_session_data()
    for key, value in data.items():
        if key=='username':
            name=value

predmeti = database.get_subjects()

def print_nav():
    print("""
    <div> Hej """ + name + """!<div>
    <br>
    <div>
    <input type="submit" value="1st Year" name="clicked">
    <input type="submit" value="2nd Year" name="clicked">
    <input type="submit" value="3rd Year" name="clicked">
    </div>""")

base.start_html()
print('<form action ="" method="post">')
print_nav()

click = params.getvalue('clicked')

if (click=="1st Year"):
    printTable.printTableDb(predmeti,1,data)
elif (click=="2nd Year"):
    printTable.printTableDb(predmeti,2,data)
elif (click=="3rd Year"):
    printTable.printTableDb(predmeti,3,data)
else:
    printTable.printTableDb(predmeti,1,data)

print('<br><input type="submit" name="submit" value="Submit"><br><br>')
print('<a href=upisniList.py> List All </a>')
print('''
<a href=changepass.py> Change Password </a>
<a href=logout.py> Log Out </a>
''')
print('</form>')
base.finish_html()
#!C:\Users\tjelcic\AppData\Local\Programs\Python\Python310\python.exe

import base
import cgi
import print_table
import session
import os
import database
from http import cookies

http_cookies_str = os.environ.get('HTTP_COOKIE', '')
get_all_cookies_object = cookies.SimpleCookie(http_cookies_str)

if not get_all_cookies_object.get("session_id"):
    print("Location: login.py")
else:
    data = session.get_session_data()
    for key, value in data.items():
        if key=='user_id':
            student_id=value
            podaci = database.get_from_upisni_list(student_id)
            
predmeti = database.get_subjects()
params = cgi.FieldStorage()

if (os.environ["REQUEST_METHOD"].upper() == "POST"):
    for predmet in params.keys():
        if predmet.isnumeric():
            predmet_id=predmet
            status=params.getvalue(predmet, default="not")
            database.add_to_upisni_list(student_id,predmet_id,status)

def print_nav():
    print("""
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
    print_table.print_table(predmeti,1,podaci)
elif (click=="2nd Year"):
    print_table.print_table(predmeti,2,podaci)
elif (click=="3rd Year"):
    print_table.print_table(predmeti,3,podaci)
else:
    print_table.print_table(predmeti,1,podaci)

print('<br><input type="submit" name="submit" value="Submit"><br><br>')
print('<a href=popis_studenata.py> Popis studenata </a>')
print('''
<br><a href=changepass.py> Change Password </a>
<br><a href=logout.py> Log Out </a>
''')
print('</form>')
base.finish_html()

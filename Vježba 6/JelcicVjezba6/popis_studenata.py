#!C:\Users\tjelcic\AppData\Local\Programs\Python\Python310\python.exe

import base
import session
import database

data = session.get_session_data()
for key, value in data.items():
    if key=='user_id':
        user_id=value
role = database.get_user_role_enum(user_id)


base.start_html()
if role == "student":
    print("Nemate pravo pristupa <br>")
    print('<a href=index.py> Back </a>')
else:
    students = database.get_students()
    for student in students:
        print('<a href=upisni_list.py/?id=' + str(student[0]) + '>' + student[1] + '</a><br>')

base.finish_html()


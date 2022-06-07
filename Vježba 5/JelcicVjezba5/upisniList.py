#!C:\Users\tjelcic\AppData\Local\Programs\Python\Python310\python.exe

import base
import cgi
import printTable
import session
import os
import database

params=cgi.FieldStorage()

if (os.environ["REQUEST_METHOD"].upper() == "POST"):
    session.add_to_session(params)

data = session.get_session_data()
predmeti = database.get_subjects()

base.start_html()
printTable.printPaperDb(predmeti,data)
print('''
<br>
<a href=changepass.py> Change Password </a>
<br>
<a href=logout.py> Log Out </a>
''')
base.finish_html()

#!C:\ProgramData\Anaconda3\python.exe

import base
import subject
import cgi
import printTable
import session
import os

params = cgi.FieldStorage()
if (os.environ["REQUEST_METHOD"].upper() == "POST"):
    session.add_to_session(params)

data = session.get_session_data()

def print_nav():
    print("""<div>
    <input type="submit" value="1st Year" name="clicked">
    <input type="submit" value="2nd Year" name="clicked">
    <input type="submit" value="3rd Year" name="clicked">
    </div>""")

base.start_html()
print('<form action ="" method="post">')
print_nav()
subjects = subject.getSubjects()
click = params.getvalue('clicked')

if (click=="1st Year"):
    printTable.printTable(subjects,1,data)
elif (click=="2nd Year"):
    printTable.printTable(subjects,2,data)
elif (click=="3rd Year"):
    printTable.printTable(subjects,3,data)
else:
    printTable.printTable(subjects,1,data)

print('<br><input type="submit" name="submit" value="Submit"><br><br>')

print('<a href=upisniList.py> List All </a>')
print('</form>')
base.finish_html()


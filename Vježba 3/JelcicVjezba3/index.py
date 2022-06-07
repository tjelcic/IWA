#!C:\Users\tjelcic\AppData\Local\Programs\Python\Python310\python.exe
import base
import subject
import cgi
import printTable
import model

params = cgi.FieldStorage()

def print_nav():
    print("""<div>
    <input type="submit" value="1st Year" name="clicked">
    <input type="submit" value="2nd Year" name="clicked">
    <input type="submit" value="3rd Year" name="clicked">
    </div>""")

model.set_cookies(params)
kolacici=model.get_cookies()

base.start_html()
print('<form action ="" method="post">')
print_nav()
subjects = subject.getSubjects()
click = params.getvalue('clicked')

for k in subject.subjects.keys():
    if k in params.keys():
        kolacici[k]=params.getvalue(k)

if (click=="1st Year"):
    printTable.printTable(subjects,1,kolacici)
elif (click=="2nd Year"):
    printTable.printTable(subjects,2,kolacici)
elif (click=="3rd Year"):
    printTable.printTable(subjects,3,kolacici)
else:
    printTable.printTable(subjects,1,kolacici)

print('<a href=upisniList.py> List All </a>')
print('</form>')
base.finish_html()


#!C:\Users\tjelcic\AppData\Local\Programs\Python\Python310\python.exe

import base
import subject
import cgi
import printTable
import model

params=cgi.FieldStorage()

kolacici=model.get_cookies()

base.start_html()
subjects = subject.getSubjects()
printTable.printPaper(subjects,kolacici)
base.finish_html()

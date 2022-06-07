#!C:\Users\tjelcic\AppData\Local\Programs\Python\Python310\python.exe

import base
import cgi
import print_table
import database

params=cgi.FieldStorage()
student_id=params.getvalue('id')

predmeti = database.get_subjects()
podaci = database.get_from_upisni_list(student_id)

base.start_html()
print_table.print_paper(predmeti,podaci)
base.finish_html()



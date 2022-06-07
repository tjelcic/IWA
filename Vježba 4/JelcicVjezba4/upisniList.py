#!C:\ProgramData\Anaconda3\python.exe

import base
import subject
import cgi
import printTable
import session
import os

params=cgi.FieldStorage()

if (os.environ["REQUEST_METHOD"].upper() == "POST"):
    session.add_to_session(params)

data = session.get_session_data()

base.start_html()
subjects = subject.getSubjects()
printTable.printPaper(subjects,data)
base.finish_html()

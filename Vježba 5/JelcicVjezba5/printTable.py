#!C:\Users\tjelcic\AppData\Local\Programs\Python\Python310\python.exe

import subject

def printTableDb (subjects, godina, data):
    print('<table>')
    print('<tr><td>'+ str(godina) +'. Godina</td><td></td></tr><tr><td>Predmet</td><td>Status</td></tr>')
    for row in subjects:
        if(row[4]==godina):
            print('<tr><td>')
            print(row[2])
            print('</td><td>')
            subject.displayRadio(row[1],data)
            print('</td></tr>')
    print('</table>')

def printPaperDb(subjects,data):
    suma = 0
    print('<table>')
    print('<tr><td>Predmet</td><td>Status</td><td>Bodovi</td></tr>')
    for row in subjects:
        if (data[row[1]] == "enr"):
            suma+=row[3]
        print('<tr><td>')
        print(row[2])
        print('</td><td>')
        print(subject.status_names.get(data[row[1]]))
        print('</td><td>')
        print(row[3])
        print('</td></tr>')
    print('<tr><td></td><td>Ukupno bodova:</td><td>' + str(suma) + '</td></tr>') 
    print('</table>')




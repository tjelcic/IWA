#!C:\Users\tjelcic\AppData\Local\Programs\Python\Python310\python.exe

import subject

def print_table (subjects, godina, data):
    print('<table>')
    print('<tr><td>'+ str(godina) +'. Godina</td><td></td></tr><tr><td>Predmet</td><td>Status</td></tr>')
    for row in subjects:
        if(row[4]==godina):
            print('<tr><td>')
            print(row[2])
            print('</td><td>')
            subject.display_radio(row[0],data)
            print('</td></tr>')
    print('</table>')

def print_paper(subjects,data):
    suma = 0
    print('<table>')
    print('<tr><td>Predmet</td><td>Status</td><td>Bodovi</td></tr>')
    for row in subjects:
        if (data[row[0]] == "enr"):
            suma+=row[3]
        print('<tr><td>')
        print(row[2])
        print('</td><td>')
        print(subject.status_names.get(data[row[0]]))
        print('</td><td>')
        print(row[3])
        print('</td></tr>')
    print('<tr><td></td><td>Ukupno bodova:</td><td>' + str(suma) + '</td></tr>') 
    print('</table>')




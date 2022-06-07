#!C:\ProgramData\Anaconda3\python.exe

import cgi

form = cgi.FieldStorage()

ime = form.getvalue("ime")
lozinka = form.getvalue("lozinka")
lozinka2 = form.getvalue("lozinka2")

if(lozinka != lozinka2):
    print("Location: prva.py")

print('''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <form action="treca.py" method="post">
        <table>
            <tr>
                <td>Status:</td>
                <td>
                    Redovan: <input type="radio" name="radio1" value="Redovan" checked="checked"/>
                    Izvanredan:<input type="radio" name="radio1" value="Izvanredan"/>
                </td>
            </tr>
            <tr>
                <td>E-mail:</td>
                <td>
                    <input type = "email" name = "email"/>
                </td>
            </tr>
            <tr>
                <td>Smjer:</td>
                <td>
                    <select name="smjer">
                        <option value="Baze podataka">Baze podataka</option>
                        <option value="Racunalni sustavi">Racunalni sustavi</option>
                        <option value="Programiranje">Programiranje</option>
                        <option value="Informacijski sustavi">Informacijski sustavi</option>
                    </select>
                </td>
            </tr>
            <tr>
                <td>Zavrsni:</td>
                <td><input type="checkbox" name="zavrsni" value="Da"/></td>
            </tr>
            <input type="hidden" name="ime" value="{ime}">
            <tr>
                <td>
                    <input type = "submit" value = "Next" name="drugi"/>
                </td>
            </tr>
        </table>
        </form>
    </body>
</html>
'''.format(ime=ime))
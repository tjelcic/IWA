#!C:\Users\tjelcic\AppData\Local\Programs\Python\Python310\python.exe

status_names = {
    'not' : 'Not selected',
    'enr' : 'Enrolled',
    'pass' : 'Passed',
}

def display_radio(key, data):
    if (data.get(key)==None):
        print('<input type="radio" name="' + str(key) + '" value=''not'' >' + status_names.get('not'))
        print('<input type="radio" name="' + str(key) + '" value=''enr''>' + status_names.get('enr'))
        print('<input type="radio" name="' + str(key) + '" value=''pass''>' + status_names.get('pass'))
    elif (data[key] == "not"):
        print('<input type="radio" name="' + str(key) + '" value=''not'' checked>' + status_names.get('not'))
        print('<input type="radio" name="' + str(key) + '" value=''enr''>' + status_names.get('enr'))
        print('<input type="radio" name="' + str(key) + '" value=''pass''>' + status_names.get('pass'))
    elif (data[key] == "enr"):
        print('<input type="radio" name="' + str(key) + '" value=''not''>' + status_names.get('not'))
        print('<input type="radio" name="' + str(key) + '" value=''enr'' checked>' + status_names.get('enr'))
        print('<input type="radio" name="' + str(key) + '" value=''pass''>' + status_names.get('pass'))
    elif (data[key] == "pass"):
        print('<input type="radio" name="' + str(key) + '" value=''not''>' + status_names.get('not'))
        print('<input type="radio" name="' + str(key) + '" value=''enr''>' + status_names.get('enr'))
        print('<input type="radio" name="' + str(key) + '" value=''pass'' checked>' + status_names.get('pass'))



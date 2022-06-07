import os
from http import cookies


def set_cookies (params):
    for key in params:
        c = cookies.SimpleCookie()
        c[key] = params.getvalue(key)
        print (c.output())
    
def get_cookies():
    http_cookies_str = os.environ.get('HTTP_COOKIE', '')
    all_cookies_object = cookies.SimpleCookie(http_cookies_str)
    data = {}
    for key, morsel in all_cookies_object.items():
        data[key] = morsel.value
    return data


    
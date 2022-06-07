import database
import os
from http import cookies

def get_or_create_session_id():
    http_cookies_str = os.environ.get('HTTP_COOKIE', '')
    get_all_cookies_object = cookies.SimpleCookie(http_cookies_str)
    session_id = get_all_cookies_object.get("session_id").value if get_all_cookies_object.get("session_id") else None
    if session_id is None:
        session_id = database.create_session()
        cookies_object = cookies.SimpleCookie()
        cookies_object["session_id"] = session_id
        print (cookies_object.output()) 
    return session_id

def add_to_session(params):
    session_id = get_or_create_session_id()
    _, data = database.get_session(session_id)
    for article_id in params.keys():
        data[article_id] = params.getvalue(article_id)
    database.replace_session(session_id, data)

def remove_from_session(params):
    session_id = get_or_create_session_id()
    _, data = database.get_session(session_id)
    for article_id in params.keys():
        data[article_id] = data.get(article_id, 0) - 1
        if data[article_id] < 1:
            data.pop(article_id, None)
    database.replace_session(session_id, data)

def get_session_data():
    session_id = get_or_create_session_id()
    _, data = database.get_session(session_id)
    return data
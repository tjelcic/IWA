import socket

def connect_to_server(ip, port):
    s = socket.socket()
    s.connect((ip, port))
    return s

def get_source(host, page, s):
    CRLF = '\r\n'
    get = 'GET /' + page + ' HTTP/1.1' + CRLF
    get += 'Host: ' + host + CRLF + CRLF

    s.send(get.encode('utf-8'))
    return s.recv(100000).decode('latin-1')

def get_links(source, link_list):
    beg = 0
    while True:    
        beg_link = source.find('href="', beg)
        if beg_link == -1:
            return link_list
        end_link = source.find('"', beg_link + 6)
        link = source[beg_link + 6 : end_link]
        beg = end_link + 1
        if link not in link_list and '.html' in link:
            link_list.append(link)

def visit(link_list):
    visited = 0
    while visited < len(link_list):
        for i in link_list:
            #print(i)
            s = connect_to_server("www.optimazadar.hr", 80)
            source = get_source("www.optimazadar.hr", "1280/" + i, s)
            visited += 1
            beg = 0
            while True:    
                beg_link = source.find('href="', beg)
                if beg_link == -1:
                    break
                end_link = source.find('"', beg_link + 6)
                link = source[beg_link + 6 : end_link]
                beg = end_link + 1
                if link not in link_list and '.html' in link:
                    link_list.append(link)
    return link_list

link_list = []
s = connect_to_server("www.optimazadar.hr", 80)
source = get_source("www.optimazadar.hr", "1280/djelatnost1280.html", s)
#print (source)
link_list = get_links(source, link_list)
print(visit(link_list))


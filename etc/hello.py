#!/usr/bin/python3

def simple_app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type','text/plain')]
    start_response(status, response_headers)
    resp = environ['QUERY_STRING'].split("&")
    resp = [item+"\n" for item in resp]
    return resp


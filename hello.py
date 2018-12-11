<<<<<<< HEAD
def app(environ, start_response):
=======
def app (environ, start_response):
>>>>>>> cb0ac82f413ca70d728ca6cd8ee89c017e020296
  status = '200 OK'
  response_headers = [('Content-type','text/plain')]
  start_response(status, response_headers)
  resp = environ['QUERY_STRING'].split("&")
  resp = [(item+"\r\n").encode('utf-8') for item in resp]
  return resp
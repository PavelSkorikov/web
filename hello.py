from cgi import parse_qs
def app(environ, start_response):
        """data = [bytes(i+'\n', encoding = 'ascii') for i in environ['QUERY_STRING'].split('&')]
        start_response("200 OK", [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(data)))
        ])"""
        start_response('200 OK', [('Content-Type', 'text/plain')])
        qs = parse_qs(environ['QUERY_STRING'])
        return  ['%s=%s<br>' % (k, qs[k][0]) for k in qs]
def app(environ, start_response):
        data = [(i + '\n') for i in environ['QUERY_STRING'].split('&')]
        start_response("200 OK", [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(data)))
        ])
        for i in data:
            return i

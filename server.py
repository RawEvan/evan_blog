from wsgiref.simple_server import make_server
from wsgi import application

httpd = make_server('', 80, application)
print "Serving HTTP on port 80..."
httpd.serve_forever()

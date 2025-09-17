bind = "0.0.0.0:8080"
workers = 2
loglevel = "info"
#accesslog = "/var/log/gunicorn/access.log"
#errorlog = "/var/log/gunicorn/error.log"
accesslogformat = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
capture_output = True

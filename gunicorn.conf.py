import os

worker_class = "gthread"
reload = True
bind = f"0.0.0.0:8080"
workers = 1
threads = 1
max_requests = 1000
timeout = 300
loglevel = "DEBUG"
accesslog = 'logs/log.log'
access_log_format = f'%(h)s %(l)s %(u)s %(t)s - {os.getenv("FLASK_APP")} - "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

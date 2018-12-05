import os


def num_CPUs():
    if not hasattr(os, "sysconf"):
        raise RuntimeError("No sysconf detected.")
    return os.sysconf("SC_NPROCESSORS_ONLN")


bind = "0.0.0.0:2004"
workers = num_CPUs() * 2 + 1
backlog = 2048
worker_class = "gevent"
debug = True
daemon = False
pidfile = "/tmp/app-gunicorn.pid"
logfile = "/tmp/app-gunicorn.log"
loglevel = 'info'
accesslog = '/tmp/gunicorn-access.log'
timeout = 50

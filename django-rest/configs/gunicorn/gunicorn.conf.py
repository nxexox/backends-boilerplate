# coding: utf-8
#########################################
# Gunicorn Settings                     #
#########################################
import os
import threading
import sys
import traceback

# Connections settings.
bind = os.getenv('GUNICORN_SOCKET_BIND', '0.0.0.0:8000')  # The socket to bind.
backlog = os.getenv('GUNICORN_BACKLOG', 2048)  # The number of pending connections.
timeout = os.getenv('GUNICORN_TIMEOUT', 30)  # Time to close client connection.
# The number of seconds to wait for the next request on a Keep-Alive HTTP connection.
keepalive = os.getenv('GUNICORN_KEEPALIVE', 2)

# Workers settings.
# The number of worker processes that this server should keep alive for handling requests.
workers = os.getenv('GUNICORN_WORKERS', 3)
threads = os.getenv('GUNICORN_THREADS', 10)
worker_class = os.getenv('GUNICORN_WORKER_CLASS', 'sync')  # The type of workers to use.
max_requests = os.getenv('GUNICORN_MAX_REQUESTS', 1000)
reload = os.getenv('GUNICORN_RELOAD', True)

# Logger settings.
errorlog = os.path.join(
    os.getenv('DJANGO_LOG_FOLDER', '/opt/logs'),
    os.getenv('GUNICORN_ERROR_LOG_FILE', 'gunicorn.error.log')
)
accesslog = os.path.join(
    os.getenv('DJANGO_LOG_FOLDER', '/opt/logs'),
    os.getenv('GUNICORN_ERROR_LOG_FILE', 'gunicorn.access.log')
)
loglevel = 'debug'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'


#########################################
# Server Hooks                          #
#########################################
def post_fork(server, worker):
    """
    Called just after a worker has been forked.
    A callable that takes a server and worker instance as arguments.

    """
    server.log.info('Worker spawned (pid: %s).', worker.pid)


def pre_fork(server, worker):
    """
    Called just prior to forking the worker subprocess.
    A callable that takes a server and worker instance as arguments.

    """
    server.log.info('The worker is going to be born (pid: %s).', worker.pid)


def pre_exec(server):
    """
    Called just prior to forking off a secondary
    master process during things like config reloading.
    A callable that takes a server instance as the sole argument.

    """
    server.log.info('Forked child, re-executing.')


def when_ready(server):
    """
    Called just after gunicorn starting.
    A callable that takes a server instance as the sole argument.

    """
    server.log.info('Server is ready. Spawning workers.')


def worker_int(worker):
    """
    Called when a worker dies.
    Write custom log data.

    """
    worker.log.info('Worker received INT or QUIT signal.')
    id2name = dict([(th.ident, th.name) for th in threading.enumerate()])
    code = []

    for threadId, stack in sys._current_frames().items():
        code.append('\n# Thread: {}({})'.format(id2name.get(threadId, ''), threadId))

        for filename, lineno, name, line in traceback.extract_stack(stack):
            code.append('File: "{}", line {}, in {}'.format(filename, lineno, name))

            if line:
                code.append('  `{}`'.format(line.strip()))

    worker.log.debug('\n'.join(code))


def worker_abort(worker):
    """
    It is sent when the worker abnormally completes his work.

    """
    worker.log.info('Worker received SIGABRT signal.')

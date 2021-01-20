"""Collect profiling statistic into graphite"""
import socket
import time


CARBON_SERVER = '127.0.0.1'
CARBON_PORT = 2003


class Stats(object):
    """Context manager for send stats to graphite"""

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        duration = (time.time() - self.start) * 1000  # msec
        message = '%s %d %d\n' % (self.name, duration, time.time())

        sock = socket.socket()
        sock.connect((CARBON_SERVER, CARBON_PORT))
        sock.sendall(message)
        sock.close()


# """Collect profiling statistic into graphite"""
# def stats(name):
#     """Decorator for send stats to graphite"""
#
#     def _timing(func):
#         def _wrapper(*args, **kwargs):
#             start = time.time()
#             in_data = func(*args, **kwargs)
#             duration = (time.time() - start) * 1000  # msec
#             message = '%s %d %d\n' % (name, duration, time.time())
#
#             sock = socket.socket()
#             sock.connect((CARBON_SERVER, CARBON_PORT))
#             sock.sendall(message)
#             sock.close()
#
#             return in_data
#
#         return _wrapper
#
#     return _timing


def prinster():
    for i in range(100):
        i = i * i * i * i
    return i

with Stats('project.application.some_action'):
    x = printer()
    print(x)
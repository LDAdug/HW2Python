import time

def timestamp(func):

    def wrap_func():
        print("%s" % time.ctime())
        func()
    return wrap_func



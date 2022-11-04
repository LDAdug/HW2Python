from time import time

def timeme(func):

    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Total time {(t2-t1):.4f}s')
        return result
    return wrap_func


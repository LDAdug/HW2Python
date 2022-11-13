import time

def timeme(func):
    def wrap_func(*args, **kwargs):
        t1 = time.time()
        t12 = int(t1)
        t13 = "{:.4f}".format(t12)
        result = func(*args, **kwargs)

        t2 = time.time()
        t22 = int(t2)
        t23 = "{:.4f}".format(t22)
        print(f'Total time {(t22-t12)}s')
        return result
    return wrap_func


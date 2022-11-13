import time

def timeme(func):
    def wrap_func(*args, **kwargs):
        t1 = time.time()
        float(int(t1))
        t12 = "{:.4f}".format(t1)
        result = func(*args, **kwargs)

        t2 = time.time()
        float(int(t2))
        t22 = "{:.4f}".format(t2)
        print(f'Total time {(t22-t12)}s')
        return result
    return wrap_func


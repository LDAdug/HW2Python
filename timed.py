import time

def timeme(func):
    def wrap_func(*args, **kwargs):
        t1 = time.time()
        float(int(t1))

        result = func(*args, **kwargs)

        t2 = time.time()
        float(int(t2))

        print(f"Total time %.2fs" % (t2-t1))
    return wrap_func



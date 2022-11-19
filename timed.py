import time

def timeme(func):
    def wrap_func():
        t1 = time.time()
        float(int(t1))

        result = func()

        t2 = time.time()
        float(int(t2))

        print(f"Total time {(t2-t1)}")
    return wrap_func



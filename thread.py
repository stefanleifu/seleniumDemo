import threading
import time

a = [100]


def func1():
    for i in range(100000000):
        a[0] += 1
    print('线程1修改完a=', a)


def func2():
    for i in range(100000000):
        a[0] += 1
    print('线程2修改完a=', a)


t1 = threading.Thread(target=func1())
t2 = threading.Thread(target=func2())

t1.start()
t2.start()
t1.join()
t2.join()

print(a)

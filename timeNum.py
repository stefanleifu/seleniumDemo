import timeit


def func():
    for i in range(10):
        print(i)


# res = timeit.Timer(func).timeit(1)
# print(res)

res2 = timeit.timeit(func)
print(res2)
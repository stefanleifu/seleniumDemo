# 生成器对象
# tu = (i for i in range(100))
#
# a = next(tu)
# print(a)
# print(next(tu))

def yiled_test(n):
    for i in range(n):
        yield i*2
        # 下一次迭代时，从下面的print('i=',i)开始执行
        print('i in the yield_test',i)
    print('Finish at the end of yiled_test')

if __name__ == '__main__':
    # 必须使用迭代来获取yield_test()函数返回值
    for i in yiled_test(3):
        print('i in the main',i)


#读取人物名称
# f = open('name1.txt')
# data = f.read()
# print(data.split('|'))

#读取兵器的名称
f2 = open('weapon.txt')
# data2 = f2.read()
i = 1
for line in f2.readline():
    if i % 2 == 1:
        print(line)
        i += 1
# print(data2)
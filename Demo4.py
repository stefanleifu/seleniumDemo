dict1 = {}
print(type(dict1))
dict2 = {'x':1, 'y':2}
print(dict2)

chinese_zodiax = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
zodiac_name = (u'摩羯座',u'水瓶座',u'双鱼座',u'白羊座',u'金牛座',u'双子座',u'巨蟹座',u'狮子座',
               u'处女座',u'天秤座',u'天蝎座',u'射手座',)
zodiac_days = ((1,20),(2,19),(3,21),(4,21),(5,21),(6,22),
               (7,23),(8,23),(9,23),(10,23),(11,23),(12,23))
while True:
    # 用户输入月份和日期
    year = int(input('请输入年份：'))
    int_month = int(input(('请输入月份：')))
    int_day = int(input(('请输入日期：')))

    cz_num = {}
    for i in chinese_zodiax:
        cz_num[i] = 0

    z_num = {}
    for i in zodiac_name:
        z_num = 0


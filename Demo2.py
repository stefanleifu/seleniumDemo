chinese_zodiax = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
year = 2021
year = int(input('请用户输入出生年份：'))
if(chinese_zodiax[year%12]) == '狗':
    print('狗年。。。')


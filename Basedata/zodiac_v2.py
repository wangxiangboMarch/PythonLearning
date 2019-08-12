# for循环中的if 嵌套

# 星座
zodiac_name = ('魔蝎座', '水瓶座', '双鱼座', '白羊座', '金牛座', '双子座', '巨蟹座',
               '狮子座', '处女座', '天平座', '天蝎座', '射手座')
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23),
               (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

# 用户输入月份和日期
int_month = int(input('请输入月份：'))
int_day = int(input('请输入日期：'))


(month, day) = (int_month, int_day)
zodiac_day = filter(lambda x: x <= (month, day), zodiac_days)
print(zodiac_day)
zodiac_len = len(list(zodiac_day)) % 12
print(zodiac_len)
print(zodiac_name[zodiac_len])

# while循环中的if嵌套
n = 0
while zodiac_days[n] < (month, day):
    if int_month == 12 and int_day > 23:
        break

    n += 1
    print(zodiac_name[n])

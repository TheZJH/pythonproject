import random

"""
if 要判断的条件:
    条件成立时,要做的事
"""
age = 10
if 3 > 2:
    print("hello world")

# if else 语法结构
if age > 2:
    print("hello world")
else:
    print("error")

"""
逻辑运算
and
or
not
"""
if age >= 0 and age <= 120:
    print("true")
else:
    print("false")

# if语句进阶
if age > 1:
    print()
elif age < 1:
    print()
elif age < 0:
    print()
else:
    print()

# if嵌套
if age > 1:
    if age > 2:
        print()

# 随机数
number = random.randint(1, 6)
print(number)
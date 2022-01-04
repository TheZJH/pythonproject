cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    # Python检查是否相等时区分大小写
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

age_0 = 18
age_1 = 60
# 使用and,使用括号改善易读性
if (age_0 >= 18) and (age_1 <= 60):
    print("可以996")
# 使用or
if (age_0 > 18) or (age_1 < 60) or (1 < 2):
    print("haha")
    if 'bmw' == 'bmw':
        print()
# 检查特定值是否包含在列表中
requested_toppings = ['mushrooms', 'onions', 'pineapple']
boolean = 'mushrooms' in requested_toppings
print(boolean)

# 检查特定值不包含在列表中,not in

# 布尔表达式
game_active = True
can_edit = False

# if-elif-else
if 1 > 0:
    print("1>0")
elif 2 > 0:
    print("2>0")
else:
    print("hello")

# 在if语句将列表名用在条件表达式时，Python将在列表至少包含一个元素时返回True
requested_toppings=[]
if requested_toppings:
    print("nothing")

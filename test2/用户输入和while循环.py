# message = input("Tell me something, and I will repeat it back to you:")
# print(message)
# name = input("Please input your name: ")
# print("Hello," + name + "!")
# 1.使用int()获取数值
# age = int(input("Tell me your age!"))
# print(type(age))

# 2.使用while循环
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# 3.使用标志符，判断程序是否处于活动状态
active = True
# while active:
# print("你好！")

# 4.删除包含特定值的所有列表元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
# 判断pets中是否有cat字符串
print('cat' in pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

# 5.使用用户输入来填充字典
responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like you to climb someday?")
    responses[name] = response
    repeat = input("Would you like to le person?(yes/no)")
    if repeat == 'no':
        polling_active = False
print(responses)

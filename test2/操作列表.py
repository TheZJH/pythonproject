magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick\n")
print("Thank you!")
# 生成数字range()
for value in range(1, 5):
    print(value)
# list直接转换
numbers = list(range(1, 10, 3))
print(numbers)
# 列表解析
squares = [value ** 2 for value in range(1, 11)]
print(squares)
# 切片,第一个元素的索引和最后一个元素的索引
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
# 遍历切片
for player in players[:3]:
    print(player.title())
# 复制列表,使用切片
my_foods = ['pizza', 'noodles', 'cake']
# 复制全部列表
friend_foods = my_foods[:]
# 元组,不可变的列表
dimensions = (200, 50)
print(dimensions)


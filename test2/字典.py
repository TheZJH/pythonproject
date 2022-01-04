# 字典类似于HashMap
alien_0 = {'color': 'green', 'points': 5}
# 获取字典索引的值
print(alien_0['color'])
# 1.添加键值对
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
# 2.删除键值对
del alien_0['color']
# 3.有类似对象组成的字典
favorite_languages = {
    # 每一行数据后面要有逗号,给最后一个键值对也加上逗号，为下次添加做好准备
    'jen': 'python',
    'sarah': 'c',
    'phil': 'ruby',
    'zjh': 'c',
    'zjw': 'java',
}
# 4.遍历字典
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
# items()返回一个键值对列表
for key, value in user_0.items():
    print("\nkey:" + key)
    print("Value:" + value)

# 5.遍历字典中的所有键,key()
for name in favorite_languages.keys():
    print(name.title())

# 6.按顺序遍历字典中的所有键
for name in sorted(favorite_languages.keys()):
    print(name.title() + ",thank you for taking the poll.")

# 7.遍历字典的所有值
for language in favorite_languages.values():
    print(language.title())

# 8.使用集合set去除重复项
for language in sorted(favorite_languages.values()):
    print(language)

# 嵌套
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

# 创建一个用于存储外星人的空列表
aliens = []
# 创建30个绿色的外星人,循环30次
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# 显示前5个外星人
for alien in aliens[:5]:
    print(alien)

# 显示创建了多少个外星人
print("Total number of aliens: " + str(len(aliens)))

# 在字典中存储列表
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# 在Python中，用方括号[]表示列表，用逗号分隔
bicyles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicyles)
print(bicyles[0])
# title()方法首字母大写
print(bicyles[0].title())
# -1索引返回最后一个列表元素
print(bicyles[-1])
message = "My first bicycle is a " + bicyles[-2].title() + "."
print(message)
# 3-1 姓名：将一些朋友的姓名存储在一个列表中，并将其命名为 names。依次访问,该列表中的每个元素，从而将每个朋友的姓名都打印出来。
names = ['zjh', 'cwy', 'zrl', 'wrj', 'zjw', 'zyl']
for name in names:
    print(name)
motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)
motocycles[0] = 'dukati'
print(motocycles)
# 1.列表末尾添加元素
motocycles.append('honda')
print(motocycles)
# 2.使用insert()可在列表任何地方添加新元素
motocycles.insert(10, 'bmw')
print(motocycles)
# 3.使用del语句删除元素
del motocycles[0]
print(motocycles)
# 4.使用pop()删除元素,弹出末尾的元素
popped_moto = motocycles.pop()
print(popped_moto)
print(motocycles)
# 5.根据值删除元素remove()
motocycles.remove('yamaha')
print(len(motocycles))
# 6.使用sort()对列表进行永久性排序
# 7.使用sorted()对列表进行临时排序

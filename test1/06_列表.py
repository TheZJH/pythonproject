# 列表操作,增删查改
name_list = ["zjh", "zjw", "cwy"]
num_list = [4]
test_list = ["zjh", "zjw", "cwy", 1, True]

# 指定索引位置插入元素
name_list.insert(2, "wrj")
print(name_list)

# 列表长度
len(name_list)

# del 关键字本质上是用来将一个变量从内存中删除
name = "陈文要"
del name
for i in name_list:
    print(i)

# 迭代遍历
for name in name_list:
    print(name)

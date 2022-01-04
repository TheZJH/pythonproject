# 字典相当于java中的hashmap,无序的数据集合
cwy_dict = {"name": "cwy",
            "age": 22,
            "height": 150}

# 取值
print(cwy_dict["name"])

# 增加 修改
cwy_dict["age"] = 23

# 删除
cwy_dict.pop("height")

print(cwy_dict)

# 统计键值对数量
len(cwy_dict)

# 合并字典,相同key会被替换
temp_dict = {"win": "zjh"}
cwy_dict.update(temp_dict)

# 清空键值对
temp_dict.clear()

# 字典遍历,变量i是每次循环中获取到的键值对的key
for i in cwy_dict:
    print("%s:%s" % (i, cwy_dict[i]))

# 字典应用场景
people_list = [{"name": "cwy",
                "age": 22,
                "height": 150},
               {"name": "cwy",
                "age": 22,
                "height": 150}]

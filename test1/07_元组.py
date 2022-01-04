# 多个元素组成的序列,元素不能修改,存储不同类型的数据
info_tuple = ("zjh", 18, 180)
info_list = [1, 2, 3]
print(info_tuple)

# 元组输出
print("%s 的年龄是 %d 身高是 %d" % info_tuple)

# 格式化字符串,后面的'()'本质上就是元组
print("%s 的年龄是 %d 身高是 %d" % ("cwy", 21, 150))

info_str = "%s 的年龄是 %d 身高是 %d" % ("cwy", 21, 150)
print(info_str)

# 元组和列表直接的转换
list(info_tuple)
tuple(info_list)

# 变量名=值
a = 10
b = 20
print(a + b)

# 变量定义
name = "小明"
age = 18
sex = "boy"
height = "1.75m"
weight = "75kg"

# 字符串变量可以和整数使用*拼接相同字符串
num = (sex + height + " ") * 10
print(num)

# 输入函数 input() 使用变量名接收输入
# password = input("请输入")

"""
类型转换函数
int(x)   转换成整型
float(x) 转换成浮点型
"""

"""
变量格式化输出
%s 字符串
%d 有符号十进制整数
%f 浮点数,%0.2f表示小数点后两位
%% 输出%
print("格式化字符串" % 变量)
"""
print("%0.2f" % 2)
print("我的名字 %0.2f ,年龄 %0.2f,%0.2f,%0.2f" % (2, 3, 4, 5))

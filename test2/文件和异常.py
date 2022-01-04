"""with:在不再需要访问文件时将其关闭
返回文件的对象"""
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    # print(contents),rstrip删除多出来的空行
    print(contents.rstrip())

# 1.逐行读取,对文件对象使用for循环
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)

    # 创建一个包含文件各行内容的列表
    lines = file_object.readline()

for line in lines:
    print(line.rstrip())

# 2.写入空文件
readname = 'programming.txt'
with open(readname, 'w') as file_object:
    file_object.write("I love programming.")

# 3.附加到文件
with open(readname, 'a') as file_object:
    file_object.write("I also love finding meaning in large data.\n")
    file_object.write("I love creating apps that can run in a brower.\n")

# 使用 try-except代码块
try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    #
    print("Yes!")

# 处理filenotfounderror异常
file = 'alice.txt'
try:
    with open(file) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry,the file " + file + " does not exist."
    print(msg)
    

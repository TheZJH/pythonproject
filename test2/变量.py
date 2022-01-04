# 1.变量名只能包含字母、数字和下划线。变量名可以字母或下划线打头，但不能数字打头
# 2.变量名不能包含空格，但是可以使用下滑线分割单词
# 3.不要将Python关键字和函数名用作变量名，尽量使用小写的Python变量名
first_name = "ada"
last_name = "lovelace"
# Python使用+号合并字符串
full_name = first_name + " " + last_name
print(full_name)
# 例子
print("Hello, " + full_name + '!')
# 制表符：用来制作表格 \t,换行符 \n
print("\tPython")
print("Languages:\nPython\nC\nJava")
print("Languages:\n\tPython\n\tC\n\tJava")
# strip()方法找出字符串开头末尾多余的空白
language = "Python "
print(language.rstrip())

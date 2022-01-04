def test(num):
    print("num变量的内存地址是 %d" % id(num))


a = 10

print("a变量内存地址是 %d" % id(10))
test(a)

# 不可变类型
# 数字类型 int,bool,float,complex,long(2.x)
# 字符串 str
# 元组 tuple

# 可变类型
# 列表 list
# 字典 dict,字典的key只能使用不可变类型的数据
num = 99


def demo1():
    # 修改全局变量global声明
    global num
    num = 10
    ll = "test"
    return num, ll


ress = demo1()
print(ress)


# 多值参数:接收参数个数不确定 参数名前*可以接收元组 **可以接收字典
# *args **kwargs

def demo(number, *args, **kwargs):
    print(number)
    print(args)
    print(kwargs)


# 不使用拆包
demo(1, 2, 3, 4, 5, name="小明", age=18, gender=True)

nums = (1, 2, 4)
numss = {"name": "cwy", "age": 18}
# 不使用拆包就和之前一样不会读取,拆成上面的元素
demo(1, *nums, **numss)

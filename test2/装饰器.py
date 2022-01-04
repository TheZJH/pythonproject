def outer(x):
    def inner(y):
        return x + y

    return inner


# 在函数中再嵌套一个函数，并且引用外部函数的变量

print(outer(6)(5))

"""python装饰器就是用于拓展原来函数功能的一种函数，这个函数的特殊之处在于它的返回值也是一个函数"""


def test_number(x, y, z=''):
    if z != '':
        print(x, y, z)
    else:
        print(x, y)


test_number(x=1, y=2)

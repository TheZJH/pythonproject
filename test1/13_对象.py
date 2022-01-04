# 内置方法
"""
dir函数
__方法名__是Python提供的内置方法
类的命名要符合大驼峰
"""
class Animal:
    def eat(self):
        pass

# 定义类
class Test:
    # 初始化方法,定义一个类具体有哪些属性
    def __init__(self, name):
        self.name = name
        print("初始化")

    #私有方法
    def __private(self):
        pass

    def method1(self):
        # 哪一个对象调用的方法,self就是哪一个对象的引用
        pass

    def method2(self):
        pass


# 创建对象 对象变量=类名()
test01 = Test()
print(test01.name)

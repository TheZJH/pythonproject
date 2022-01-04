class Dog(object):
    # 构造方法
    def __init__(self, name):
        self.name = name

    def game(self):
        print("芜湖,%s 开玩" % self.name)


class XiaoTian(Dog):
    def game(self):
        print("%s 小玩一哈" % self.name)

    # 类方法
    @classmethod
    def method(cls):
        pass

    # 静态方法,不需要访问类属性,实例属性
    @staticmethod
    def method1():
        pass


class Person(object):
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s 和 %s 开玩" % self.name, dog.name)
        # 让狗调用game方法,而不关系具体是什么狗
        # 程序在执行时,传入不同的狗产生不同的执行效果
        Dog.game()


wangcai = XiaoTian("tom")

"""
1. 在内存中为对象分配空间
2. 调用初始化方法__init__为对象初始化
"""


class Game(object):
    # 历史最高分,相当全局变量
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("帮助信息:开玩")

    @classmethod
    def show_top_score(cls):
        print("历史记录 %d" % cls.top_score)

    def start_game(self):
        print("%s 开始游戏" % self.player_name)


game = Game("cwy")
game.start_game()

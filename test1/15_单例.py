class MusicPlayer(object):
    # 重写了父类的new方法
    def __new__(cls, *args, **kwargs):
        print("创建对象,分配空间")
        """
        1. 为对象分配空间
        2. 放回对象的引用
        """
        # 之前super后忘了加()...
        instance = super().__new__(cls)
        return instance

    def __init__(self):
        print("播放器初始化")


player = MusicPlayer()
print(player)


class Instance(object):
    # 定义类属性记录单例对象引用
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

def test():
    try:
        pass
        num = int(input("请输入数字: "))
    # 捕获未知错误
    except Exception as res:
        print("%s" % res)


def input_password():
    pwd = input("请输入密码: ")
    if len(pwd) >= 8:
        return pwd
    print("主动抛出异常")
    # 自定义异常类
    ex = Exception("密码长度不够")
    raise ex


try:
    print(input_password())
except Exception as re:
    print(re)

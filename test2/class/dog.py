# 括号中必须加入object不然会提示
class Dog(object):
    def __init__(self, name, age):
        # self.name相当于实参，name相当于形参
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")


# 1.根据类创建实例
my_dog = Dog('tom', 6)
your_dog = Dog('lucy', 3)
print("My dog's name is " + my_dog.name + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()
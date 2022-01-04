def greet_user():
    print('Hello!')


greet_user()


def greet_user(username):
    print("Hello," + username.title() + "!")


greet_user('jesse')


# 1.位置实参
def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + " name is " + pet_name.title())


describe_pet('hamster', 'harry')

# 2.关键字实参
describe_pet(animal_type='cat', pet_name='tom')


# 3.给形参指定默认值,默认值必须放在后面
def des_pet(pet_name, animal_type='dog'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + " name is " + pet_name.title())


des_pet('tom')


# 4.返回值
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)


# 5.让实参变成可选的
def get_formatted_name(first_name, last_name, middle_name=None):
    if middle_name != '':
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix', 'lee')
print(musician)


# 6.返回字典
def build_person(first_name, last_name):
    person = {
        'first': first_name,
        'last': last_name,
    }
    return person


musician = build_person('jimi', 'hendrix')
print(musician)


# 7.传递任意数量的实参
def make_pizza(*topping):
    # 星号让Python创建一个元组，任意数量实参的形参放在最后
    print(topping)


make_pizza('mushrooms', 'green peppers', 'extra cheese')


# 8.使用任意数量的关键字实参
def build_profile(first, last, **user_info):
    # **创建一个空字典
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last

    for key, value in user_info.items():
        profile[key] - value
        return profile

# 9.导入整个模块

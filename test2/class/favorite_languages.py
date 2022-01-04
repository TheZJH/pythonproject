# Python标准库
from collections import OrderedDict

"""要创建有序字典并记录其中的键—值对的添加顺序，可使用模块collections中的OrderedDict类。"""
# 创建一个orderedDict实例
favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

people = {
    'name': 'zjh',
    'age': 15,
}

# Python 字典(Dictionary) items() 函数以列表返回可遍历的(键, 值) 元组数组
for name, language in favorite_languages.items():
    print(name.title() + " s favorite language is " + language.title() + ".")

# print(favorite_languages.items())
# print(people)

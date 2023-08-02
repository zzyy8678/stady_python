
"""1、装饰器

装饰器实际上就是为了给某程序增添功能，但该程序已经上线或已经被使用，那么就不能大批量的修改源代码，
这样是不科学的也是不现实的，因为就产生了装饰器，使得其满足：

不能修改被装饰的函数的源代码
不能修改被装饰的函数的调用方式
满足1、2的情况下给程序增添功能
那么根据需求，同时满足了这三点原则，这才是我们的目的。因为，下面我们从解决这三点原则入手来理解装饰器。

等等，我要在需求之前先说装饰器的原则组成：

< 函数+实参高阶函数+返回值高阶函数+嵌套函数+语法糖 = 装饰器 >
这个式子是贯穿装饰器的灵魂所在！"""

# import time
# def test():
#     time.sleep(2)
#     print("test is running!")
# def deco(func):
#     start = time.time()
#     func()  # 2
#     stop = time.time()
#     print(stop - start)
# deco(test)  # 1
# import time
# import ssl
#
# def timer(func):
#     def deco():
#         start = time.time()
#         func()
#         stop = time.time()
#         print(stop - start)
#
#     return deco
#
#
# @timer
# def test(parameter):  # 8
#     time.sleep(2)
#     print("test is running!")
#
#
# test()
def 炼丹炉(func):
    def 变身(*args, **kwargs):
        print('有火眼金睛了')
        return func(*args, **kwargs)

    return 变身


def 龙宫走一趟(func):
    def 你好(*args, **kwargs):
        print('有金箍棒了')
        return func(*args, **kwargs)

    return 你好


def 拜师学艺(func):
    def 师傅(*args, **kwargs):
        print('学会飞、72变了')
        return func(*args, **kwargs)

    return 师傅


@拜师学艺
@龙宫走一趟
@炼丹炉
def 孙悟空():
    print('吃桃子')


孙悟空()

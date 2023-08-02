
"""=================================RE正则表达式====================================="""
import re
# pattern = "^hello$"
#
# string = "hello"
#
# result = re.match(pattern, string)
#
# print(result)
"""===================================、re.match函数
re.match函数可以在给定的字符串开头匹配正则表达式，如果匹配成功，返回一个匹配对象，否则返回None。
下面是一个使用re.match的例子："""

# pattern = "^hello$"
#
# string = "hello, world!"
#
# result = re.match(pattern, string)
# if result:
#     print("匹配成功")
# else:
#     print("匹配失败")
"""=================================、re.search函数
re.search函数可以在整个字符串中匹配正则表达式，如果匹配成功，返回一个匹配对象，否则返回None。
下面是一个使用re.search的例子："""
# pattern = "world"
# string = "hello, world!"
# result = re.search(pattern, string)
# if result:
#     print("匹配成功")
# else:
#     print("匹配失败")
"""==================================、re.findall函数
re.findall函数可以返回一个列表，其中包含了整个字符串中所有匹配正则表达式的子串。
下面是一个使用re.findall的例子："""
# pattern = "\d+"
#
# string = "hello, 123 world! 456"
#
# result = re.findall(pattern, string)
#
# print(result)
#
"""===========================================、re.sub函数
re.sub函数可以使用指定的字符串替换掉所有匹配正则表达式的子串。
下面是一个使用re.sub的例子：
"""
# pattern = "\d+"
# string = "hello, 123 world! 456"
# result = re.sub(pattern, "number", string)
# print(result)
"""============================================、re.split函数
re.split函数可以使用正则表达式来分割字符串。
下面是一个使用re.split的例子："""
# pattern = "s+"
# string = "hello, world!"
# result = re.split(pattern, string)
# print(result)
# text = "The quick brown fox jumps over the lazy dog."
# re_pattern = "(quick|slow) (brown|red|green) (fox|dog)"
# result = re.search(re_pattern, text)
# print(result.group(0)) # 匹配到的整个字符串
# print(result.group(1)) # 第一个分组，quick或者slow
# print(result.group(2)) # 第二个分组，brown、red或者green
# print(result.group(3)) # 第三个分组，fox或者dog
"""========================================条件判断[if else]================================"""
# age = int(input('请输⼊您的年龄：'))
# if age >= 18:
#  print(f'您的年龄是{age},已经成年，可以上⽹')
# print('系统关闭')

# a= 1
# b = 2
# c = a if a > b else b
# print(c)
"""========================================循环[while]========================================="""
# ======================================循环的计数器===================================================
# i = 0
# while i < 5:
#  print('媳妇⼉，我错了')
#  i += 1
# print('任务结束')
# 1-100累加和
# i = 1
# result = 0
# while i <= 100:
#  result += i
#  i += 1
# # 输出5050
# print(result)
# ⽅法⼀：条件判断和2取余数为0则累加计算
# i = 1
# result = 0
# while i <= 100:
#  if i % 2 == 0:
#     result += i
#  i += 1
# # 输出2550
# print(result)

"""=============================⽅法⼆：计数器控制增量为2============================="""
# i = 0
# result = 0
# while i <= 100:
#  result += i
#  i += 2
# # 输出2550
# print(result)

"""====================================break======================================="""
# i = 1
# while i <= 5:
#     if i == 4:
#         print(f'吃饱了不吃了')
#         break
#     print(f'吃了第{i}个苹果')
#     i += 1

# str1 = 'itheima'
# for i in str1:
#     if i == 'e':
#         print('遇到e不打印')
#         break
#     print(i)

"""==================================continue======================================="""
# str1 = 'itheima'
# for i in str1:
#     if i == 'e':
#         print('遇到e不打印')
#         continue
#     print(i)
"""计数器"""
# i = 1
# while i <= 5:
#     if i == 3:
#         print(f'⼤⾍⼦，第{i}个不吃了')
#         # 在continue之前⼀定要修改计数器，否则会陷⼊死循环
#         i += 1
#         continue
#     print(f'吃了第{i}个苹果')
#     i += 1
# j = 0
# while j < 3:
#  i = 0
#  while i < 3:
#     print('媳妇⼉，我错了')
#     i += 1
#     print('刷晚饭的碗')
#     print('⼀套惩罚结束----------------')
#     j += 1


""" ===============================重复打印5⾏星星=================================="""
# j表示⾏号
# j = 0
# while j <= 4:
#     # ⼀⾏星星的打印
#     i = 0
#     # i表示每⾏⾥⾯星星的个数，这个数字要和⾏号相等所以i要和j联动
#     while i <= j:
#         print('*', end='')
#         i += 1
#     print()
#     j += 1
""" ==================================重复打印9⾏表达式======================================="""
# j = 1
# while j <= 9:
#     # 打印⼀⾏⾥⾯的表达式 a * b = a*b
#     i = 1
#     while i <= j:
#         print(f'{i}*{j}={j * i}', end='\t')
#         i += 1
#     print()
#     j += 1

# i = 1
# while i <= 5:
#  print('媳妇⼉，我错了')
#  i += 1
# else:
#  print('媳妇原谅我了，真开⼼，哈哈哈哈')


# i = 1
# while i <= 5:
#  if i == 3:
#     print('这遍说的不真诚')
#     i += 1
#     continue
#  print('媳妇⼉，我错了')
#  i += 1
# else:
#  print('媳妇原谅我了，真开⼼，哈哈哈哈')
"""======================================for else========================================="""

# str1 = 'itheima'
# for i in str1:
#  print(i)
# else:
#  print('循环正常结束之后执⾏的代码')

# str1 = 'itheima'
# for i in str1:
#  if i == 'e':
#     print('遇到e不打印')
#     break
#  print(i)
# else:
#  print('循环正常结束之后执⾏的代码')

# str1 = 'itheima'
# for i in str1:
#     if i == 'e':
#         print('遇到e不打印')
#         continue
#     print(i)
# else:
#      print('循环正常结束之后执⾏的代码')
""" ======================================String ====================================="""
"""string  切片"""
# name = "abcdef"
# print(name[1])
# print(name[0])
# print(name[2])

# name = "abcdefg"
# print(name[2:5:1]) # cde
# print(name[2:5]) # cde
# print(name[:5]) # abcde
# print(name[1:]) # bcdefg
# print(name[:]) # abcdefg
# print(name[::2]) # aceg
# print(name[:-1]) # abcdef, 负1表示倒数第⼀个数据
# print(name[-4:-1]) # def
# print(name[::-1]) # gfedcb
"""==========================================查找 find 按照下表查找======================="""
# mystr = "hello world and itcast and itheima and Python"
# print(mystr.find('and')) # 12
# print(mystr.find('and', 15, 30)) # 23
# print(mystr.find('ands')) # -
"""==================index()：检测某个⼦串是否包含在这个字符串中，如果在返回这个⼦串开始的位置下标，否则则报异常"""
# mystr = "hello world and itcast and itheima and Python"
# print(mystr.index('and')) # 12
# print(mystr.index('and', 15, 30)) # 23
# print(mystr.index('ands')) # 报
""" ========================字符串序列.count(⼦串, 开始位置下标, 结束位置下标)========================"""
# mystr = "hello world and itcast and itheima and Python"
# print(mystr.count('and')) # 3
# print(mystr.count('ands')) # 0
# print(mystr.count('and', 0, 20)) # 1
"""===========================replace()：替换============================"""
# mystr = "hello world and itcast and itheima and Python"
# # 结果：hello world he itcast he itheima he Python
# print(mystr.replace('and', 'he'))
# # 结果：hello world he itcast he itheima he Python
# print(mystr.replace('and', 'he', 10))
# # 结果：hello world and itcast and itheima and Python
# print(mystr)


"""================================spilt  字符串序列.split(分割字符, num)=========================="""
# mystr = "hello world and itcast and itheima and Python"
# # 结果：['hello world ', ' itcast ', ' itheima ', ' Python']
# print(mystr.split('and'))
# # 结果：['hello world ', ' itcast ', ' itheima and Python']
# print(mystr.split('and', 2))
# # 结果：['hello', 'world', 'and', 'itcast', 'and', 'itheima', 'and', 'Python']
# print(mystr.split(' '))
# # 结果：['hello', 'world', 'and itcast and itheima and Python']
# print(mystr.split(' ', 2))
"""=======================join()：⽤⼀个字符或⼦串合并字符串，即是将多个字符串合并为⼀个新的字符串================"""
# list1 = ['chuan', 'zhi', 'bo', 'ke']
# t1 = ('aa', 'b', 'cc', 'ddd')
# # 结果：chuan_zhi_bo_ke
# print('_'.join(list1))
# # 结果：aa...b...cc...ddd
# print('...'.join(t1))
"""========================capitalize()：将字符串第⼀个字符转换成⼤写================================"""
# mystr = "hello world and itcast and itheima and Python"
# # 结果：Hello world and itcast and itheima and python
# print(mystr.capitalize())
"""===========================title()：将字符串每个单词⾸字⺟转换成⼤写=============================="""
# mystr = "hello world and itcast and itheima and Python"
# # 结果：Hello World And Itcast And Itheima And Python
# print(mystr.title())
"""=====================lower()：将字符串中⼤写转⼩写====================================="""
# mystr = "hello world and itcast and itheima and Python"
# # 结果：hello world and itcast and itheima and python
# print(mystr.lower())
"""======================upper()：将字符串中⼩写转⼤写================================"""
# mystr = "hello world and itcast and itheima and Python"
# # 结果：HELLO WORLD AND ITCAST AND ITHEIMA AND PYTHON
# print(mystr.upper())
"""=============================字符串序列.startswith(⼦串, 开始位置下标, 结束位置下标================="""

# mystr = "hello world and itcast and itheima and Python "
# # 结果：True
# print(mystr.startswith('hello'))
# # 结果False
# print(mystr.startswith('hello', 5, 20))
"""=======================字符串序列.endswith(⼦串, 开始位置下标, 结束位置下标==============================="""
# mystr = "hello world and itcast and itheima and Python"
# # 结果：True
# print(mystr.endswith('Python'))
# # 结果：False
# print(mystr.endswith('python'))
# # 结果：False
# print(mystr.endswith('Python', 2, 20))
"""=====================isalpha()：如果字符串⾄少有⼀个字符并且所有字符都是字⺟则返回 True, 否则返回 False=========="""

# mystr1 = 'hello'
# mystr2 = 'hello12345'
# # 结果：True
# print(mystr1.isalpha())
# # 结果：False
# print(mystr2.isalpha())
"""======================isdigit()：如果字符串只包含数字则返回 True 否则返回 False=============================="""
# mystr1 = 'aaa12345'
# mystr2 = '12345'
# # 结果： False
# print(mystr1.isdigit())
# # 结果：False
# print(mystr2.isdigit())
"""=========================isalnum()：如果字符串⾄少有⼀个字符并且所有字符都是字⺟或数字则返 回 True,否则返回False。"""
# mystr1 = 'aaa12345'
# mystr2 = '12345-'
# # 结果：True
# print(mystr1.isalnum())
# # 结果：False
# print(mystr2.isalnum())
# mystr1 = 'aaa12345'
# mystr2 = '12345-'
# # 结果：True
# print(mystr1.isalnum())
# # 结果：False
# print(mystr2.isalnum())
"""=======================isspace()：如果字符串中只包含空⽩，则返回 True，否则返回 False==================="""
# mystr1 = '1 2 3 4 5'
# mystr2 = ' '
# # 结果：False
# print(mystr1.isspace())
# # 结果：True
# print(mystr2.isspace())
""" =====================================LIST[]操作=============================================="""
# name_list = ['Tom', 'Lily', 'Rose']
# print(name_list[0]) # Tom
# print(name_list[1]) # Lily
# print(name_list[2]) # Rose
"""1,=====================================index()：返回指定数据所在位置的下标 """
# name_list = ['Tom', 'Lily', 'Rose']
# print(name_list.index('Lily', 0, 2)) # 1
"""2,=================================count()：统计指定数据在当前列表中出现的次数"""
# name_list = ['Tom', 'Lily', 'Rose']
# print(name_list.count('Lily')) # 1
"""3,==================================in：判断指定数据在某个列表序列，如果在返回True，否则返回False"""
# name_list = ['Tom', 'Lily', 'Rose']
# # 结果：True
# print('Lily' in name_list)
# # 结果：False
# print('Lilys' in name_list)
"""4,==============================not in：判断指定数据不在某个列表序列，如果不在返回True，否则返回False"""
# name_list = ['Tom', 'Lily', 'Rose']
# # 结果：False
# print('Lily' not in name_list)
# # 结果：True
# print('Lilys' not in name_list)
"""5,=======================================append()：列表结尾追加数据"""
# name_list = ['Tom', 'Lily', 'Rose']
# name_list.append('xiaoming')
# # 结果：['Tom', 'Lily', 'Rose', 'xiaoming']
# print(name_list)
"""6,======================================如果append()追加的数据是⼀个序列，则追加整个序列到列表"""
# name_list = ['Tom', 'Lily', 'Rose']
# name_list.append(['xiaoming', 'xiaohong'])
# # 结果：['Tom', 'Lily', 'Rose', ['xiaoming', 'xiaohong']]
# print(name_list)
"""7,===========================extend()：列表结尾追加数据，如果数据是⼀个序列，则将这个序列的数据逐⼀添加到列表。"""
# name_list = ['Tom', 'Lily', 'Rose']
# name_list.extend('xiaoming')
# # 结果：['Tom', 'Lily', 'Rose', 'x', 'i', 'a', 'o', 'm', 'i', 'n', 'g']
# print(name_list)
# name_list = ['Tom', 'Lily', 'Rose']
# name_list.extend(['xiaoming', 'xiaohong'])
# # 结果：['Tom', 'Lily', 'Rose', 'xiaoming', 'xiaohong']
# print(name_list)
"""8,=====================================insert()：指定位置新增数据。"""
# name_list = ['Tom', 'Lily', 'Rose']
# name_list.insert(1, 'xiaoming')
# # 结果：['Tom', 'xiaoming', 'Lily', 'Rose']
# print(name_list)
"""9,====================================del============================"""
# name_list = ['Tom', 'Lily', 'Rose']
# del name_list[0]
# # 结果：['Lily', 'Rose']
# print(name_list)
"""10,===============================pop()：删除指定下标的数据(默认为最后⼀个)，并返回该数据"""
# name_list = ['Tom', 'Lily', 'Rose']
# del_name = name_list.pop(1)
# # 结果：Lily
# print(del_name)
# # 结果：['Tom', 'Rose']
# print(name_list)
"""11,=====================================remove()：移除列表中某个数据的第⼀个匹配项"""
# name_list = ['Tom', 'Lily', 'Rose']
# name_list.remove('Rose')
# # 结果：['Tom', 'Lily']
# print(name_list)
"""12,=================================clear()：清空列表"""
# name_list = ['Tom', 'Lily', 'Rose']
# name_list.clear()
# print(name_list) # 结果： []
"""13,======================================修改"""
# name_list = ['Tom', 'Lily', 'Rose']
# name_list[0] = 'aaa'
# # 结果：['aaa', 'Lily', 'Rose']
# print(name_list)
"""14,=======================================逆置：reverse()"""
# num_list = [1, 5, 2, 3, 6, 8]
# num_list.reverse()
# # 结果：[8, 6, 3, 2, 5, 1]
# print(num_list)
"""15,=======================================排序：sort()"""
# num_list = [1, 5, 2, 3, 6, 8]
# num_list.sort()
# # 结果：[1, 2, 3, 5, 6, 8]
# print(num_list)
""""16,====================================="函数：copy()"""
# name_list = ['Tom', 'Lily', 'Rose']
# name_li2 = name_list.copy()
# # 结果：['Tom', 'Lily', 'Rose']
# print(name_li2)
"""17,=======================================while list"""
# name_list = ['Tom', 'Lily', 'Rose']
# i = 0
# while i < len(name_list):
#  print(name_list[i])
#  i += 1
"""18,=======================================for list"""
# name_list = ['Tom', 'Lily', 'Rose']
# for i in name_list:
#  print(i)
"""19,======================================列表嵌套"""
# name_list = [['⼩明', '⼩红', '⼩绿'], ['Tom', 'Lily', 'Rose'], ['张三', '李四',
# '王五']]
# print(name_list[0][1])
"""========================================tuple操作==============================="""
# 多个数据元组
# t1 = (10, 20, 30)
# # 单个数据元组
# t2 = (10,)
# t2 = (10,)
# print(type(t2)) # tuple
# t3 = (20)
# print(type(t3)) # int
# t4 = ('hello')
# print(type(t4)) # str

# tuple1 = ('aa', 'bb', 'cc', 'bb')
# print(tuple1[0]) # aa
"""1,index()：查找某个数据，如果数据存在返回对应的下标，否则报错，语法和列表、字符串的index⽅法相同。"""
# tuple1 = ('aa', 'bb', 'cc', 'bb')
# print(tuple1.index('aa')) # 0
"""2,====================================count()：统计某个数据在当前元组出现的次数。"""
# tuple1 = ('aa', 'bb', 'cc', 'bb')
# print(tuple1.count('bb')) # 2
"""3,==========================================len()：统计元组中数据的个数"""
# tuple1 = ('aa', 'bb', 'cc', 'bb')
# print(len(tuple1)) # 4
"""4,============================================元组的数据不可以直接修改"""
# tuple2 = (10, 20, ['aa', 'bb', 'cc'], 50, 30)
# print(tuple2[2]) # 访问到列表
# # 结果：(10, 20, ['aaaaa', 'bb', 'cc'], 50, 30)
# tuple2[2][0] = 'aaaaa'
# print(tuple2)

"""================================dict{}字典常见操作，增加数据=============================="""

# dict1 = {'name': 'Rose', 'age': 20, 'gender': '男'}
# # 结果：{'name': 'Rose', 'age': 20, 'gender': '男'}
# print(dict1)
# dict1['id'] = 110
# # {'name': 'Rose', 'age': 20, 'gender': '男', 'id': 110}
# print(dict1)
"""1,=======================================删除数据============================"""

# dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
# del dict1['gender']
# # 结果：{'name': 'Tom', 'age': 20}
# print(dict1)
"""2,=======================================清空字典============================"""
# dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
# dict1.clear()
# print(dict1) # {}
"""3,========================================查询====================================="""
# dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
# print(dict1['name']) # Tom
# print(dict1['id']) # 报错
"""4,======================================get======================================="""
# dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
# print(dict1.get('name')) # Tom
# print(dict1.get('id', 110)) # 110
# print(dict1.get('id')) # None
"""5,======================================keys========================================"""
# dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
# print(dict1.keys()) # dict_keys(['name', 'age', 'gender'])
"""6,======================================values======================================="""
# dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
# print(dict1.values()) # dict_values(['Tom', 20, '男'])
"""7,=======================================items==============================================="""
# dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
# print(dict1.items())
# # dict_items([('name', 'Tom'), ('age', 20), ('gender','男')])
"""8,=====================================遍历字典的key================================================="""
# dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
# for key in dict1.keys():
#  print(key)
"""9,=====================================遍历value==================================================="""
# dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
# for value in dict1.values():
#     print(value)

"""10,====================================遍历字典的元素==============================================="""
# dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
# for item in dict1.items():
#     print(item)

"""11,====================================遍历键值对==================================================="""
# dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
# for key, value in dict1.items():
#  print(f'{key} = {value}')
"""12, =============================集合[set]======================================="""
# s1 = {10, 20, 30, 40, 50}
# print(s1)
# s2 = {10, 30, 20, 10, 30, 40, 30, 50}
# print(s2)
# s3 = set('abcdefg')
# print(s3)
# s4 = set()
# print(type(s4)) # set
# s5 = {}
# print(type(s5)) # dict
"""13,===========================add==========================="""
# s1 = {10, 20}
# s1.add(100)
# s1.add(10)
# print(s1) # {100, 10, 20}
"""14,==========================update(), 追加的数据是序列========================"""
# s1 = {10, 20}
# # s1.update(100) # 报错
# s1.update([100, 200])
# s1.update('abc')
# print(s1)
"""15,========================remove()，删除集合中的指定数据，如果数据不存在则报错======================"""

# s1 = {10, 20}
# s1.remove(10)
# print(s1)
# s1.remove(10) # 报错
# print(s1)
"""16,=======================discard()，删除集合中的指定数据，如果数据不存在也不会报错。================="""
# s1 = {10, 20}
# s1.discard(10)
# print(s1)
# s1.discard(10)
# print(s1)


"""17,=======================pop()，随机删除集合中的某个数据，并返回这个数据============================="""
# s1 = {10, 20, 30, 40, 50}
# del_num = s1.pop()
# print(del_num)
# print(s1)
"""18,=======================in：判断数据在集合序列not in：判断数据不在集合序列"""
# s1 = {10, 20, 30, 40, 50}
# print(10 in s1)
# print(10 not in s1)
"""===========================公共操作[+- *]=============================="""
"""运算符  +"""
# 1. 字符串
# str1 = 'aa'
# str2 = 'bb'
# str3 = str1 + str2
# print(str3) # aabb
# # 2. 列表
# list1 = [1, 2]
# list2 = [10, 20]
# list3 = list1 + list2
# print(list3) # [1, 2, 10, 20]
# # 3. 元组
# t1 = (1, 2)
# t2 = (10, 20)
# t3 = t1 + t2
# print(t3) # (10, 20, 100, 200)
"""  *  """
"""1,=============================================[+,*]==============================="""
# print('-' * 10) # ----------
# # 2. 列表
# list1 = ['hello']
# print(list1 * 4) # ['hello', 'hello', 'hello', 'hello']
# # 3. 元组
# t1 = ('world',)
# print(t1 * 4) # ('world', 'world', 'world', 'world')
"""2,==========================================in或not in======================================="""
# # 1. 字符串
# print('a' in 'abcd') # True
# print('a' not in 'abcd') # False
# # 2. 列表
# list1 = ['a', 'b', 'c', 'd']
# print('a' in list1) # True
# print('a' not in list1) # False
# # 3. 元组
# t1 = ('a', 'b', 'c', 'd')
# print('aa' in t1) # False
# print('aa' not in t1) # True
"""3,========================================len================================"""
# 1. 字符串
# str1 = 'abcdefg'
# print(len(str1)) # 7
# # 2. 列表
# list1 = [10, 20, 30, 40]
# print(len(list1)) # 4
# # 3. 元组
# t1 = (10, 20, 30, 40, 50)
# print(len(t1)) # 5
# # 4. 集合
# s1 = {10, 20, 30}
# print(len(s1)) # 3
# # 5. 字典
# dict1 = {'name': 'Rose', 'age': 18}
# print(len(dict1)) # 2

"""4,=========================================del()================================="""
# 1. 字符串
# str1 = 'abcdefg'
# del str1
# print(str1)
# # 2. 列表
# list1 = [10, 20, 30, 40]
# del(list1[0])
# print(list1) # [20, 30, 40]

"""5,==========================================max()============================="""
# 1. 字符串
# str1 = 'abcdefg'
# print(max(str1)) # g
# # 2. 列表
# list1 = [10, 20, 30, 40]
# print(max(list1)) # 40

"""6,========================================min()======================================"""
# # 1. 字符串
# str1 = 'abcdefg'
# print(min(str1)) # a
# # 2. 列表
# list1 = [10, 20, 30, 40]
# print(min(list1)) # 10


"""7,========================================range()======================================"""

# # 1 2 3 4 5 6 7 8 9
# for i in range(1, 10, 1):
#  print(i)
# # 1 3 5 7 9
# for i in range(1, 10, 2):
#  print(i)
# # 0 1 2 3 4 5 6 7 8 9
# for i in range(10):
#  print(i)


"""7,====================================enumerate()enumerate(可遍历对象, start=0)"""

# list1 = ['a', 'b', 'c', 'd', 'e']
# for i in enumerate(list1):
#  print(i)
# for index, char in enumerate(list1, start=1):
#  print(f'下标是{index}, 对应的字符是{char}')


"""8,====================================容器类型转换touple()=================================="""

# list1 = [10, 20, 30, 40, 50, 20]
# s1 = {100, 200, 300, 400, 500}
# print(tuple(list1))
# print(tuple(s1))
"""9,==========================================2 list()====================================================="""

# t1 = ('a', 'b', 'c', 'd', 'e')
# s1 = {100, 200, 300, 400, 500}
# print(list(t1))
# print(list(s1))


"""10,===========================================set()================================================="""

# list1 = [10, 20, 30, 40, 50, 20]
# t1 = ('a', 'b', 'c', 'd', 'e')
# print(set(list1))
# print(set(t1))

"""11, ===========================================推导式=================================================="""
# list1 = [i for i in range(0, 10, 2)]
# print(list1)
# list1 = [i for i in range(10) if i % 2 == 0]
# print(list1)
# list1 = [(i, j) for i in range(1, 3) for j in range(3)]
# print(list1)

# dict1 = {i: i**2 for i in range(1, 5)}
# print(dict1) # {1: 1, 2: 4, 3: 9, 4: 16}

# list1 = ['name', 'age', 'gender']
# list2 = ['Tom', 20, 'man']
# dict1 = {list1[i]: list2[i] for i in range(len(list1))}
# print(dict1)
#
# counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}
# # 需求：提取上述电脑数量⼤于等于200的字典数据
# count1 = {key: value for key, value in counts.items() if value >= 200}
# print(count1)  # {'MBP': 268, 'DELL': 201}
# list1 = [1, 1, 2]
# set1 = {i ** 2 for i in list1}
# print(set1)  # {1, 4}
"""12,==================================函数,包裹关键字参数传递============================"""
# def user_info(**kwargs):
# print(kwargs)
# # {'name': 'TOM', 'age': 18, 'id': 110}
# user_info(name='TOM', age=18, id=110)
"""13,==================================拆包==============================="""
# def return_num():
#     return 100, 200
#
#
# num1, num2 = return_num()
# print(num1)  # 100
# print(num2)  # 200
"""14,===============================字典================================="""
# dict1 = {'name': 'TOM', 'age': 18}
# a, b = dict1
# # 对字典进⾏拆包，取出来的是字典的key
# print(a) # name
# print(b) # age
# print(dict1[a]) # TOM
# print(dict1[b]) # 18

"""15,=======================不定长参数============================"""
# def user_info(*args):
#     print(args)
#
#
# # ('TOM',)
# user_info('TOM')
# # ('TOM', 18)
# user_info('TOM', 18)
"""15,==============================lambda的参数形式==========================="""
# fn1 = lambda: 100
# print(fn1())
# fn1 = lambda a: a
# print(fn1('hello world'))
# fn1 = lambda a, b, c=100: a + b + c
# print(fn1(10, 20))
# fn1 = lambda *args: args
# print(fn1(10, 20, 30))

"""fn1 = lambda a, b: a if a > b else b
# print(fn1(1000, 500))
"""
# students = [
#  {'name': 'TOM', 'age': 20},
#  {'name': 'ROSE', 'age': 19},
# {'name': 'Jack', 'age': 22}
# ]
"""15,==========================================按name值升序排列"""
# students.sort(key=lambda x: x['name'])
# print(students)
"""16,==========================================按name值降序排列"""
# students.sort(key=lambda x: x['name'], reverse=True)
# print(students)
"""17,==========================================按age值升序排列"""
# students.sort(key=lambda x: x['age'])
# print(students)
"""18,======================================map==========================="""
# list1 = [1, 2, 3, 4, 5]
# def func(x):
#  return x ** 2
# result = map(func, list1)
# print(result) # <map object at 0x0000013769653198>
# print(list(result)) # [1, 4, 9, 16, 25]
"""18,============================reduce====================================="""
# import functools
#
# list1 = [1, 2, 3, 4, 5]
#
#
# def func(a, b):
#     return a + b
#
#
# result = functools.reduce(func, list1)
# print(result)  # 15
"""19,========================================filter===================================="""
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# def func(x):
#     return x % 2 == 0
#
#
# result = filter(func, list1)
# print(result)  # <filter object at 0x0000017AF9DC3198>
# print(list(result))  # [2, 4, 6, 8, 10]

"""20,=========================================高阶函数========================================="""
# def sum_num(a, b, f):
#  return f(a) + f(b)
# result = sum_num(-7, 2, abs)
# print(result) # 3

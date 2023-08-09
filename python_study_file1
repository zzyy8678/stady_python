
# -- coding: utf-8 --

import random
from datetime import datetime
from functools import reduce
from sys import argv
from sys import exit
from random import randint
from sys import exit
from random import randint
import random
from functools import reduce
from sys import argv
from sys import exit
from random import randint

from sys import exit
from random import randint

print(3 + 2 < 5 - 7)
print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)
print("What is 3 + 2?", 3 + 2)
my_name = 'Zed A. Shaw'
print("Let's talk about %s." % my_name)
my_height = 74
print("He's %d inches tall." % my_height)
my_eyes = 'Blue'
my_hair = 'Brown'
print("He's got %s eyes and %s hair." % (my_eyes, my_hair))

x = "There are %d types of people." % 10

print("I said: %r." % x)
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
print("How old are you?")
age = input("请输入：")
print("How tall are you?")
height = input("请输入：")
print("How much do you weigh?")
weight = input("请输入：")

print("So, you're %r old, %r tall and %r heavy." % (
    age, height, weight))
age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weigh? ")

print("So, you're %r old, %r tall and %r heavy." % (
    age, height, weight))


script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
def print_two(*args):
    arg1, arg2 = args
    print("arg1: %r, arg2: %r" % (arg1, arg2))


print_two("aa", "你好")

#
def print_two_again(arg1, arg2):
    print("arg1: %r, arg2: %r" % (arg1, arg2))


print_two_again("你好", "在吗？")
script, input_file = argv


def print_all(f):
    print("++++++++++++" + f.read())  # 读取文件内容


def rewind(f):
    f.seek(0)


def print_a_line(line_count, f):
    print(line_count, f.readline())


current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)  # 传递一个文件名称
#############################################################
print("******************Now let's rewind, kind of like a tape.*************")
rewind(current_file)

print("Let's print three lines:")

current_line = 1
print("11111111111111111111")
print_a_line(current_line, current_file)
current_line = current_line + 1
print("222222222222222222222222222")
print_a_line(current_line, current_file)
print("33333333333333333333333333333333")
current_line = current_line + 1
print_a_line(current_line, current_file)
def add(a, b):
    print("ADDING %d + %d" % (a, b))
    return a + b


def subtract(a, b):
    print("SUBTRACTING %d - %d" % (a, b))
    return a - b


def multiply(a, b):
    print("MULTIPLYING %d * %d" % (a, b))
    return a * b


def divide(a, b):
    print("DIVIDING %d / %d" % (a, b))
    return a / b


print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
print("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))
print("Here is a puzzle.")
# subtract(a, b):multiply(a, b):   weight=180,25   35+(74-180*25)
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    print(words)
    return words


def sort_words(words):
    """Sorts the words."""
    print(sorted(words))
    return sorted(words)


def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)


def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)


def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


sentence = "All good things come to those who wait."
words = break_words(sentence)
sort_words(words)
print_first_word(words)
print_last_word(words)
sort_sentence(sentence)
print_first_and_last(sentence)
print_first_and_last_sorted(sentence)
print(3 < 2)
print("Roosters", 100 - 25 * 3 % 4)
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)
print(help(random))#获取文档帮助信息
formatter = "%r %r %r %r"
formatters = "%s %s %s %s"
print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two", "three", "four"))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatters % (1, 2, 3, 4))
print(formatters % ("one", "two", "three", "four"))
print(formatters % (True, False, False, True))
print(formatters % (formatter, formatter, formatter, formatter))
print(formatters % ("I had this thing.",
                    "That you could type up right.",
                    "But it didn't sing.",
                    "So I said goodnight."))
#
d = datetime.date.today()
print('%s' % d)

print('%r' % d)

x = "weiruoyu"
y = 25.66

print("%s" % x)

print("%s" % y)



print("%r" % x)

print("%r" % y)

print("%d" % y)

print("%d" % x)


days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
print("Here are the days: ", days)
print("Here are the months: ", months)
print("""
There's something going on here. With the three double-quotes.
 We'll be able to type as much as we like. Even 4 lines if we want, or 5, or 6. """)
"""转义字符"""
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = """ I'll do a list: \t* Cat food \t* Fishies
\t* Catnip\n\t* Grass """
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
"""键盘输入传递参数"""
print("How old are you?")
age = input()
print("How tall are you?", )
height = input()
print("How much do you weigh?", )
weight = input()
print("So, you're %r old, %r tall and %r heavy." % (age, height, weight))
"""输入提示信息"""
y = input("Name? ")
age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weigh? ")
print("So, you're %r old, %r tall and %r heavy." % (age, height, weight))
"""参数、解包、变量"""
script, first, second, third = argv
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
script, user_name = argv
prompt = '> '
print("Hi %s, I'm the %s script." % (user_name, script))
print("I'd like to ask you a few questions.")
print("Do you like me %s?" % user_name)
likes = input(prompt)
print("Where do you live %s?" % user_name)
lives = input(prompt)
print("What kind of computer do you have?")
computer = input(prompt)
print("""
Alright, so you said %r about liking me.
 You live in %r. Not sure where that is.
 And you have a %r computer. Nice.""" % (likes, lives, computer))
script, filename = argv
txt = open(filename)
print("Here's your file %r:" % filename)
print(txt.read())
print("Type the filename again:")
file_again = input("> ")
txt_again = open(file_again)
print(txt_again.read())
"""读写文件"""
script, filename = argv
print("We're going to erase %r." % filename)
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
input("?")
print("Opening the file...")
target = open(filename, 'w')
print("Truncating the file. Goodbye!")
target.truncate()
print("Now I'm going to ask you for three lines.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
print("I'm going to write these to the file.")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
print("And finally, we close it.")
target.close()
"""文件拷贝的"""
from sys import argv
from os.path import exists

script, from_file, to_file = argv
print("Copying from %s to %s" % (from_file, to_file))
# we could do these two on one line too, how?
input = open(from_file)
indata = input.read()
print("The input file is %d bytes long" % len(indata))
print("Does the output file exist? %r" % exists(to_file))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()
output = open(to_file, 'w')

output.write(indata)
print("Alright, all done.")
output.close()
input.close()
"""命名、变量、代码、函数
this one is like your scripts with argv"""
def print_two(*args):
    arg1, arg2 = args
    print("arg1: %r, arg2: %r" % (arg1, arg2))
    # ok, that *args is actually pointless, we can just do this


def print_two_again(arg1, arg2):
    print("arg1: %r, arg2: %r" % (arg1, arg2))


# this just takes one argument
def print_one(arg1):
    print("arg1: %r" % arg1)
#
#
# this one takes no arguments
def print_none():
    print("I got nothin'.")


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
"""函数和变量"""
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have %d cheeses!" % cheese_count)
    print("You have %d boxes of crackers!" % boxes_of_crackers)
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
"""函数和文件"""
script, input_file = argv

#
def print_all(f):
    print(f.read())


def rewind(f):
    f.seek(0)


def print_a_line(line_count, f):
    print(line_count, f.readline())


current_file = open(input_file)
print("First let's print the whole file:\n")

print_all(current_file)
print("Now let's rewind, kind of like a tape.")

rewind(current_file)
print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
"""函数可以返回东西"""
def add(a, b):
    print("ADDING %d + %d" % (a, b))
    return a + b


def subtract(a, b):
    print("SUBTRACTING %d - %d" % (a, b))
    return a - b


def multiply(a, b):
    print("MULTIPLYING %d * %d" % (a, b))
    return a * b


def divide(a, b):
    print("DIVIDING %d / %d" % (a, b))
    return a / b


print("Let's do some math with just functions!")
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))

# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print ("That becomes: ", what, "Can you do it by hand?")
print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')
poem = """ \tThe lovely world with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation \n\t\twhere there is none. """
print("--------------")
print(poem)
print("--------------")
five = 10 - 2 + 3 - 6
print("This should be five: %s" % five)


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)
print("With a starting point of: %d" % start_point)
print("We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates))
start_point = start_point / 10
print("We can also do that this way:")
print("We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point))
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words


def sort_words(words):
    """Sorts the words."""
    return sorted(words)


def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)


def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)


def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    print(sort_words(words))
    return sort_words(words)


def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
#
#
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


sentence = "All good things come to those who wait."
break_words(sentence)
print_first_word(break_words(sentence))  # 取出第一个元素
print_last_word(break_words(sentence))  # 取出最后一个元素
sort_sentence(sentence)
print_first_and_last(sentence)
print_first_and_last_sorted(sentence)
"""布尔表达式练习"""
people = 20
cats = 30
dogs = 15
if people < cats:
    print("Too many cats! The world is doomed!")
if people > cats:
    print("Not many cats! The world is saved!")
if people < dogs:
    print("The world is drooled on!")
if people > dogs:
    print("The world is dry!")
dogs += 5
if people >= dogs:
    print("People are greater than or equal to dogs.")
if people <= dogs:
    print("People are less than or equal to dogs.")
if people == dogs:
    print("People are dogs.")
people = 30
cars = 40
buses = 15
if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
if buses > cars:
    print("That's too many buses.")
elif buses < cars:
    print("Maybe we could take the buses.")
else:
    print("We still can't decide.")
if people > buses:
    print("Alright, let's just take the buses.")
else:
    print("Fine, let's stay home then.")
print("You enter a dark room with two doors. Do you go through door #1 or door #2?")
door = input("> ")
if door == "1":
    print("There's a giant bear here eating a cheese cake. What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
    bear = input("> ")
    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print("Well, doing %s is probably better. Bear runs away." % bear)
elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")
    insanity = input("> ")
    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello. Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck. Good job!")
else:
    print("You stumble around and fall on a knife and die. Good job!")
"""循环和列表"""
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
# this first kind of for-loop goes through a list
for number in the_count:
    print("This is count %d" % number)
# same as above
for fruit in fruits:
    print("A fruit of type: %s" % fruit)
# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print("I got %r" % i)
elements = []
# elements = range(0, 6)

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print ("Adding %d to the list." % i)
# append is a function that lists understand
    elements.append(i)
# # now we can print them out too
for i in elements:
    print ("Element was: %d" % i)
"""首先简单的说一下append,extend与insert的区别
append是在列表后面直接添加你输入的数据，就算是列表或字典，也直接添加进去，比较死板

extend是在列表后面添加数据，如果添加的是列表或字典亦或者是字符串，都会会拆分并添加进去，但是这仅限一元的情况下,多元仅会拆分一个最大的列表再添加进去

insert是在列表中某个下标的前面添加单个数据，要带至少两个参数，添加的方法和append相同
1:append
list_1 = ['0','1','2','3','4']
data_str = 'abc'
data_list = ['abc','bcd','cdf','dfg']
data_list_n = [['abc','bcd'],['cdf','dfg']]
data_dict = {'qwe','wer','ert'}
list_1.append(data_str)
print(list_1)
['0', '1', '2', '3', '4', 'abc']
list_1.append(data_list)
print(list_1)
['0', '1', '2', '3', '4', ['abc', 'bcd', 'cdf', 'dfg']]
list_1.append(data_dict)
print(list_1)
['0', '1', '2', '3', '4', {'wer', 'ert', 'qwe'}]
2:extend
list_1 = ['0','1','2','3','4']
data_str = 'abc'
data_list = ['abc','bcd','cdf','dfg']
data_list_n = [['abc','bcd'],['cdf','dfg']]
data_dict = {'qwe','wer','ert'}

list_1.extend(data_str)
print(list_1)
['0', '1', '2', '3', '4', 'a', 'b', 'c']
list_1.extend(data_list)
print(list_1)
['0', '1', '2', '3', '4', 'abc', 'bcd', 'cdf', 'dfg']
list_1.extend(data_list_n)
print(list_1)
list_1.extend(data_dict)
print(list_1)
['0', '1', '2', '3', '4', 'qwe', 'ert', 'wer']
3:insert
list_1 = ['0','1','2','3','4']
data_str = 'abc'
data_list = ['abc','bcd','cdf','dfg']
data_list_n = [['abc','bcd'],['cdf','dfg']]
data_dict = {'qwe','wer','ert'}
list_1.insert(0,data_str)
print(list_1)
['abc', '0', '1', '2', '3', '4']
list_1.insert(0,data_list)
print(list_1)
[[['abc', 'bcd'], ['cdf', 'dfg']], '0', '1', '2', '3', '4']
list_1.insert(0,data_dict)
print(list_1)
[{'qwe', 'ert', 'wer'}, '0', '1', '2', '3', '4']
https://blog.csdn.net/gghhm/article/details/98309602
"""

"""While 循环"""
def demo(now):
    i = 0
    numbers = []
    while i < now:
        print("At the top i is %d" % i)
        numbers.append(i)
        i += 1
        print("Numbers now: ", numbers)
        print("At the bottom i is %d" % i)
    print("The numbers: ")
    for num in numbers:
        print(num)


demo(7)
def test(new):
    #   i=0
    numbers = []
    for i in range(0, 11):
        if i < new:
            print("At the top i is %d" % i)
            numbers.append(i)
    for num in numbers:
        print(num)


test(10)
"""访问列表的元素"""
ten_things = "Apples Oranges Crows Telephone Light Sugar Apples"
print("Wait there's not 10 things in that list, let's fix that.")
stuff = ten_things.split(' ')
print(stuff)
"""删除一个元素,具体的元素"""
stuff.remove("Crows")
print(stuff)

aa = stuff.pop(1)
print("删除的元素为:" + aa)
print(stuff)

del stuff[0]  # del还可以删除指定范围内的值  [2:4] #删除从第2个元素开始，到第4个为止的元素(但是不包括尾部元素)
print(stuff)


"""统计元素的个数"""
cc = stuff.count("Apples")
print(cc)
# 追加一个元素append() 方法向列表的尾部添加一个新的元素。只接受一个参数
stuff.append("next_one")
print(stuff)
stuff.insert(2, "Desktop")
print(stuff)
cc = ['aa', 'bb', 'cc', 'dd']
ss = stuff.extend(cc)  # extend()方法只接受一个列表作为参数，并将该参数的每个元素都添加到原有的列表中。也是只接受一个参数。
print(ss)

print("###############################")
dd = stuff.copy()
print(dd)
stuff.reverse()
print(stuff)
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
while len(stuff) != 10:
    next_one = more_stuff.pop()  # 默认从最后一个取值
    print("Adding: ", next_one)
    stuff.append(next_one)
    print("There's %d items now." % len(stuff))
print("There we go: ", stuff)
print("Let's do some things with stuff.")
# 按照下标取值
print("这个是" + stuff[0])
print("这个是" + stuff[-1])


print(stuff)
# whoa! fancy
print(stuff.pop())
print(','.join(stuff))
dd =','.join(stuff)
print(type(dd))
print(' '.join(stuff))
print('#'.join(stuff[3:5])) # 左边是第四个元素下标是3，右边是地四个元素,下标为5
things = ['a', 'b', 'c', 'd']
print(things[1])
things[1] = 'z'
print(things[1])
print(things)
stuff = {'name': 'Zed', 'age': 36, 'height': 6 * 12 + 2}
print(stuff['name'])
print(stuff['age'])
stuff['city'] = "San Francisco"
print(stuff)
stuff[1] = "Wow"
stuff[2] = "Neato"
print(stuff)
del stuff['city']
del stuff[1]
del stuff[2]
print(stuff)
cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville'}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print(cities)


def find_city(city_dict, state):
    if state in city_dict:  # 如果state在这个字典中存在
        print(city_dict)
        print("++++++++++" + city_dict[state])
        return city_dict[state]
    else:
        return "Not found."


# ok pay attention!
while True:
    print("State? (ENTER to quit)")
    state = input("> ")
    if not state:
        break
    # this line is the most important ever! study!
    city_found = find_city(cities, state)  # 这个函数要传递2个参数
    print(city_found)
cities['_find'] = find_city  # 把这个函数做为一个变量放到字典中，标记为‘_find’,知道 find_city 是在字典中 _find 的位置
city_found = cities['_find'](cities, state)  # city_found = 于是知道了需要创建一个变量。
"""
然后它读到 cities ，然后知道了它是一个字典
然后看到了 ['_find'] ，于是 Python 就从索引找到了字典 cities 中对应的位置，并且获取了该位置的内
['_find'] 这个位置的内容是我们的函数 find_city ，所以 Python 就知道了这里表示一个函数，于是当它碰到 ( 就开始了函数调用。
cities, state 这两个参数将被传递到函数 find_city 中，然后这个函数就被运行
find_city 接着从 cities 中寻找 states ，并且返回它找到的内容，如果什么都没找到，就返回一个信息说它什么都没找
find_city 接受返回的信息，最后将该信息赋值给一开始的 city_found 这个变量
"""

def death():
    quips = ["You died. You kinda suck at this.",
             "Nice job, you died ...jackass.",
             "Such a luser.",
             "I have a small puppy that's better at this."]
    print(quips[randint(0, len(quips) - 1)])
    exit(1)


def central_corridor():
    print("The Gothons of Planet Percal #25 have invaded your ship and destroyed")
    print("your entire crew. You are the last surviving member and your last")
    print("mission is to get the neutron destruct bomb from the Weapons Armory,")
    print("put it in the bridge, and blow the ship up after getting into an ")
    print("escape pod.")
    print("\n")
    print("You're running down the central corridor to the Weapons Armory when")
    print("a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume")
    print("flowing around his hate filled body. He's blocking the door to the")
    print("Armory and about to pull a weapon to blast you.")
    action = input("请输入： ")
    if action == "shoot!":
        print("Quick on the draw you yank out your blaster and fire it at the Gothon.")
        print("His clown costume is flowing and moving around")
        print("off your aim. Your laser hits his costume but misses him entirely. This")
        print("completely ruins his brand new costume his mother bought him, which")
        print("makes him fly into an insane rage and blast you repeatedly in the face until")
        print("you are dead. Then he eats you.")
        return 'death'
    elif action == "dodge!":
        print("Like a world class boxer you dodge, weave, slip and slide right")
        print("as the Gothon's blaster cranks a laser past your head.")
        print("In the middle of your artful dodge your foot slips and you")
        print("bang your head on the metal wall and pass out.")
        print("You wake up shortly after only to die as the Gothon stomps on")
        print("your head and eats you.")
        return 'death'
    elif action == "tell a joke":
        print("Lucky for you they made you learn Gothon insults in the academy.")
        print("You tell the one Gothon joke you know:")
        print("Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr.")
        print("The Gothon stops, tries not to laugh, then busts out laughing and can't move.")
        print("While he's laughing you run up and shoot him square in the head")
        print("putting him down, then jump through the Weapon Armory door.")
        return 'laser_weapon_armory'
    else:
        print("DOES NOT COMPUTE!")
    return 'central_corridor'
#
#

#
def the_bridge():
    print("You burst onto the Bridge with the neutron destruct bomb")
    print("under your arm and surprise 5 Gothons who are trying to")
    print("take control of the ship. Each of them has an even uglier")
    print("clown costume than the last. They haven't pulled their")
    print("weapons out yet, as they see the active bomb under your")
    print("arm and don't want to set it off.")
    action = input("> ")
    if action == "throw the bomb":
        print("In a panic you throw the bomb at the group of Gothons")
        print("and make a leap for the door. Right as you drop it a")
        print("Gothon shoots you right in the back killing you.")
        print("As you die you see another Gothon frantically try to disarm")
        print("the bomb. You die knowing they will probably blow up when")
        print("it goes off.")
        return 'death'
    elif action == "slowly place the bomb":
        print("You point your blaster at the bomb under your")
        print("and the Gothons put their hands up and start to sweat.")
        print("You inch backward to the door, open it, and then carefully")
        print("place the bomb on the floor, pointing your blaster at it.")
        print("You then jump back through the door, punch the close button")
        print("and blast the lock so the Gothons can't get out.")
        print("Now that the bomb is placed you run to the escape pod to")
        print("get off this tin can.")
        return 'escape_pod'
    else:
        print("DOES NOT COMPUTE!")
        return "the_bridge"


def escape_pod():
    print("You rush through the ship desperately trying to make it to")
    print("the escape pod before the whole ship explodes. It seems like")
    print("hardly any Gothons are on the ship, so your run is clear of")
    print("interference. You get to the chamber with the escape pods, and")
    print("now need to pick one to take. Some of them could be damaged")
    print("but you don't have time to look. There's 5 pods, which one")
    print("do you take?")
    good_pod = randint(1, 5)
    guess = input("[pod #]> ")
    if int(guess) != good_pod:
        print("You jump into pod %s and hit the eject button." % guess)
        print("The pod escapes out into the void of space, then")
        print("implodes as the hull ruptures, crushing your body")
        print("into jam jelly.")
        return 'death'
    else:
        print("You jump into pod %s and hit the eject button." % guess)
        print("The pod easily slides out into space heading")
        print("the planet below. As it flies to the planet, you look")
        print("back and see your ship implode then explode like a")
        print("bright star, taking out the Gothon ship at the same")
        print("time. You won!")
        exit(0)


ROOMS = {'death': death, 'central_corridor': central_corridor, 'laser_weapon_armory': "",
         'the_bridge': the_bridge, 'escape_pod': escape_pod}


def runner(map, start):
    next = start
    while True:
        room = map[next]
        print("\n--------")
        next = room()


runner(ROOMS, 'central_corridor')

stuff = ['Test', 'This', 'Out']
print(' '.join(stuff))


class TheThing(object):
    def __init__(self):
        self.number = 0

    def some_function(self):
        print("I got called.")

    def add_me_up(self, more):
        self.number += more
        return self.number

#
# two different things
a = TheThing()
b = TheThing()
a.some_function()
b.some_function()
print(a.add_me_up(20))
print(a.add_me_up(20))
print(b.add_me_up(30))
print(b.add_me_up(30))
print(a.number)
print(b.number)
# Animal is-a object (yes, sort of confusing) look at the extra credit

class Animal(object):
    pass

#
class Dog(Animal):
    def __init__(self, name):
        self.name = name


class Cat(Animal):
    def __init__(self, name):
        self.name = name


class Person(object):
    def __init__(self, name):
        self.name = name  # Person has-a pet of some kind self.pet = None


class Employee(Person):
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary


class Fish(object):
    pass


class Salmon(Fish):
    pass


class Halibut(Fish):
    pass


rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")
mary.pet = satan
frank = Employee("Frank", 120000)
frank.pet = rover
flipper = Fish()
crouse = Salmon()
harry = Halibut()
for sss in 'Python':  # 第一个实例
    if sss == 'Python':
        continue
    print('当前字母 :',sss)
var = 10
"""9,8的时候就不执行后面的打印的，继续执行返回去执行条件了，
7,6，5的时候就不执行后面的打印的，继续执行返回去执行条件了
continue 语句是一个删除的效果，他的存在是为了删除满足循环条件下的某些不需要的成分:"""
while var > 0:
    var = var - 1
    if var == 5 or var == 8:
        continue
    print('当前值 :', var)
print("Good bye!=====================================")
var = 10  # 第二个实例
while var > 0:
    print('当前变量值 :', var)
    var = var - 1
    if var == 5:  # 当变量 var 等于 5 时退出循环,后面的就木有了
        break

print("Good bye!")

"""输出 Python 的每个字母"""
"""Python pass 是空语句，是为了保持程序结构的完整性。

pass 不做任何事情，一般用做占位语句。

Python 语言 pass 语句语法格式如下："""
for i in 'Python':
    print(i)
    if i == 'h':
        pass
        print('这是 pass 块')
    print('当前字母 :', i)

# print("Good bye!")
"""字符串截取单个字符"""
var1 = 'Hello World!'
var2 = "Python Runoob"

print("var1[0]: ", var1[0])
print("var2[1:5]: ", var2[1:5])  # 从第一个开始截取
"""列表元素截取"""
var1 = 'Hello World!'
print("输出 :- ", var1[:6] + 'Runoob!')
#list
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]
print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[0:5])
"""列表更新"""
list = []          ## 空列表
list.append('Google')   ## 使用 append() 添加元素
list.append('Runoob')
print(list)


"""列表删除，下标"""
list1 = ['physics', 'chemistry', 1997, 2000]

print(list1)
del list1[2]
print("After deleting value at index 2 : ")
print(list1)
"""访问元组"""
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)

print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])
"""修改元组，默认是不可以修改的"""
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# 以下修改元组元素操作是非法的。
# tup1[0] = 100

# 创建一个新的元组
tup3 = tup1 + tup2
print(tup3)
"""删除元组"""
tup = ('physics', 'chemistry', 1997, 2000)
print(tup)
del tup
print("After deleting tup : ")
print(tup)

print('abc', -4.24e93, 18 + 6.6j, 'xyz')
x, y = 1, 2
print("Value of x , y : ", x, y)
"""字典"""
tinydict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print("tinydict['Name']: ", tinydict['Name'])
print("tinydict['Age']: ", tinydict['Age'])

"""修改字典"""

tinydict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
#
tinydict['Age'] = 8  # 更新
tinydict['School'] = "RUNOOB"  # 添加

print("tinydict['Age']: ", tinydict['Age'])
print("tinydict['School']: ", tinydict['School'])
print('Name' in tinydict)


l = list(range(10)[1::2])
print(l)
for i in range(len(l)):
    print(i)
    l[i] = 0
print(l)
class Employee:
    """'所有员工的基类'"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


persion = Employee("李伟", "李宁")
persion.displayCount()
persion.displayEmployee()
class Test:
    def prt(runoob):
        print(runoob)
        print(runoob.__class__)


t = Test()
t.prt()
class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


"创建 Employee 类的第一个对象"
emp1 = Employee("Zara", 2000)
"创建 Employee 类的第二个对象"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empCount)
emp1.age = 7  # 添加一个 'age' 属性
emp1.age = 8  # 修改 'age' 属性
emp2.displayEmployee()
del emp1.age  # 删除 'age' 属性
print(hasattr(emp1, 'age'))    # 如果存在 'age' 属性返回 True。
print(getattr(emp1, 'age'))    # 返回 'age' 属性的值
setattr(emp1, 'age', 8) # 添加属性 'age' 值为 8
print(getattr(emp1, 'age'))
delattr(emp1, 'age')    # 删除属性 'age'
print(hasattr(emp1, 'age'))
class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)
p=Employee("李倩",9000)
p.displayEmployee()
p.displayCount()
class Parent:  # 定义父类
    parentAttr = 100

    def __init__(self):
        print("调用父类构造函数")

    def parentMethod(self,age,name):
        self.age=age
        self.name=name
        print('调用父类方法',self.age,self.name)

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("父类属性 :", Parent.parentAttr)


class Child(Parent):  # 定义子类
    def __init__(self):
        print("调用子类构造方法")

    def childMethod(self,name,age):
        self.name=name
        self.age=age
        print('调用子类方法',self.age,self.name)


c = Child()  # 实例化子类
c.childMethod("李倩","99")  # 调用子类的方法
c.parentMethod("李宁","90")  # 调用父类方法
c.setAttr(200)  # 再次调用父类的方法 - 设置属性值
c.getAttr()  # 再次调用父类的方法 - 获取属性值
class Parent:  # 定义父类
    def myMethod(self, name, age):
        self.age=age
        self.name=name
        print('调用父类方法',self.age,self.name)
#
#
# class Child(Parent):  # 定义子类
#     def myMethod(self,age,name,sex):
#         self.age = age
#         self.name = name
#
#         self.sex=sex
#         print('调用子类方法',self.sex,self.age,self.name)


# c = Child()  # 子类实例
# c.myMethod("李宁","nihai",99)  # 子类调用重写方法
# b=Parent()
# b.myMethod("李宁",98)
# class Vector:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __str__(self):
#         return 'Vector (%d, %d)' % (self.a, self.b) # 2 1
#
#     def __add__(self, other):
#         return Vector(self.a + other.a, self.b + other.b) # 2+5  1- -2=-1
#
#
# v1 = Vector(2, 10)
# v2 = Vector(5, -2)
# print(v1 + v2)
# class JustCounter:
#     __secretCount = 0  # 私有变量
#     publicCount = 0  # 公开变量
#
#     def count(self):
#         self.__secretCount += 1
#         self.publicCount += 1
#         print(self.__secretCount)


# counter = JustCounter()
# counter.count()  # 1
# counter.count() # 2
# print(counter.publicCount) # 2
# print(counter.__secretCount) # 报错，实例不能访问私有变量

# class Runoob:
#     __site = "www.runoob.com"
#
# runoob = Runoob()
# print(runoob._Runoob__site)
# import re
# print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
# print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配

# import re
#
# line = "Cats are smarter than dogs"
#
# matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
#
# if matchObj:
#     print("matchObj.group() : ", matchObj.group())
#     print("matchObj.group(1) : ", matchObj.group(1))
#     print("matchObj.group(2) : ", matchObj.group(2))
# else:
#     print("No match!!")
#
# import re
# print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
# print(re.search('com', 'www.runoob.com').span())         # 不在起始位置匹配
# import re
#
# line = "Cats are smarter than dogs";
#
# matchObj = re.match(r'dogs', line, re.M | re.I)
# if matchObj:
#     print("match --> matchObj.group() : ", matchObj.group())
# else:
#     print("No match!!")
#
# matchObj = re.search(r'dogs', line, re.M | re.I)
# if matchObj:
#     print("search --> searchObj.group() : ", matchObj.group())
# else:
#     print("No match!!")
"""re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；
    而re.search匹配整个字符串，直到找到一个匹配。"""
#
# import re
#
# phone = "2004-959-559 # 这是一个国外电话号码"
#
# # 删除字符串中的 Python注释
# num = re.sub(r'#.*$', "", phone)
# print("电话号码是: ", num)
#
# # 删除非数字(-)的字符串
# num = re.sub(r'\D', "", phone)
# print("电话号码是 : ", num)
import re


# 将匹配的数字乘以 2
def double(matched):
    value = int(matched.group('value'))
    print(value)
    return str(value * 2)


s = 'A23G4HFD567'
"""检索和替换
Python 的 re 模块提供了re.sub用于替换字符串中的匹配项
double函数的到返回值是46,8,567*2=1134 ,然后替换掉原来的
re.sub(pattern, repl, string, count=0, flags=0)
pattern : 正则中的模式字符串。
repl : 替换的字符串，也可为一个函数。
string : 要被查找替换的原始字符串。
count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。"""
# print(re.sub('(?P<value>\d+)', double, s))
# import re
#
# pattern = re.compile(r'\d+')  # 用于匹配至少一个数字
# # m = pattern.match('one12twothree34four')        # 查找头部，没有匹配
# # print (m)
# # #
# # m = pattern.match('one12twothree34four', 2, 10) # 从'e'的位置开始匹配，没有匹配
# # print(m)
#
# m = pattern.match('one12twothree34four', 3, 10)  # 从'1'的位置开始匹配，正好匹配
# print(m)
# # 返回一个 Match 对象
# if re.search("12",m.string):
#     print("yes")
# else:
#     print("no")
# # <_sre.SRE_Match object at 0x10a42aac0>
# print("==========="+m.group())
#
# print("start=========="+str(m.start()))
#
# print("end============"+str(m.end()))
#
# print("span==========="+str(m.span(0)))
"""在上面，当匹配成功时返回一个 Match 对象，其中：

group([group1, …]) 方法用于获得一个或多个分组匹配的字符串，当要获得整个匹配的子串时，可直接使用 group() 或 group(0)；
start([group]) 方法用于获取分组匹配的子串在整个字符串中的起始位置（子串第一个字符的索引），参数默认值为 0；
end([group]) 方法用于获取分组匹配的子串在整个字符串中的结束位置（子串最后一个字符的索引+1），参数默认值为 0；
span([group]) 方法返回 (start(group), end(group))。"""
# import re
# pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)   # re.I 表示忽略大小写
# m = pattern.match('Hello World Wide Web')
# print("==============="+str(m))                               # 匹配成功，返回一个 Match 对象
#
# print("group()================="+m.group())  # 返回匹配成功的整个子串
#
# print("span()=================="+str(m.span()))    # 返回匹配成功的整个子串的索引
# print("group(1)================="+m.group(1))      # 返回第一个分组匹配成功的子串
#
# print("span(1)==================="+str(m.span(1)))  # 返回第一个分组匹配成功的子串的索引
#
# print("group======================"+m.group(2))                          # 返回第二个分组匹配成功的子串
#
# print("span(2)===================="+str(m.span(2)))                          # 返回第二个分组匹配成功的子串
#
# print("groups()==================="+str(m.groups()))                            # 等价于 (m.group(1), m.group(2), ...)

# import re
#
# pattern = re.compile(r'\d+')  # 查找数字
# result1 = pattern.findall('runoob 123 google 456')
# result2 = pattern.findall('run88oob123google456', 0, 10)
#
# print(result1)
# print(result2)
# import re
#
# result = re.findall(r'(\w+)=(\d+)', 'set width=20 and height=10')
# print(result)
"""多个匹配模式，返回元组列表："""
"""和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。"""
# it = re.finditer(r"\d+","12a32bc43jf3")
# for match in it:
#     print(match.group())
#
# sp=re.split('\W+', 'runoobrunoob, runoob.')
# print(sp)
# st=re.split('(\W+)', 'runoobrunoobrunoob')
# print(st)
# print(re.split('\W+', ' runoob, runoob, runoob.', 1))

"""推导式"""
"""while实现"""
# list1 = []
# i = 0
# while i < 10:
#     list1.append(i)
#     i += 1
# print(list1)
# """for循环实现"""
# list2 = []
# for i in range(10):
#     list2.append(i)
# print(list2)
# """列表推导式"""
# list3 = [i for i in range(10)]
# print(list3)
#
# """带if的列表推导是，步长实现,偶数"""
# list4 = [i for i in range(0, 10, 2)]
# print(list4)
# """if实现"""
# list5 = [i for i in range(10) if i % 2 == 0]
# print(list5)
# """多个for实现列表推导式"""
# list6 = [(i, j) for i in range(1, 3) for j in range(3)]
# print(list6)
# """字典推导式"""
# dict1 = {i: i * 2 for i in range(1, 5)}
# print(dict1)
# """将两个列表合并为一个字典"""
# list6 = ['age', 'name', 'gender']
# list7 = ['tom', '20', 'man']
# dict2 = {list6[i]: list7[i] for i in range(len(list7))}
# print(dict2)
# """提取文中目标数据"""
# counts = {'MBP': 268, 'HP': 125, 'DELL': 210, 'LENOVO': 199, 'ACER': 99}
# # 提取上述电脑数量大于200的字典数据
# count1 = {key: value for key, value in counts.items() if value >= 200}
# print(count1)
# """集合推导式，set去重复"""
# lista = [1, 1, 2]
# set1 = {i * 2 for i in lista}
# print(set1)
# a = (1, 2, 2, 1)
# print("去重元组", set(a))  # 去重元组
# #
# a = [1, 2, 3, 2]
# print("去重列表", set(a))  # 去重列表
# #
# a = '123123'
# print("去重字符串", set(a))  # 去重字符串
# a = [1, 2, 3, 1, 2]
# dict1 = {}
# for i in a:
#     dict1[i] = ''
# print("通过字典的可以来进行去重", dict1.keys())
# a = [1, 2, 3, 4, 1, 2, 3, 4, 5, 6, 7]
# def fun1(a, b):
#     if not str(b) in a:
#         a.append(str(b))
#     return a
# c = reduce(fun1, [[], ] + a)
# print(c)
"""列表去重复 set改变了顺序"""
# old_list = [2, 1, 3, 3, 6, 5, 5]
# new_list = list(set(old_list))
# print("new_list={}".format(new_list))
"""用sort把顺序变回来"""
# new_list.sort(key=old_list.index)
# print("new_list={}".format(new_list))
"""利用dict来去重"""
# new_list = list({}.fromkeys(old_list))
# print("new_list = {}".format(new_list))
"""拆分"""
# b_dict = {}.fromkeys(old_list)
# print(type(b_dict))
# print(b_dict)
# """再把dict转化成list"""
# new_list = list(b_dict)
# print(new_list)
# list1 = ['chuan', 'zhi', 'bo', 'ke']
# t1 = ('aa', 'b', 'cc', 'ddd')
# # 结果：chuan_zhi_bo_ke
# print('_'.join(list1))
# # 结果：aa...b...cc...ddd
# print('...'.join(t1))
# mystr = "hello world and itcast and itheima and Python"
# # 结果：Hello world and itcast and itheima and python
# print(mystr.capitalize())
# mystr = "hello world and itcast and itheima and Python"
# # 结果：Hello World And Itcast And Itheima And Python
# print(mystr.title())
# def demo(test):
#     hello ="this is a {}".format(test)
#     print(hello)
#
# demo("apple")
#
# f = open("/pythontab/code.txt")
# while 1:
#
#     lines = f.readlines(10000)
#
#     if not lines:
#         break
#     for line in lines:
#
#         print(line)
#
# for line in open("/pythontab/code.txt"):
#
# #print line, #python2 用法
#
#     print(line)
#
#
# f = open("my_file.txt",'rb')
# byt = f.readlines()
# print(byt)

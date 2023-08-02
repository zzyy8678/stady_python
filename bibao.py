""" 闭包现象是指返回嵌套函数作为一个闭包,但可在函数之外访问函数局部变量的现象"""
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure = outer_function(10)
print(closure(5))  # 输出 15
print(closure(30))
'''
在上面的示例中，outer_function 是外部函数，它接收一个参数 x 并返回内部函数 inner_function 。
内部函数inner_function接收另一个参数y，并返回 x + y 的结果。

当调用 outer_function(10) 时，它返回了一个闭包，即内部函数inner_function 。
闭包在创建时会捕获外部函数的变量，这里是x的值为10。

然后，我们将返回的闭包赋值给变量closure 。接下来，当我们调用closure(5) 时，
它会将 5 作为参数传递给内部函数 inner_function ，并且由于闭包捕获了外部函数的x，所以 x 的值为 10 。
因此，closure(5) 的结果为15




闭包的优点：
是它可以保存状态。在上面的示例中，每次调用closure时，它都记住了外部函数outer_function的参数x的值。
这使得闭包可以用于实现记忆功能或保持特定状态的函数。'''

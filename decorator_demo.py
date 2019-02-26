#本文件与该项目无关，只作对装饰器用法的讲解的笔记使用。

from functools import wraps

'''
装饰器实际上是个函数
有两个特别之处：
1.参数是一个函数
2.返回值是一个函数
'''

'''
1.装饰器使用的是@符号，放在函数的上面
2.装饰器中定义的函数，要使用*args,**kwargs两对兄弟组合
3.需要使用functools.wraps在装饰器中的函数上把传进来的这个函数进行包裹，这样就不会丢失原来函数的__name__等属性。
'''

#一下为装饰器例子，需求是使所有的函数运行前先输出一个‘hello’

def my_log(func):

    @wraps(func)        #让传进来的函数保持原来的__name__等属性
    def wrapper(*args,**kwargs):   #这两个参数是为了兼容修饰的函数（有些函数带参数，有些不要），有参数可传入，没有也不影响。
        print('hello')
        return retfunc(*args,*kwargs)

    return wrapper      #返回的是修饰过的函数，注意不是wrapper()，加括号的话会返回运行后的值

@my_log
def run():
    print('run')

@my_log
def add(a,b):
    c = a + b
    print(c)
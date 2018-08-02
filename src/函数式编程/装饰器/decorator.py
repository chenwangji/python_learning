def now():
    print('2017-12-4')
f = now
f()
# __name__属性，指向函数名
print(now.__name__, f.__name__) # now now

# 定义一个装饰器
def log(fn):
    def wrapper(*args, **kw):
        print(('call {}():'.format(fn.__name__)))
        return fn(*args, **kw)
    return wrapper
@log
def myFn():
    print('12345')

myFn()  # call myFn(): 
        # '12345'

# 定义一个带参数的装饰器
def log2(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('{} {}()'.format(text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
@log2('execute')
def myFn2():
    print('23456')

myFn2() # execute myFn2()
        # '23456'

# functools.wraps
import functools 
def log3(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s()' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log3
def myFn3():
    print(34567)

myFn3()

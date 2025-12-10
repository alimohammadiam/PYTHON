# Iterate -> تکرار کردن
# Iteration -> تکرار : for, while
# Iterable -> قایل تکرار, تکرار پذیر
# Iterator ->

import functools
from time import perf_counter


def is_iterable(obj):
    return '__iter__' in dir(obj)


# Decorator / Wrapper
def dec(func):
    def inner(x, y):
        if y == 0:
            print('Zero Error....!')
        else:
            func(x, y)
    return inner


@dec
def f(x, y):
    print(x / y)


def star(a):
    def inner1(func):
        @functools.wraps(func)
        def inner2(*args, **kwargs):
            print('*' * a)
            func(*args, **kwargs)
            print('*' * a)
        return inner2
    return inner1


@star(10)
def msg(name):
    """prints a message"""
    print('I am ', name)


# Decorator base formol
def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator


# blocker
passwords = {'ali': '456879', 'reza01': '548931', 'alimohammadi': '789123', 'zeinab': '852147'}
blacklist = {'reza01'}


def blocker(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        if args[0] in blacklist:
            print('This user is blocked...!')
        else:
            func(*args, **kwargs)
    return inner


@blocker
def print_password(username):
    print(username, ":", passwords[username])


@blocker
def change_password(username, new_password):
    passwords[username] = new_password
    print(username, ':', passwords[username])


# Calculate time
def calculate_time(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        start_time = perf_counter()
        value = func(*args, **kwargs)
        end_time = perf_counter()
        run_time = end_time - start_time
        print(f'The run time of {func.__name__} is: {run_time}')
        return value
    return wrapper_decorator


@calculate_time
def a(y):
    s = 0
    for i in range(y):
        s += i


@calculate_time
def b(x):
    fact = 1
    for i in range(1, x+1):
        fact *= i


# ---

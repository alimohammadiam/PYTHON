from functools import wraps


def coroutine(func):
    @wraps(func)
    def start(*args, **kwargs):
        gn = func()
        next(gn)
        return gn
    return start


@coroutine
def my_gen():
    print("start!")
    for i in range(10):
        name = yield i
        print('your name is', name)


def cen_gen(words):
    print('start!')
    w = None
    while True:
        word = yield w
        if word not in words:
            w = word
        else:
            w = '*' * len(word)


def spl_gen(delimiter=" "):
    print('Start!')
    s = None
    while True:
        line = yield s
        s = line.split(delimiter)



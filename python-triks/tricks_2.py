from time import perf_counter, process_time
from functools import wraps
import timeit
from collections import Counter
from itertools import combinations

# from getpass import getpass
#   استفاده از getpass برای وارد کردن رمز : رمز نشان داده نمشود, در بعضی جاها درست کار نمیکند
# username = input('username: ')
# password = getpass()
#
# print(username)
# print(password)

# _________________________________run time


def time_calculation(func):
    @wraps(func)
    def wrapper_decorator(*args, **kwargs):
        start_time = perf_counter()
        # start_time = process_time()
        value = func(*args, **kwargs)
        end_time = perf_counter()
        # end_time = process_time()     # فقط زمانی که سی پی یو درگیر هست محاسبه میکند
        run_time = end_time - start_time
        print(f'Run Time of {func.__name__} is: {run_time}')
        return value
    return wrapper_decorator


@time_calculation
def test_sum(n=100000):
    sum_ = 0
    for i in range(n):
        sum_ += i


def test_sum_2(n=100000):
    sum_ = 0
    for i in range(n):
        sum_ += i


time_run = timeit.timeit(stmt='test_sum_2()', globals=globals(), number=1)


# ----------------------------numer of frequency in list
lst = ['a', 'b', 'a', 'c', 'c', 'a', 'd', 'e', 'f', 'a', 'f']

frequency = {}
for item in lst:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1


frequency_2 = Counter(lst)

# --------------------------------------Sets زیر مجموعه های یک مجموعه
s = {'a', 'b', 'c', 'd'}
subsets = []
for r in range(len(s) + 1):
    subsets.extend(list(combinations(s, r=r)))

# ---------------------------------------











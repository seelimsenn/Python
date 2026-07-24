# def my_decorator(func):
#     def wrapper(name):
#         print("Fonksiyondan önceki işlemler")
#         func(name)
#         print("Fonksiyondan sonraki işlemler")
#     return wrapper

# @my_decorator
# def say_hello(name):
#     print("hello", name)

# say_hello("ali")


import math
import time

def calculate_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        time.sleep(1)
        func(*args, **kwargs)
        finish = time.time()
        print(f" {func.__name__} fonksiyonun çalışma süresi: {finish - start} saniye")
    return inner

@calculate_time
def us_alma(a, b):
    print(math.pow(a, b))

@calculate_time
def faktoriyel(num):
    print(math.factorial(num))

@calculate_time
def toplama(a, b):
    print(a + b)

us_alma(2, 3)
faktoriyel(5)
toplama(5, 6)
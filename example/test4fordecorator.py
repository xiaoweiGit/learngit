import time

def deco_1(func):
    print("enter into deco_1")
    def wrapper(a,b):
        print("enter into deco_1_wrapper")
        func(a,b)
    return wrapper


def deco_2(func):
    print("enter into deco_2")
    def wrapper(a,b):
        print("enter into deco_2_wrapper")
        func(a,b)
    return wrapper

@deco_1
@deco_2
def addFunc(a,b):
    print("result is %d" %(a+b))

def a():
    print("1")
# addFunc(3,8)
# deco_1(deco_2(addFunc(3,8)))



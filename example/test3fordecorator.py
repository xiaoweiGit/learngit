import time
def deco(arg=True):
    if arg:
        def _deco(func):
        def wrapper():
        startTime=time.time()
        func()
        endTime=time.time()
        msecs=(endTime-startTime)*1000
        print("->elapsed time:%f ms" %msecs)
    return wrapper
    else
        def _desc
@deco
def myfunc():
    print("start myfunc")
    time.sleep(0.6)
    print("end myfunc")

print("myfunc is :",myfunc.__name__)
 # myfunc=deco(myfunc)
# print("myfunc is :",myfunc.__name__)
print(myfunc())

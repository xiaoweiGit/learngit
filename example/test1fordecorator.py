import time
def deco(args=True):
    if args:
        def _desc(func):
            def wrapper(*args,**kwargs):
                startTime=time.time()
                func(*args,**kwargs)
                endTime=time.time()
                msecs=(endTime-startTime)*1000
                print("->elapsed time:%f ms" %msecs)
            return wrapper
    else:
        def _desc(func):
            return func
    return _desc
@deco(False)
def myfunc():
    print("start myfunc")
    time.sleep(0.6)
    print("end myfunc")

@deco()
def addFunc(a,b):
    print("start myfunc")
    time.sleep(0.6)
    print("result is %d" %(a+b))
    print("end myfunc")

print("myfunc is :",myfunc.__name__)
# myfunc=deco(myfunc)
# print("myfunc is :",myfunc.__name__)
print(myfunc())
addFunc(1,2)

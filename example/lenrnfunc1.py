# 普通函数
def prwer(x):
    return x*x

# 默认函数
def power(x,n=2):
    return x+n;

# 传入list
def add_end(L=None):
    if L==None:
        L=[]
    L.append('End')
    print(L)
    return L

# 多参数
def calc(*number):
    sum=0
    for n in number:
        sum=sum+n
    print(sum)
    return sum

# 关键字参数
def person(name,age,**kw):
    print("name:",name,"age:",age,"other:",kw)


def person2(name,age,*args,**kw):

    print("name:",name,"age:",age,"args:", args,"other:",kw)

person('hanxiaowei',30,city='nanjing')


person2('1','2',3,4,5,6,7,8,9,x=11)
num=[1,2,3,45]

calc(*num)
calc(12,3,4,5,6,6,7,8,8)
# add_end([2,3,4])
add_end()
add_end();


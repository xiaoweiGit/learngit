
def fn(self,name='world'):
    print('hello,%s' % name)

Hello=type('hello',(object,),dict(hello=fn)) # 创建hello class

h=Hello()
h.hello()


# metaclass  类似C# 中外部方法 
class ListMetaclass(type):
    def __new__(cls,name,bases,attrs):
        attrs['add']=lambda self,value:self.append(value)
        return type.__new__(cls,name,bases,attrs)

class MyList(list,metaclass=ListMetaclass):
    pass

L=MyList()
L.add(1)
print(L)


#  ORM

class Field(object):
    def __init__(self,name,column_type):
        self.name=name
        self.column_type=column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__,self.name)

class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

class ModelMetaclass(type):
    def __new__(cls,name,bases,attrs):
        if name=='model':
            return type.__new__(cls,name,bases,attrs)
        print('Found model:%s' % name)
        mappings=dict()
        for k,v in attrs.items():
            if isinstance(v,Field):
                print('Found mapping:%s==>%s' % (k,v))
                mappings[k]=v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__']=mappings  # 保存属性和列的映射关系
        attrs['__table__']=name # 假设表名和列名一致
        return type.__new__(cls,name,bases,attrs)

class Model(dict,metaclass=ModelMetaclass):
      def __init__(self, **kw):
        super(Model, self).__init__(**kw)

      def __getattr__(self, key):
           try:
               return self[key]
           except KeyError:
               raise AttributeError(r"'Model' object has no attribute '%s'" % key)

      def __setattr__(self, key, value):
        self[key] = value

      def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

class User(Model):
    # 定义类的属性到列的映射：    
    id=IntegerField('id')
    name=StringField('username')
    email=StringField('email')
    password=StringField('password')
    
u=User(id=12345,name='Michael',email="test@qq.com",password='123')
# 保存到数据库
u.save();




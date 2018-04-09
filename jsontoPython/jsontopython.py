# _*_ coding:utf-8 _*_
import os
import json

_dictfiles=[]


def getalljsonfile():
    path=f"{os.path.abspath('.')}\model"
    if os.path.exists(path) is False:
        os.makedirs(path)
    for prefix,dirs, files, in os.walk(path):
        for name in files:
            if name.endswith(".json"):
                filename=path+'\\'+name
                _dictfiles.append(filename)
                print(filename)
    print(_dictfiles)

def _getjson():
    for f in _dictfiles:
        print(f)
        with open(f,'r',encoding="UTF-8") as json:
           return json.read()

def _getpyhonObject(jsonstr):
    myobject=json.loads(jsonstr) 
    print(myobject)
    import templete
    ob= templete.build("User",myobject)
    print(ob)

def templete(classname):
    """
    """
    strlist =[]
    import templete
    print(templete.head)
if __name__=="__main__":
   getalljsonfile() 
   strjson= _getjson()
   _getpyhonObject(strjson)
   # templete("User")
   

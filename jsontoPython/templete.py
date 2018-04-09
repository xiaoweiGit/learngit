def enter():
    return "\n"
def tab():
    return "    "
def head(name):
    head=["# _*_ coding:utf-8 _*_",enter(),"class ",name,":",enter()]
    print(head)
    return ''.join(head)
    # return head
def templete_construction():
    construction=[tab(),"def"," ","__init__","(","self",")",enter()]
    return ''.join(construction) 

def templete_key(key,t):
    if t is bool:
        templete_key(key,False)
    elif t is str:
        templete_key(key,"")
    elif t is int:
        templete_key(key,0)
    elif t is float:
        templete_key(key,0.0)
    key=["    ","self.",key,"=",'t']
    return ''.join(key)
def templete_dict(mydict=[]):
    body=[]
    for key in mydict:
      body.append(tab())
      body.append(tab())
      body.append(templete_key(key,type(mydict[key])))
      body.append(enter())
    return ''.join(body)
        
def build(classname,dicts):
    return head(classname)+templete_construction()+templete_dict(dicts)
           




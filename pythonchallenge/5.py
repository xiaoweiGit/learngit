import pickle
import urllib.request

def getData(address):
   f=urllib.request.urlopen(address) 
   data =f.read().decode("utf-8") 
   return data


def result(data):
    data=pickle.loads(data.encode())
    for d in data:
        res=''
        for s in d:
            res+=s[0]*s[1]
            print(f" {s}--{s[0]*s[1]},s0={s[0]},s1={s[1]}")
        # print(res)

if __name__=="__main__":
    f='http://www.pythonchallenge.com/pc/def/banner.p'
    d=getData(f)
    result(d)

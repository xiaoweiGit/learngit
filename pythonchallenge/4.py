import urllib.request
import re

q="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
num=16044;
def open(url):
    f=urllib.request.urlopen(url)
    data =f.read().decode("utf-8")
    print(data)
    return data

def getNum(data):
    p=re.compile(r'[\d]+')
    p= ''.join(re.findall('the next nothing is ([0-9]*)',data))
    return p
    results= re.findall(p,data)
    return int(results[-1])
    

if __name__=="__main__":
    for i in range(0,1000):
        # try:
            data= open(f"{q}{num}")
            num=getNum(data)
            print("--> %d" %i)

        # except IndexError:
            # num=num/2
            # print("next")
            # input()

        # except Exception:
            # print("发生异常了")
            # break

        




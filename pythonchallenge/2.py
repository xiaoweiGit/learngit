#  coding:utf-8
# http://www.pythonchallenge.com/pc/def/map.html
import string

strs="""
g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
"""
def result(text):
    o=""
    for c in strs:
        if ord(c)>=ord('a') and ord(c)<=ord('z'):
            if c=='y':
                o+='a'
            elif c=='z':
                o+='b'
            else:
                o+=chr((ord(c)+2))
            # o+=chr((ord(c)+2-ord('a')) % 26 + ord('a'))
        else:
            o+=c
    print(o)

def result2(text):
    o=''
    for c in text:
        if ord(c)>=ord('a') and ord(c)<=ord('z'):
             o+=chr((ord(c)+2-ord('a')) %26  + ord('a'))
        else:
            o+=c
    print(o) 
        
def result3(text):
    in_characters = "abcdefghijklmnopqrstuvwxyz"  
    out_characters = "cdefghijklmnopqrstuvwxyzab"  
    transtab = string.maketrans(in_characters, out_characters)  
    text.translate(transtab)

if __name__=="__main__":
    result2('map')

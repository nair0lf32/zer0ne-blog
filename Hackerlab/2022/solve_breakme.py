#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import string

def debig(data):
    data=list(data)
    a=data[:20]
    b=data[20:]
    res=''
    temp=''
    for i in range(20):
        temp+=a[i]+b[i]
    for i in temp:
        res+=chr(ord(i)^0xb)
    res=res[::-1]
    res=res[1:]+res[0]
    return res 

def debang(data,chift):
    data=data[1:].swapcase()+data[0]
    res=''
    M='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    m='abcdefghijklmnopqrstuvwxyz'
    verif=''
    for c in data:
        if c not in string.ascii_letters:
            res+=c
        else:
            if c in string.ascii_lowercase:
                start = ord('a')
                verif=m
            else:
                start = ord('A')
                verif=M
            for i in verif:
                if ord(c)-start==(ord(i)-start+chift)%26:
                    res+=i
                    break
    return res
            

print(debig(debang(debang(debig(debang(debang(debig("ZYYKXWAT[6RM@T6?ES>69=?Z6GRE}6WEGNK^>Oa6"),11),6)),13),18)))
    



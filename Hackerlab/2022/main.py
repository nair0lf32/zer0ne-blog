#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import string

def big(data):
    o = ''
    f = (data[-1] + data[:-1])[::-1]
    for i in f:
        o += chr(ord(i) ^ 0xb)
    return o[::2]+ o[1::2]

def bang(data,shift):
    enc = ''
    for c in data:
        if c not in string.ascii_letters:
            enc += c
        else:
            if c in string.ascii_lowercase:
                start = ord('a')
            else:
                start = ord('A')
            enc += chr(((ord(c) - start + shift) % 26) + start)

    return enc[-1] + enc[:-1].swapcase()

def check(s):
    
    if big(bang(bang(big(bang(bang(big(s),18),13)),6),11)) != "ZYYKXWAT[6RM@T6?ES>69=?Z6GRE}6WEGNK^>Oa6" :
        print("\nTry harder :)")
    else:
        print("\nYou got me !")
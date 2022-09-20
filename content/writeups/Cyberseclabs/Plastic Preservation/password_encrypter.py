#!/usr/bin/env python3

import base64
from datetime import datetime


def z(v):
    a = '\x2e\x6c\x6f\x67'
    with open(a, 'a') as a:
        a.write('# {} {} \n'.format(datetime.now(), v))


def y(a):
    b = 0xCBF29CE484222325
    c = '100000001B3'
    for i in a:
        z(str(b))                          # <- #REMOVE#
        b = b ^ ord(str(i)) * int(c, 16)
    b ^= 0xFFFFFFFFFFFFFFF
    d = str.encode(hex(b)[2:])
    return base64.b64encode(d).decode()


def x():
    e = input('[*]Enter your password: ')
    f = y(e)
    print('[*]Your encrypted password is: {}'.format(f))
    print('[*]And has been saved to encrypted.txt')
    with open('encrypted.txt', 'w') as g:
        g.write(f)


if __name__ == '__main__':
    x()

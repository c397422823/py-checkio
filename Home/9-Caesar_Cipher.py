#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-25 15:00:21
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import string

def to_encrypt(text, delta):
    #replace this for solution
    result = ""
    num = 0
    for word in text:
        if word == " ":
            result = result + " "
        else:
            if ord(word) + delta < 97:
                num = ord(word) + delta + 26
            elif ord(word) + delta > 122:
                num = ord(word) + delta - 26
            else:
                num = ord(word) + delta
            result = result + chr(num)
    # print(string.ascii_lowercase[-5:])
    return result

if __name__ == '__main__':
    print("Example:")
    print(to_encrypt('abc', 10))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-27 17:44:51
# @Author  : Chenweijie (397422823@qq.com)
# @Link    : emty
# @Version : $Id$

import os

def first_word(text):
    """
    reg_match = re.search('(?:[a-zA-Z\']+)', text)
    s = reg_match.group()
    return s
    """
    
    l = [",","."]
    for i in l:
    	text = text.replace(i," ")
    r = text.strip().split(" ")
    if len(r) != 1:
    		print(r)
    		return r[0]
    return text

if __name__ == '__main__':
    print("Example:")
    print(first_word("... and so on ..."))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")


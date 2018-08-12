#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-08 22:17:47
# @Author  : Chenweijie (397422823@qq.com)
# @Link    : emty
# @Version : $Id$

import os

def popular_words(text, words):
    # your code here
    '''
    dd = {}
    ll = text.lower().split()
    for ww in words:
        dd[ww] = ll.count(ww)
    return dd
    '''
    ll = text.lower().split()
    return {ww:ll.count(ww) for ww in words}


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-27 14:44:02
# @Author  : Chenweijie (397422823@qq.com)
# @Link    : emty
# @Version : $Id$

import os

# 1. on CheckiO your solution should be a function
# 2. the function should return the right answer, not print it.

def say_hi(name, age):
	s = "Hi. My name is %s and I'm %d years old" % (name,age)
	return s

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", "First"
    assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", "Second"
    print('Done. Time to Check.')

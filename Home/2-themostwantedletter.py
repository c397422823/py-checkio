#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-16 21:49:02
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os

def checkio(text):
	d = {}
	str=text.lower()
	for key in str:
		if key.isalpha():
			if key in d:
				d[key] += 1
			else:
				d[key] = 1
	#首先对key值排序，d.items将dict转化为list，d[0]即第一个元素，即key值，下同，reverse即由大到小
	d = sorted(d.items(), key=lambda d: d[0],reverse=True) 
	#再对value值排序
	d = sorted(d, key=lambda d: d[1])
	return d.pop()[0]
    #replace this for solution

if __name__ == '__main__':
    print("Example:")
    print(checkio("One"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-17 21:03:06
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os


def checkio(data):
	l = []
	for i in data:
		if data.count(i) > 1:
			l.append(i)
	print(l)
	return l

#Some hints
#You can use list.count(element) method for counting.
#Create new list with non-unique elements
#Loop over original list


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")
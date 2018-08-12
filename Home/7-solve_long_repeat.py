#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-21 21:57:18
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os

def long_repeat(line):
	d = {}
	result = []
	if line == "":
		return 0
	for i in range(len(line)):
		if line[i] in d :
			if line[i-1]  == line[i]:
				d[line[i]] += 1
			else:
				d[line[i]] = 1
		else:
			d[line[i]] = 1
	print(d)
	d = sorted(d.items(), key=lambda d: d[1])
	#print(d.pop()[1])
	return d.pop()[1]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')

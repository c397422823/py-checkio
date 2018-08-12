#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-23 21:01:34
# @Author  : Chenweijie (397422823@qq.com)
# @Link    : emty
# @Version : $Id$

import os

def safe_pawns(pawns):
	num = 0
	for chess in pawns:
		left = chr(ord(chess[0])-1) + chr(ord(chess[1])-1)
		right = chr(ord(chess[0])+1) + chr(ord(chess[1])-1)
		if left in pawns or right in pawns:
			num = num + 1
		print("left",left)
		print("right",right)
		print("result",num)
	return num

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
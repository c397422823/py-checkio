#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-29 22:05:32
# @Author  : Chenweijie (397422823@qq.com)
# @Link    : emty
# @Version : $Id$

import os


def second_index(text, symbol):
	# your code here
	i = text.find(symbol)
	j = text.rfind(symbol)
	if i == -1 or i == j:
		return None
	else:
		return j


if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", "s"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')

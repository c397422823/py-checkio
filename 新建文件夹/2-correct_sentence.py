#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-27 17:09:12
# @Author  : Chenweijie (397422823@qq.com)
# @Link    : emty
# @Version : $Id$

import os
import string

def correct_sentence(text):
	if text[0] in string.lowercase:
		text = text[0].upper() + text[1:]
	if text.endswith("."):
		return text
	else:
		return text + "."


if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    print("Coding complete? Click 'Check' to earn cool rewards!")
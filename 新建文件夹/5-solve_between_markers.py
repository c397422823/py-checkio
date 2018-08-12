#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-29 22:05:32
# @Author  : Chenweijie (397422823@qq.com)
# @Link    : emty
# @Version : $Id$

import os


def between_markers(text, begin, end):
    """
        returns substring between two given markers
    """
    # your code here
    l = text.find(begin)
    r = text.rfind(end)
    if r == l == -1:
    	return text
    elif r == -1:
    	return text[l+len(begin):]
    elif l == -1:
    	return text[:r]
    elif l > r:
    	return ''
    else:
    	return text[l+len(begin):r]



if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-25 17:07:58
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import datetime

def sun_angle(time):
    #replace this for solution
	date = datetime.datetime.strptime(time,'%H:%M')
	clock6 = datetime.datetime.strptime("6:00",'%H:%M')
	clock12 = datetime.datetime.strptime("12:00",'%H:%M')
	clock18 = datetime.datetime.strptime("18:00",'%H:%M')
	if date < clock6 or date > clock18:
		return "I don't see the sun!"
	else:
		if date <= clock12:
			s = (date - clock6).seconds
			result =  s / 3600 *15
		elif date > clock12:
			s = (date - clock6).seconds
			result =  s / 3600 *15 
		return result

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("17:00"))  #7:00

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"

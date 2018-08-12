#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-04 21:20:45
# @Author  : Chenweijie (397422823@qq.com)
# @Link    : emty
# @Version : $Id$

import os
def bigger_price(limit, data):
    """
        TOP most expensive goods
    """
    # your code here
    ll = []
    #result = sorted(data, lambda x, y: cmp(x['price'], y['price']), reverse=True)
    result = sorted(data,key = (lambda x: x['price']), reverse=True)
    for i in range(limit):
        ll.append(result[i])
    print(ll)
    return ll


if __name__ == '__main__':
    from pprint import pprint
    print('Example:')
    pprint(bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]))

    # These "asserts" using for self-checking and not for auto-testing
    assert bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]) == [
        {"name": "wine", "price": 138},
        {"name": "bread", "price": 100}
    ], "First"

    assert bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]) == [{"name": "whiteboard", "price": 170}], "Second"

    print('Done! Looks like it is fine. Go and check it')
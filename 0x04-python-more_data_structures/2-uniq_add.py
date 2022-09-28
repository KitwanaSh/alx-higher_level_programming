#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return None
    # return [set(x+y) for x in my_list for y in my_list]
    return [x if x != x else sum(set(x)) for x in my_list]

#!/usr/bin/python3
def uniq_add(my_list=[]):
    # return [set(x+y) for x in my_list for y in my_list]
    add_them = 0
    for i in set(my_list):
        add_them = add_them + i
    return add_them

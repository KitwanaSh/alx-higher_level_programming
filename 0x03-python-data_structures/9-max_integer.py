#!/usr/bin/python3
def max_integer(my_list=[]):
    max_number = my_list[0]
    for num in my_list[1:]:
        if my_list == []:
            return None
        if num > max_number:
            max_number = num
        return max_number


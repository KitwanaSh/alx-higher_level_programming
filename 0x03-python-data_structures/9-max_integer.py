#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    max_number = my_list[0]
    for num in range(len(my_list)):
        if my_list[num] > max_number:
            max_number = my_list[num]
    return max_number

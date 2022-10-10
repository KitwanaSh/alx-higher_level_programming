#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    iterate_go = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
        except IndexError:
            break
        else:
            iterate_go += 1
    print()
    return (iterate_go)

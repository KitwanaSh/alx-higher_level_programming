#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arg_cnt = len(sys.argv) - 1
    if arg_cnt == 0:
        print("0 argument.")
    elif arg_cnt == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(arg_cnt))
    for index in range(arg_cnt):
        print("{}: {}".format(index + 1, sys.argv[index + 1]))

#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    num_args = 0
    for index in range(len(sys.argv) - 1):
        num_args = num_args + int(sys.argv[index + 1])
    print("{}".format(num_args))

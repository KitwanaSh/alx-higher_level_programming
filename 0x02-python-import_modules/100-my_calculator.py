#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    from calculator_1 import add, sub, mul, div

    num_args = len(sys.argv) - 1

    if num_args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
        sys.exit(1)

    opera = sys.argv[2]
    if opera != '+' and opera != '-' and opera != '*' and opera != '/':
        print("Unknown operator. Available operators: +, -, * and /\n")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if opera == '+':
        print("{} {} {} = {}".format(a, opera, b, add(a, b)))
    elif opera == '-':
        print("{} {} {} = {}".format(a, opera, b, sub(a, b)))
    elif opera == '*':
        print("{} {} {} = {}".format(a, opera, b, mul(a, b)))
    else:
        print("{} {} {} = {}".format(a, opera, b, div(a, b)))

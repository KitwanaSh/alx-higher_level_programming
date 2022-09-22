#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    from calculator_1 import add, sub, mul, div

    num_args = len(sys.argv) - 1
    operator = sys.argv[2]

    if num_args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
        sys.exit(1)

    if operator != '+' and operator != '-' and operator != '*' and operator != '/':
        print("Unknown operator. Available operators: +, -, * and /\n")
        sys.exit(1)
    
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if operator == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif operator == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif operator == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    else:
        print("{} / {} = {}".format(a, b, div(a, b)))

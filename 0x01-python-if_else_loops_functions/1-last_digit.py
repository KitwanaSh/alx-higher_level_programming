#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_dig = int(repr(number)[-1])
if last_dig > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, last_dig))
elif last_dig == 0:
    print("Last digit of {} is {} and is 0".format(number, last_dig))
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, last_dig))

#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_numbers = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if (roman_string is None) or type(roman_string) is not str:
        return 0

    for key, value in roman_numbers.items():


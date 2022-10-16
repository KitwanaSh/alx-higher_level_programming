#!/usr/bin/python3
def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.
    
    Arguments:
        text (string): The text to print.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    m = 0
    while m < len(text) and text[m] == ' ':
        m += 1

    while m < len(text):
        print(text[m], end="")
        if text[m] == "\n" or text[m] in ".?:":
            if text[m] in ".?:":
                print("\n")
            m += 1
            while m < len(text) and text[m] == ' ':
                m += 1
            continue
        m += 1

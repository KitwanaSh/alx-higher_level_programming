#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        final = fct(*args)
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(e))
        final = None
    return (final)

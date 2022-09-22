#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)
    for nm in names:
        if nm[:2] != "__":
            print("{}".format(nm))

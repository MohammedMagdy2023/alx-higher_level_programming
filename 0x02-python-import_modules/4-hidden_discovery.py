#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    NameList = dir(hidden_4)
    for i in NameList:
        if "__" not in i:
            print("{}".format(i))

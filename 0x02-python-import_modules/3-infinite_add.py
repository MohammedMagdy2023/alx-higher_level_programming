#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_c = len(sys.argv[1:])
    res = 0
    for i in sys.argv[1:]:
                res += int(i)
    print(res)

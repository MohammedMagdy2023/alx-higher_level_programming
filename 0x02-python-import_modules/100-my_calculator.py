#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_c = len(sys.argv[1:])
    arg_v = sys.argv[1:]
    if arg_c != 3:
        exit(1)
    else:
        a = sys.argv[1]
        operator = sys.argv[2]
        b = sys.argv[3]
        match operator:
            case '+':
                print("{} + {} = {}".format(a, b, (int(a) + int(b))))
            case '-':
                print("{} - {} = {}".format(a, b, (int(a) - int(b))))
            case '*':
                print("{} * {} = {}".format(a, b, (int(a) * int(b))))
            case '/':
                print("{} / {} = {}".format(a, b, (int(a) / int(b))))
            case _:
                print("Unknown operator. Available operators: +, -, * and /")
                exit(1)

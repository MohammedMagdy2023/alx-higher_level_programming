#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    # Exit If There Is An Error While Calling Func
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    # Check For Operator
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])
    if operator == '+':
        res = add(a, b)
    elif operator == '-':
        res = sub(a, b)
    elif operator == '*':
        res = mul(a, b)
    elif operator == '/':
        res = div(a, b)
    else:
        # if Invlid Operator
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print("{} {} {} = {}".format(a, operator, b, res))

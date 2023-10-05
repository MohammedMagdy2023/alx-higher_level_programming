#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    # This gives the n arguments including the script name
    argc = len(sys.argv)
    # This creats a list of n arguments without the script name
    argv = sys.argv[1:]
    if argc > 1:
        if argc == 1:  # This prints the argument if there is one
            j = 1
            print("{} argument".format(len(argv)))
            print("{} : {}".format(j, argv))
        else:  # This prints the n number of arguments
            j = 1
            print("{} arguments".format(len(argv)))
            for i in argv:
                print("{} : {}".format(j, i))
                j += 1
    else:  # This prints the argument if there is no arguments
        print("0 arguments.")

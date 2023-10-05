#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) #This gives the n arguments including the script name
    argv = sys.argv[1:]
    if argc > 1:
        if argc == 1 :
                j = 1
                print("{} argument".format(len(argv)))
                print("{} : {}".format(j, argv))
        else:
            j = 1
            print("{} arguments".format(len(argv)))
            for i in argv:
                print("{} : {}".format(j, i))
                j += 1
    else:
        print(" {} arguments.".format(0))

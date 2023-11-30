#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argNum = len(sys.argv) - 1
    if argNum == 0:
        print("0 arguments.")
    elif argNum == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(argNum))
        for r in range(argNum):
            print("{}: {}".format(r + 1, sys.argv[r + 1]))

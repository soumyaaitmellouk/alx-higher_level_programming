#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argNum = len(sys.argv) - 1
    somme = 0
    if argNum == 0:
        print("0")
    else:
        for r in range(argNum):
            somme = somme + int(sys.argv[r+1])
print("{}".format(somme))

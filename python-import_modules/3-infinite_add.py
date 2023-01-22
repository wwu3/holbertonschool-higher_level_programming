#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv)
    d = 0
    for i in range(1, n):
        d = d + int(sys.argv[i])
    print("{}".format(d))

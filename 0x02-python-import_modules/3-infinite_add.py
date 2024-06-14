#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    argc = len(argv)
    result = 0
    for i in range(argc):
        result += int(argv[i])
        if result is None:
            print("0")
    print(result)

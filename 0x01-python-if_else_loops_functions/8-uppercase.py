#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':
            char = chr(ord(char) - ord('a') + ord('A'))
        print("{}".format(char), end="")
    print("{}".format(""))

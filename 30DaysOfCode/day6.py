#!/bin/python3

def evenStr(s):
    l = len(s)
    result = ""

    for i in range(0, l, 2):
        result += s[i]
    return result

def oddStr(s):
    l = len(s)
    result = ""

    for i in range (1, l, 2):
        result += s[i]
    return result


T = int(input())

for i in range(0, T):
    s = input()
    print(evenStr(s) + " " + oddStr(s))
    

#!/bin/python3

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    res = ""
    
    if n == len(arr):
        for i in range(len(arr)-1, -1, -1):
            res += str(arr[i]) + " "


    print(res)

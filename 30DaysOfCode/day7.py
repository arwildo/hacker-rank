#!/bin/python3

#def rev(arr):
#    for i in arr:
#        return arr[len-1]
#
#
#if __name__ == '__main__':
#    #n = int(input())
#    #print(n)
#    arr = list(map(int, input().rstrip().split()))
#    revArr = rev(arr)
#    print(arr)

def revArr(test):
    result = []
    count = len(test)
    for i in test:
        result.append(test[count-1])
        count -= 1
    print(result)


test = list(map(int, input().rstrip().split()))
print(test)
revArr(test)
    

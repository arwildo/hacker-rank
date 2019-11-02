#!/bin/python3

i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


if __name__ == '__main__':
    n = int(input())


for l in i:
    print(str(n) +' x '+ str(i[l -1]) + ' = ' + str(n*i[l-1]))

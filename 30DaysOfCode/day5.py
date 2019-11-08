#!/bin/python3

i = list(range(1, 11))


if __name__ == '__main__':
    n = int(input())


for l in i:
    print(str(n) +' x '+ str(i[l -1]) + ' = ' + str(n*i[l-1]))

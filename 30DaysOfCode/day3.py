#!/bin/python3


def checks(N):
    odd = 1

    if N%2 != odd and N > 20:
        print('Not Weird')
    elif N%2 != odd and N >= 2 and N <= 5:
        print('Not Weird')
    elif N%2 != odd and N >= 6 and N <= 20:
        print('Weird')
    elif N%2 == odd:
        print('Not Weird')

if __name__ == '__main__':
    N = int(input())
    checks(N)

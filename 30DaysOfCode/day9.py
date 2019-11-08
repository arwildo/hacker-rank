#!/bin/python3
import os


def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result



if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'environ_var.txt'
    fptf = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    results = factorial(n)
    print(results)

    fptf.write(str(results) + '\n')

    fptf.close()

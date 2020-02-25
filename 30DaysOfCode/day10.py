
def maxCon(n):
    max = 0
    res = 0

    while n > 0:
        if n % 2 == 1:
            res += 1
            if res > max:
                max = res
        else:
            res = 0
        n //= 2
    return max



if __name__ == '__main__':
    n = int(input())
    print(maxCon(n))

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

#print(a)

numberOfSwaps = 0

for i in range(n):
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            temp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = temp
            numberOfSwaps += 1
        if numberOfSwaps == 0:
            break
#print(a)
print("Array is sorted in {} swaps".format(numberOfSwaps))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[len(a) - 1]))




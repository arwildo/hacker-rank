#!/bin/python3


word = '12345'
n = 2
t = [word[j:j+n] for j in range(0, len(word), n)]
c = 0
print(t)
for i in t:
    print(word[c])
    c += 1

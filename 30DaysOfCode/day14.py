class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        self.maximumDifference = max(a) - min(a)


#_ = 3
#a = list(map(int, "1 2 5".split(' ')))
#
#d = Difference(a)
#d.computeDifference()
#
#print(d.maximumDifference)

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)

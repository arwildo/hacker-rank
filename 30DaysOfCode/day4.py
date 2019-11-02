#!/bin/python3

class Person(object):
    def __init__(self, initialAge):
        self.age = 0 
        self.initialAge = initialAge

        if self.initialAge < 0:
            print("Age is not valid, setting age to 0")
        elif self.initialAge > 0:
            self.age = initialAge

    def yearPasses(self):
        self.age += 1
        print(self.age)

    def amIOld(self):
        if self.age < 13:
            print("You are young.")
        elif self.age >= 13 and self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")


Person(int(input())).yearPasses()

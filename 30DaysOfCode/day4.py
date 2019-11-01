#!/bin/python3

class Person(int):
    
#    def __init__(self):
#        self.age = ()
#
#    if self.age < 0:
#        print("Age is not valid, setting age to 0")
#    elif self.age > 0:
#        initialAge = self.age

    def yearPasses(initialAge):
        initialAge += 1

    def amIOld(initialAge):
        if initialAge < 13:
            print("You are young.")
        elif initialAge >= 13 and initialAge < 18:
            print("You are a teenager.")
        else:
            print("You are old.")

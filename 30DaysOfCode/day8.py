#!/bin/python3
import sys

savedList = []

for line in sys.stdin:
    if len(line) == 1:
        break
    else:
        savedList.append(line)


n = int(savedList[0])
contactInfo = savedList[1:n+1]
getContact = savedList[n+1:]

phoneBook = {}

for contact in contactInfo:
    name, id = contact.split()
    phoneBook[name] = id #assign id into contact name

for get in getContact:
    getQuery = get.rstrip()
    if getQuery in phoneBook:
        print(getQuery + "=" + str(phoneBook[getQuery]))
    else:
        print("Not found")

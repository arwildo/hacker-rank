class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    def calculate(self):
        res = None
        sum = 0
        for i in self.scores:
            sum += i
        res = sum / numScores

        if res < 40:
            res = 'T'
        elif res < 55:
            res = 'D'
        elif res < 70:
            res = 'P'
        elif res < 80:
            res = 'A'
        elif res < 90:
            res = 'E'
        else:
            res = 'O'

        return res


#inputText = "Heraldo Memelli 8135627 2"
#inputScores = "100 80"
#line = inputText.split()
#firstName = line[0]
#lastName = line[1]
#idNum = line[2]
#numScores = line[3]
#scores = list(map(int, inputScores.split()))
#p = Person(firstName, lastName, idNum, numScores)
#p.printPerson()
#print("Grade: {}".format(Student.calculate()))

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())

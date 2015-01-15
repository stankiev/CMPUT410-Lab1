# Lab1
# Dylan Stankievech
# January 14, 2015

class Student:
	courseMarks={}
	name= ""
	family = ""
	def __init__(self, name, family):
		self.name = name
		self.family = family

	def addCourseMark(self, course, mark):
		self.courseMarks[course] = mark

	def average(self):
		marks = self.courseMarks.values()
		return sum(marks) / len(marks)



test = Student("Dylan", "Stank")
test.addCourseMark("comp410", 10)
test.addCourseMark("comp401", 10)
test.addCourseMark("comp174", 100)
print(test.average())

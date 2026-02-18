#name : peter mbugua
# date : 18/02/2026
# program to show lists in python

friends = ["Rachel","pheobe","ross","chandler"]
print(friends)
friends.sort()
print(friends)
friends.reverse()
print(friends)
friends.append("jack")
print(friends)
new_friends=["charles","james"]
print(len(new_friends))

students = friends + new_friends
print(students)
students.pop()
print(students)
students.insert(5,"jenny")
print(students)
students.insert(6,"valary")
print(students)
students.extend("dawn")
print(students)
students.remove("chandler")
print(students)
new_students = students.copy()
print(students)
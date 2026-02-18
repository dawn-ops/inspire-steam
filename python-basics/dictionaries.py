#name : peter mbugua
# date : 18/02/2026
# program to show the use of dictionaries in python

cars = {"model" : "audi","make" : "q8" ,"color":"cherry"}
print(cars)
print(cars["model"])
print(cars["color"])

students = {"alice" : 24, "james" : 18}
for key in students:
    print(key)
for val in students.values():
    print(val)
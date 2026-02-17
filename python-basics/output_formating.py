#name : peter mbugua
# date : 16/02/2026
# program to format the output in different types

name = "dawn julio"
weight = 90 #weight in kg
fav_team = "liverpool"
height = 120.86 #height in cms
# 1. format using f printf(f"{}")
print(f"my name is {name} and i weigh {weight} kgs")

# 2. using f string
msg = f"my name is {name} and i support {fav_team}"
print(msg)

# 3. using {} and .format()
print("my name is {0} an i am {1} cms tall".format(name,height))

# using outpit specifies %s
import math
print("the value of pi is approximately %5.3f."math.pi)

#%f is for float fractions
print("i support %S" %fav_team)
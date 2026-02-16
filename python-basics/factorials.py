#name : peter mbugua
# date : 16/02/2026
# program to calc factorials of numbers



number = int(input("enter the number x :"))
factorial = 1 #initiate factorial as 1
for x in range(1,number+1):
    factorial *= x

print(f"{number}!={factorial}")
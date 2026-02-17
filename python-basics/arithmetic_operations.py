#name : peter mbugua
# date : 17/02/2026
# program to perform arithmetic operations

f_number = 12 #1st number
s_number = 34 #2nd number
sum_number = f_number + s_number
diff_number = f_number - s_number
prod_number = f_number * s_number

print("the sum of the numbers %d"%sum_number)
print("the diff of the numbers %0.2f"%diff_number)
print("the prod of the numbers %d"%prod_number)

#modulus-remainder
print(7%5)

#even and odd numbers
for x in range (0,21):
    if (x%2==1):
        print(f"{x}is an odd numer")
    elif(x%2==0):
         print(f"{x} is an even number")
    

# name : peter mbugua
# date : 13/02/2026
# program to calculate arithmetic progression

# calculating thee nth term

a = int(input("enter the first number :"))
n = int(input("enter the number of terms :"))
d = int(input("enter the common difference :"))

nth_term = a + (n - 1) * d
sn =( n * (2 * a + (n - 1) * d) / 2)
print(f"the nth term is : {nth_term}")
print(f"the sum of numbers is{sn}")
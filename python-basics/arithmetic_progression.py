# name : peter mbugua
# date : 13/02/2026
# program to calculate arithmetic progression

# calculating the nth term


a = int(input("enter the first number :"))
n = int(input("enter the number of terms :"))
d = int(input("enter the common difference :"))

nth_term = a + (n - 1) * d
sn =( n * (2 * a + (n - 1) * d) / 2)
print(f"the nth term is : {nth_term}")
print(f"the sum of numbers is{sn}")

#calculating the sum of geometric progression
def geometric_sum(a,r,n):
    if r<1:

        #formula:sn=a(1-r^n)/(1-r)
        sn=a*(1-r**n)/(1-r)

    elif r>1:

        #formula:sn=a(r^n-1)/(r-1)
        sn=a*(r**n-1)/(r-1)

    else:

        #r==1
     #formula:sn=a*n
        sn=a*n

     return sn

answer=geometric_sum(a,r,n)
print("the sum of te geometric progression is",answer)
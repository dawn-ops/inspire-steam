#name : peter mbugua
# date : 16/02/2026
# program to calc income tax

salary = int(input ("enter your gross salary"))

if salary < 50000:
    tax = (2.5 * salary)/100
    net_salary = salary - tax
print(f"gross salary = {salary}")
print(f"net salary = {net_salary}")
print(f"tax = {tax}")
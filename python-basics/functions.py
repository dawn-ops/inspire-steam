def cook_egg():
    oil = "20ml"
    pan =   "true"
    moto = "true"
    egg = 2

    print(f"the pan is {pan},and the fire is {moto},add {oil} amount of oil amount of oil and cook {egg} eggs")
print("here is statement 1")
print("here is statement 2")

cook_egg()
print("here is statement 3")

# ride fare creating function

def create_fare(route,distance,rush_hour):
    fare = distance * 10
    if rush_hour == True:

        fare = fare *1.5
    
    print(f"your fare on route {route} is {fare}")
    rush_hour = True
returned_fare = create_fare("juja-allsops", 7 , "rush_hour")
print(f"the fare returned is :n{returned_fare}")
 # passing a list as a paremeter
def write_all_interests(interests):

    for interest in interests:

        print(f"i am interested in {interest}")

all_interests = ["bike riding","playing"]
write_all_interests(all_interests)
#name : peter mbugua
# date : 19/02/2026
# program to objects in python

class Human:
 #first we determine the attributes of a human being
 type = "mammal"
 legs = 2
 brain = "true"
 warm_blooded = "true"
  #we then create the constructor for class/object
  #the constructor will be used to create copies of this object

def _init_(self,name,age):
    self.human_name = name
    self.human_age = age
def tell_story(self):
    print(f"hello,i am {self.human_name} here is my story")
    print(f"there was once a bot that said hello world")
#create the human
amani = human("amani,17")
triza = human("triza,16")
#let the humans created do things
amani.tell_story()
print("amanis age")

# name : peter mbugua
# date : 23/02/2026
# program to show inheritance in python
    class Animal():

                def __init__(self,species,weight,food):

                    self.species = species
                    self.weight = weight
                    self.food = food
        def grow(self,weight):

            weight = 1.1 * weight
            print(f"the animal weighs{weight}")
        def eat(self,food):
            print(f"the animal eats {food}")

    class dog(animal):

            def __init__(self,color,weight,breed)
            self().__init__ (species,weight,food)
            self.color = color
            self.weight = weight
            self.breed = breed
    def grow(self,weight):
        weight = 1.1 * weight
        print(f"the animal weighs{weight}")
    def barks(self,):
        print(f"the dog says woof woof")


    class horse(animal):

            def __init__(self,color,weight,breed)
            self.color = color
            self.weight = weight
            self.breed = breed
    def grow(self,weight):
        weight = 1.1 * weight
        print(f"the animal weighs{weight}")
    def neighs(self,):
        print(f"the horse says neigh neigh")



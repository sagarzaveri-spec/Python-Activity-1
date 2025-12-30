'''
class FIFA:
    def __init__(self,country): #init is the method for the class, when you add the object it will call itself automatoically.
        self.country=country #this is an instance variable
    def show_information(self):
        print("FIFA Country Name: ",self.country)
object1=FIFA("Argentina")
object1.show_information()

class fruit:
    taste="Sweet"
    def __init__(self,name,colour):
        self.name=name
        self.colour=colour
apple=fruit("Apple","Red")
banana=fruit("Banana","Yellow")

print(apple.taste)
print(apple.name,apple.colour)
print(banana.name,banana.colour)
'''

class Parrot:
    species="Bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sings(self,song):
        return "{} sings {}".format(self.name,song)
    def dances(self,dances):
        return "{} is now dancing {}".format(self.name,dances)

cockatiel=Parrot("Cockatiel",8)
grey_parrot=Parrot("Grey Parrot",11)

print("This is a",cockatiel.species)
print("This is a",grey_parrot.species)

print("This is a",cockatiel.name,cockatiel.age)
print("This is a",grey_parrot.name,cockatiel.age)

print(cockatiel.sings("'Smooth Operator'"))
print(cockatiel.dances("Contemporary"))
'''
class square():
    def __init__(self,side):
        self.side=side
    def area(self):
        print("My area is: ",self.side**2)
class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print("My area is: ",3.14*self.radius*self.radius)
osquare=square(5)
ocircle=circle(5)
for shape in (osquare,ocircle):
    shape.area()
'''

'''
class SocialMedia():
    def post(self,content):
        self.content=content
        pass
class Facebook(SocialMedia):
    def post(self,content):
        self.content=content
        print(f"Posting on Facebook {self.content}")
class Instagram(SocialMedia):
    def post(self,content):
        self.content=content
        print(f"Posting on Instagram {self.content}")
class Twitter(SocialMedia):
    def post(self,content):
        self.content=content
        print(f"Posting on Twitter {self.content}")
platforms=[Facebook(),Instagram(),Twitter()]
for stories in platforms:
    stories.post("My first post")

#Encapsulation
class Computer:
    def __init__(self):
        self.__maxprice=900
    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))
    def setMaxPrice(self,price):
        self.__maxprice=price
c=Computer()
c.sell()

c.setMaxPrice(1000)
c.sell()
'''

class user:
    def __init__(self,username,password):
        self.username=username
        self.__password=password
        self.__is_logged_in=False
    def login(self,entered_password):
        if entered_password==self.__password:
            self.__is_logged_in=True
            print(f"{self.username} is logged in successfully")
        else:
            print("Invalid Password")
    def logout(self):
        if self.__is_logged_in:
            self.__is_logged_in=False
            print(f"{self.username} is logged out successfully")
    def change_password(self,old,new):
        if self.__is_logged_in:
            if old==self.__password:
                self.__password=new
                print("Password Updated Succssfully")
            else:
                print("New password cannot be the old password")
        else:
            print("Please login first")
    def get_login_status(self):
        return self.__is_logged_in

user1=user("Sagar","1234")
user1.change_password("1234","Apple")
user1.login("1234")
print(user1.get_login_status())
user1.change_password("1234","Apple")
user1.login("1234")
user1.logout()
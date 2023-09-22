# #import requests
import random

import pygame
# #url = "http://www.cs.utah.edu/~dejohnso/simple.html"
# #source = requests.get(url) #get the
# #source_text = source.text
# #print(source_text)
# #index = source_text.find("simple")
# #soup = BeautifulSoup(source_text, "html perser")
# #my_paragraph = soup.find("p")
#
# #vote_count = {}
# #for vote in votes:
#  #   print(vote)
#   #  count = vote_count.get(vote,0)
#    # vote_count[vote] = count + 1
# #values = [1, -2, -3, 4]
# #positive_values = [x for x in values if x > 0]
# #print(positive_values)
# #nonzeros = [x for x in values if x !=0]
# #print(nonzeros)
# #values = [1, 2, 3, 0, 0, 5, 0, 6]
# #for index in range(len(values)):
#  #   if values[index] == 0
#   #      values.pop(index)
# #print(values)
# #for value in values:
#  #  if value == 0:
#   #      values.remove(value)
# #print(values)
# #new_vals = [value for value in values if value != 0]
# #print(new_vals)
# #def modify(item):
#  #   item = item + 1
#   #  item = item * item
#    # return item
# #vals = [0, 1, 2, 3]
# #final = [modify(item) for item in vals if item !=2]
# #print(final)
# import pygame, sys, math
# # class Sprite:
# #     def __int__(self, image, position):
# #         self.image = image
# #         self.rect = image.get_rect()
# #         self.rect.center = position
# #         self.mask = pygame.mask.
# #
# # pygame.init()
# # size = width, height = 1920, 1080
# # screen = pygame.display.set_mode((width, height))
# # ball = pygame.image.load("ex-aid.png").convert_alpha()#load image and precalculate transparency
# # ball_rect = ball.get_rect()
# # print(ball_rect)
# # ball_rect = ball_rect.move(10, 20) #move by 10 in x, 20 in y
# # print(ball_rect)
# # genm = pygame.image.load("genm.png").convert_alpha()
# # genm_rect = genm.get_rect()
# # print(genm_rect)
# # genm_rect = genm_rect.move(20, 40)
# # is_playing = True
# # while is_playing:
# #     #StartPlay
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             is_playing = False
# #         if event.type == pygame.MOUSEBUTTONDOWN:
# #             pos = pygame.mouse.get_pos()
# #             print(pos)
# #             ball_rect.center = pos #move the image to the mouse position
# #     screen.fill((200, 0, 200))
# #     screen.blit(ball, ball_rect) #draw image at screen
# #     screen.blit(genm, genm_rect)
# #     pygame.draw.rect(screen, (255, 100, 100), ball_rect, 10) #red box around ex-aid
# #     pygame.draw.rect(screen, (100, 255, 100), genm_rect, 10)
# #
# #     collision_rect = ball_rect.inflate(-20, -20)
# #     if collision_rect.collidedict(genm_rect):
# #         pygame.draw.rect(screen, (255, 100, 100), ball_rect, 3)
# #         pygame.draw.rect(screen, (255, 100, 100), collision_rect, 3)
# #     else:
# #         pygame.draw.rect(screen, (255, 255, 100), ball_rect, 3)
# #         pygame.draw.rect(screen, (255, 255, 100), collision_rect, 3)
# #     pygame.display.update() #display what I draw
# #     pygame.time.wait(20) #50fps
# # pygame.quit()
# # sys.exit()
# def main():
#     pygame.init()
#     screen = pygame.display.set_mode((1280, 720))
#     image = pygame.image.load("ex-aid.png").convert_alpha()
#     is_playing = True
#     while is_playing:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 is_playing = False
#         screen.fill((0, 100, 50))
#         #getting mouse position
#         mouse_x, mouse_y = pygame.mouse.get_pos()
#         image_x, image_y = rect.center
#         image_x, image_y = (mouse_x,mouse_y)
#         image_x += mouse_x - image_x
#         image_y += mouse_y - image_y
#         rect.center = image_x, image_y
#         screen.blit(image, rect)
#         pygame.display.update()
#         pygame.time.wait(1000//60)

# class Vehicle():
#     def __init__(self, vehicle_type):
#         self.type = vehicle_type
#         if self.type == "car":
#             self.seats = 5
#         if self.type == "truck":
#             self.seats = 2
#         if self.type == "bus":
#             self.seats = 30
#         if self.type == "bike":
#             self.seats = 1
#
#     def __init__(self, color):
#         self.color = color
#
#     def __str__(self):
#         return "I am a " + self.color + " vechicle!"
#
# class Car(Vehicle):
#     def __init__(self, color, top_speed):
#         super().__init__(color)
#         self.top_speed = top_speed
#     def set_speed(self, current_speed):
#         if current_speed < self.top_speed:
#             self.speed = current_speed
#         else:
#             self.speed = self.top_speed
#
# class Truck(Vehicle):
#
#     def __init__(self, color, capacity):
#         super().__init__(color)
#         self.max_load = capacity
#         self.current_load = 0
#
#     def load(self, cargo_weight):
#         if ((self.max_load - self.current_load) >= cargo_weight):
#             self.current_load += cargo_weight
#             print("The current load is " + self.current_load)
#         else:
#             print("Load too big")
#
# lightning = Vehicle("red")
# mater = Vehicle("brown")
# print(lightning)
# print(mater)
# lightning = Car("red", 200)
# print(lightning)
# lightning.set_speed(200)
# mater = Truck("brown", 1000)
# print(mater)
# class Vehicle():
    #This is what our code might look like if we didn't want to create multiple
#classes
    # def __init__(self, vehicle_type): # type is "car", "bus", ...
    #     self.type = vehicle_type
        # if self.type == "car":
        #     self.seats = 5
        # if self.type == "truck":
        #     self.seats = 2
        # if self.type == "bus":
        #     self.seats = 30
        # if self.type == "bike":
        #     self.seats = 1
        # #what about if the type is unknown? error-handling?
#     def __init__(self, color):
#         self.color = color
#     def __str__(self):
#         return "I am a " + self.color + " vehicle!"
 #class Car(Vehicle):
#     def __init__(self, color, top_speed):
#         super().__init__(color) #initializes the Vehicle "part" of our car; note we
# #don't pass self parameter
#         self.top_speed = top_speed #an additional instance variable in cars
#     #a new method that Vehicles don't have
#     def set_speed(self, current_speed):
#         if current_speed < self.top_speed: #obey the max speed
#             self.speed = current_speed
#         else:
#             self.speed = self.top_speed
# class Truck(Vehicle): #trucks inherit from vehicles
#     def __init__(self, color, capacity):
#         super().__init__(color) #call constructor on base class
#         self.max_load = capacity
#         self.curr_load = 0
#     def load(self, cargo_weight):
#         if ((self.max_load - self.curr_load) >= cargo_weight): #it fits
#             self.curr_load += cargo_weight
#             print("Current load is", self.curr_load)
#         else:
#             print("Load too big!")
# #Create multiple Vehicle objects, demonstrate that print uses the __str__ function
# #(before we defined it, we got a memory address)
# lightning = Vehicle("red")
# print(lightning)
# mater = Vehicle("brown")
# print(mater)
# #create a Car, show that it inherits __str__ from Vehicle
# lightning = Car("red", 200)
# print(lightning)
# #this throws an error because Vehicles don't have a set_speed method
# #mater.set_speed(50)
# #test the features of a Truck, including inheritance of __str__ and the new load()
# #method
# mater = Truck("brown", 1000)
# print(mater)
# mater.load(600)
# mater.load(410)

# class person:
#
# class student(person):
#     def __init__(self, name, age, degree, hometown):
#         super().__init__(name, age)
#
# class UofUStudent(student):
#     def __init__(self, name, age, degree, hometown, uid):
#         super().__init__(name, age, degree, hometown)
#         self.uid = uid
#
# def whiz_bang(whiz, bang):
#     if whiz:
#         print("whiz")
#     if bang:
#         print("bang")
# print(whiz_bang(2,3))
# #def beep_boop(beeps: int, booper: int)
#whiz_bang(True, True)
# class Persona:
#     def __init__(self, name, persona):
#         self.name = name
#         self.persona = persona
#     def introduction(self):
#         print("I am " + self.name + "," + "my persona is " + self.persona)
# Joker = Persona("joker", "yasen")
# Joker.introduction()
# class Resident_evil(Persona):
#     def introduction(self):
#         print("I am " + self.name + ", I will Kill all of you with my " + self.persona)
# Lyon = Resident_evil("Lyon", "pistol")
# Lyon.introduction()
# class car:
#     def __init__(self, color, type, weight):
#         self.color = color
#         self.type = type
#         self.weight = weight
#     def greeting(self):
#         if self.weight > 100:
#             print("I am a " + self.color + " " + self.type + ", I am too heavy!")
#         else:
#             print("I am a " + self.color + " " + self.type + ", I can aboard!")
#
# Mcqueen = car("red", "racing car", 50)
# Mcqueen.greeting()
# Truck = car("yellow", "truck", 200)
# Truck.greeting()
# class animal:
#     def __init__(self, name):
#         self.name = name
#     def greeting(self):
#         print("Hi, I am " + self.name)
# dog = animal("dog")
# dog.greeting()

# class Trip():
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#
#     def method(self):
#         self.c = self.a - self.b
#         print(self.c)
#
#
# trip = Trip(11, 12)
# trip.method()
# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def talk(self):
#         print("My name is " + self.name + " and I am " + self.age + " years old")
# class student(person):
#     def __init__(self,name, age, degree):
#         self.degree = degree
#         super().__init__(name, age)
#     def report_degree(self):
#         print("My degree is " + self.degree)
# Me = student("zhaoyi", "18", "games")
# Me.report_degree()
# Me.talk()
# pygame.init()
#
# window = pygame.display.set_mode((640, 480))
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
#
# class ImageSwitcher(QWidget):
#     def __init__(self, image1, image2):
#         super.__init__()
#         self.image1 = image1
#         self.image2 = image2
#
#         layout = QVBoxLayout()
#         self.setLayout(layout)
#
#         self.label = QLabel()
#         self.label.setPixmap(self.image1)
#         layout.addWidget(self.label)
#
#         self.button = QPushButton("change picture")
#         layout.addWidget(self.button)
#         self.button.clicked.connect(self.change_image)
#
#     def change_image(self):
#         if self.showing_image1:
#             self.label.setPixmap(self.image2)
#             self.showing_image1 = False
#         else:
#             self.label.setPixmap(self.image1)
#             self.showing_image1 = True
#
#
#     def change_image():
#         print("image changed")
#         label.setPixmap("genm.png")
#
#     def main():
#         app = QApplication([])
#
#         window = QWidget()
#         layout = QVBoxLayout()
#
#
#
#         window.setLayout(layout)
#         window.show()
#
#         app.exec()
#
# if __name__ == "__main__":
#     main()
# def cals_of_food(food):
#     table_of_cals = {"apple":100, "cookie":500}
#     return table_of_cals.get(food, 0)
#
#
#
# total_cals = 0
#
# while True:
#     food = input("What food did you eat?")
#     cals = cals_of_food(food)
#     total_cals += cals
#     print(total_cals)
#
# def sum_from_1_to_n(end_num):
#     total = 0
#     for num in range(1, end_num +1):
#         print(num)
#         total += num
#     return total
#
# print(sum_from_1_to_n(3))
# vals = [3, 4, 5]
# print(vals[0:2])
# vals.append(6)
# print(vals[2])
# print(vals[0:4])
# def add_one(value):
#     new_num = value+1
#     return new_num
# from graphics import *
# win = GraphWin('Drawing', 700, 350, autoflush=False )
# win.setBackground('pink')
#
# def eyes(x, y, win):
#     c1 = Circle(Point(x - 40, y), 30)
#     c2 = Circle(Point(x + 40, y), 30)
#     c1.setFill("blue")
#     c2.setFill("green")
#     c1.draw(win)
#     c2.draw(win)

# c = Circle(Point(150, 250), 60)
# c.setFill("black")
# c.draw(win)
# #
# x = 150
# # y = 200
# frame = 0
# #
# for x in range(100000):
#     win.clear_win()
     # x += 1
     # c = Circle(Point(x, y), 60)
     # c.setFill("black")
     # c.draw(win)
    # eyes(frame, 300, win)
    #
    # win.update()
    # frame = frame + 0.01




#eyes(100, 250, win)

# win.getMouse()
# win.close()
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def talk(self):
#         print('HI, I AM ' + self.name)
#
# Zhaoyi = Person("Zhaoyi")
#
# print(Zhaoyi.talk())
# class Cat:
#     sound = "meow" # Make a variable for the class
#
#     def __init__(self, name):
#         self.name = name # Store a name in the object
#
#     def talk(self):
#         print(self.name + " says " + Cat.sound)
#
#     def greet(self, friend):
#         print(self.name + " says hi to " + friend.name)
#
# # The program will start running at main
# def main():
#     kitty = Cat("Smokey")
#     stray = Cat("Tiger")
#     kitty.name = "King"
#     print(stray.name)
#
# if __name__ == "__main__":
#     main()

# import random
#
# class Dice:
#     def __init__(self, numberOfSides):
#         self.numberOfSides = numberOfSides
#
#     def roll(self):
#         return random.randint(1, self.numberOfSides )
#
#
# def main():
#     dice = Dice(10)
#     dice2 = Dice(10)
#     count = 0
#
#     for i in range(1000):
#         roll1 = dice.roll()
#         roll2 = dice2.roll()
#
#         if roll1 == roll2:
#             print("double found")
#             count += 1
#
#     print(count/10000)
#
# if __name__ == "__main__":
#     main()

# class Enemy:
#     def __init__(self, start_health, greeting):
#         self.health = start_health
#         self.greeting = greeting
#
#     def speak(self):
#         print(self.greeting)
#
#     def take_damage(self, damage):
#         self.health -= damage
#
#
# def main():
#     shadow = Enemy(100, "I'm you")
#     shadow.speak()
#     shadow.take_damage(20)
#     print(shadow.health)
#
#     bugstar = Enemy(10, "No!")
#     bugstar.speak()
#     bugstar.take_damage(5)
#     print(bugstar.health)
#
# if __name__ == "__main__":
#     main()

# with open("1000Sentence.txt") as file:
#     lines = file.readlines()
#
# print(len(lines))
#
# while True:
#     User_input = input("Tell me something: ")
#
#     key_words = User_input.split()
#
#     last_word = key_words[-1]
#
#     for line in lines:
#         if last_word in line:
#             print(line)
#             break

# class test:
#     def __init__(self, value):
#         self.value = value
#
#     def get_value(self):
#         return  self.value
#
# val = test(20)
# print(val.get_value())
class BankAccount:
    def __init__(self, fullname, starting_balance):
        self.balance = starting_balance
        name = fullname.split()
        # change storing a single name into first and last
        self.first_name = name[0]
        self.last_name = name[1]
        self.log = [starting_balance]

    def report_on_balance(self):
        print("The account for", self.first_name, self.last_name, "has $", self.balance)

    def deposit(self, amount):
        self.balance += amount
        self.log.append(amount)

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("Request exceeds balance of", self.balance)
        else:
            self.balance -= amount
            self.log.append(-amount)

    def print_log(self):
        for entry in self.log:
            print(entry)


def main():
    savings = BankAccount("Zhaoyi Sun", 100)
    savings.deposit(200)
    savings.withdraw(500)
    savings.withdraw(50)
    print(savings.print_log())

if __name__ == "__main__":
    main()

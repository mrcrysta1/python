# Declaring Classes , methods and Attributes
class Personal_Trainer:
    def __init__ (self,name,email,phone_no,speciality,experience):
        self.name = name
        self.email = email
        self.phone_no = phone_no
        self.speciality = speciality
        self.experience = experience
    def print_info(self):
        print(self.name)
        print(self.email)
        print(self.phone_no)
        print(self.speciality)
        print(self.experience)
        print("\n----------------------------\n")
class Students:
    def __init__ (self,name,email,phone_no,address):
        self.name = name
        self.email =email
        self.phone_no = phone_no
        self.address = address
    def print_info(self):
        print(self.name)
        print(self.email)
        print(self.phone_no)
        print(self.address)
        print("\n----------------------------\n")
class Classes:
    def __init__ (self,date,time,trainer_name,duration,status):
        self.date = date
        self.time= time
        self.trainer_name = trainer_name
        self.duration = duration
        self.status = status
    def print_info(self):
        print(self.date)
        print(self.time)
        print(self.trainer_name)
        print(self.duration)
        print(self.status)
        print("\n----------------------------\n")
class Reviews:
    def __init__ (self,name,review):
        self.name = name
        self.review = review
    def print_info(self):
        print(self.name)
        print(self.review)
        print("\n----------------------------\n")

# Declaring Values

Trainer1 = ["Kevin Brown","kevin@company.com","+1 459 7835474","Yoga Specialist","12 Years", ]
Trainer2 = ["Chris Petterson","chris@company.com","+1 931 7842587","Boot Camp Classes","18 Years", ]
Trainer3 = ["Reba Smith","reba@company.com","+1 142 7836578","Sports Trainer","7 Years", ]

Student1 = ["John Doe","john@company.com","+1 130 456731","123 Main Street, Seattle, WA 98101"]
Student2 = ["Jane","jane@company.com","+1 130 4585246","789 Oak Street, Tacoma, WA 98401"]
Student3 = ["Susan Smith","susan@company.com","+1 130 7523654","456 Elm Street, Spokane, WA 99201"]

Class1 = ["19-5-23","18:00","Kevin Brown","2 Hours","Upcomming"]
Class2 = ["19-5-23",":20:00","Chris Petterson","2 Hours","Upcomming"]
Class3 = ["21-5-23","08:00","Reba Smith","4 Hours","Upcomming"]

Review1 =["John Doe","The teaching and instruction are absolutely dynamic, they have the ability to break down movements and teach it at a level suited to the student. I just look at the number of students that have had some type of disability and what he has managed to do for them."]
Review2 =["Jane", "Come to think of it, I am slightly disappointed that I missed out on the Competition the other weekend. It’s hard to keep track of all the events going on just of late."]
Review3 =["Susan Smith" , "I really like the whole atmosphere that they create. On one hand it’s inviting, fun, and motivating, while on the other hand its challenging, and at times downright hard."]

# Declaring and Initializing Class Objects

t1 = Personal_Trainer(*Trainer1)
t2 = Personal_Trainer(*Trainer2)
t3 = Personal_Trainer(*Trainer2)

s1 = Students(*Student1)
s2 = Students(*Student2)
s3 = Students(*Student3)

c1 = Classes(*Class1)
c2 = Classes(*Class2)
c3 = Classes(*Class3)

r1 = Reviews(*Review1)
r2 = Reviews(*Review2)
r3 = Reviews(*Review3)

# Calling Method to print values

t1.print_info()
t2.print_info()
t3.print_info()

s1.print_info()
s2.print_info()
s3.print_info()

c1.print_info()
c2.print_info()
c3.print_info()

r1.print_info()
r2.print_info()
r3.print_info()

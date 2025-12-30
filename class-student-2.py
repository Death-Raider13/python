class Student:
    grade=10
    name="John"

    def introduction(self):
        print("Hi, I am", self.name, "and I am a student of grade", self.grade)

    def details(self):
            print("My name is", self.name)
            print("I study in grade", self.grade)
ob = Student()
ob.introduction()
ob.details()

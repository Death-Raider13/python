with open("A-journey.txt", "w") as file:
    file.write("Hi I am Lateef and am learning Python")
    file.close()


with open("A-journey.txt", "r") as file:
    data=file.readlines()
    print("Words In This file are")
    for line in data:
        words=line.split()
        print(words)
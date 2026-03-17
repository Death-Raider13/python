new_file = open("A-journey10.txt", "x")
new_file.close()

import os
print("Checking if my file exists or not....")
if os.path.exists("A-journey10.txt"):
    os.remove("A-journey10.txt")
else:
        print("File does not exist")

my_file = open("A-journey5.txt", "w")
my_file.write("Hi I am Lateef and am learning Python")
my_file.close()

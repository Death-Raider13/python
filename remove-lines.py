file1 = open("A-journey.txt","r")
file2 =open("A-journey2.txt","w")

for line in file1.readlines():
    if not(line.startswith("Coding")):
        print(line)
        file2.write(line)


file1.close
file2.close
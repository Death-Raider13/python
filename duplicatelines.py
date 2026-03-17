#programs to eliminate repeated lines from files

#creating the output lines
outputfile = open("spo.txt", "w")

#reading the input lines
inputfile =open("po.txt", "r")

#holds lines already seen
lines_seen = set()
print("Eliminating duplicate lines")

for line in inputfile:
    if line not in lines_seen:
        lines_seen.add(line)
        outputfile.write(line)

#closing the files
inputfile.close()
outputfile.close()
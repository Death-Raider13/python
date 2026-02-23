file_read =open('A-journey.txt')
print("file in read mode")
print(file_read.read())
file_read.close()

file_write = open('A-journey.txt','w')
file_write.write("file in write mode")
file_write.write("Hi, I am learning file handling operations in python")
file_write.close()


file_append = open('A-journey.txt','a')
file_append.write("\n file in append mode")
file_append.write("I am enjoying learning file handling operations in python")
file_append.close()
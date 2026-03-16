fil_read = open("A-journey.txt", "r")
print("File in Read Mode -")
print(fil_read.read())
fil_read.close()

file_write = open("polynominal.txt", "w")
file_write.write("This is a new content in the file.")
file_write.write("\nThis will overwrite the previous content.")
file_write.close()

fie_append = open("polynominal.txt", "a")
fie_append.write("\nThis line will be added to the end of the file.")
fie_append.close()
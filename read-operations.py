file = open("A-journey.txt", "r")
print(file.read())
file.close()

file = open("A-journey.txt", "r")
print("\n Reading first 8 characters:\n")
print(file.read(8))
file.close()

file = open("polynominal.txt", "a")
file.write("Hi, My name is Lattef and am 17 years old.")
file.close()
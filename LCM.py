numberLargest = int(input("Enter Largest number:"))
numberSmallest = int(input("Enter Smallest Number:"))

if numberLargest > numberSmallest:
    greater=numberLargest
else:
    greater=numberSmallest

while True:
    if greater % numberLargest == 0 and greater % numberSmallest == 0:
        lcm = greater
        break
    greater += 1

print("LCM is:", lcm)
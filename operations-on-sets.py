my_set={1,2,2,4,4,5,3,3}
print("Set:", my_set)

my_set.add(6)
print("Updated Set after adding 6:", my_set)

set1= my_set
set2 ={2,4,6,4}

print("\nSet1:", set1)
print("Set2:", set2)
print("Differnce")
print(set1.difference(set2))
print("Symmetric Differnce")
print(set1.symmetric_difference(set2))
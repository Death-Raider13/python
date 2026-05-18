def sum_m(n):
    return n*(n +1)//2
print("Sum of first 10 natural numbers is(n=5) ",sum_m(5))




def array_sum(a):
    total=0
    for i in a:
        total += 1
    return total

a=[1,2,3,4,5]
print("Sum of array is ",array_sum(a))






def summ(n):
    if n<=0:
        return 0
    return n+ summ(n-1)
print("Recursive sum (n=5):",summ(5))
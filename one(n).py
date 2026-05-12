def Ontime(n):
    iteration=0
    for i in range(1,n+1):
        iteration+=1
    print("when n is", n, "the total iteration done by the code is",iteration)

    Ontime(20)
    Ontime(10)
    Ontime(42)

    print("\n With any 'n' the time taken by our code will change as it is directly proportional to n")
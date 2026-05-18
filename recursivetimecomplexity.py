def prints(n):
    if n <=0:
        return
    print("Hello World")
    prints(n //2)
    prints(n //2)
prints(8)
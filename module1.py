def fact(am):
    f = 1
    for i in range(1,am+1):
        f = f*i
    return f
am = int(input("Enter any number "))
print("factorial of ",am ,"is ",fact(am))

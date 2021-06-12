def fact(n):
    if n==0:
        return 1
    return n * fact(n-1)
x= int (input("Enter the number:"))
res = fact(x)
print("Factorial of {} is {}".format(x,res))

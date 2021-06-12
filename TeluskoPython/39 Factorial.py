
def fact(n):
    d=1
    for i in range(1,n+1):
        d=d*i
    return d

x = int(input("Enter the of factorial:"))

result= fact(x)
print("Factorial of {} is {}".format(x,result))
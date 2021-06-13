#Code1 Factorial Using Numbers
def fact(n):
    d=1
    for i in range(1,n+1):
        d=d*i
    return d
x = int(input("Enter the of factorial:"))
result= fact(x)
print("Factorial of {} is {}".format(x,result))
print()

#Code2 Factorial Using Recursion
def fact(n):
    if n==0:
        return 1
    return n * fact(n-1)
x= int (input("Enter the number:"))
res = fact(x)
print("Factorial of {} is {}".format(x,res))
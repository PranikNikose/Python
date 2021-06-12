
def fib(n):
    a = 0
    b = 1
    if n < 0:
        print("Negative Number")
    elif n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            print(c)


x = int(input("Enter the length:"))
fib(x)
print()

#code2 using While Loop
print("Code2")
a = 0
b = 1
if x < 0:
    print("Negative Number")
elif x == 1:
    print(a)
else:
    print(a)
    print(b)
    w = 3
    while (w <= x):
        d = a + b
        a = b
        b = d
        print(d)
        w += 1




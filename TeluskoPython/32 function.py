#Code1 Function Example
def GM():
    print("Hello")
    print("Good Morning Dear")
    print()
GM()

#Code2 to add with parameters
def add(x,y):
    c=x+y
    print("Addition=",c)
    print()
add(7,8)

#Code3 To return and store value
def sub(a,b):
    r = a-b
    return r
res = sub (10,2)
print( "Substraction=",res)
print()

#Code4 to Return Value
def add_sub(p,q):
    r1=p+q
    r2=p-q
    return r1,r2
res1,res2=add_sub(10,5)
print("Addition=",res1, "Substraction=",res2)
print()

